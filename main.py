import logging
import shutil
from pathlib import Path
from typing import Dict, List, Set

import pandas as pd
import pyreadstat

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataPipeline:
    """Pipeline to analyze and compare human vs LLM responses to personal queries."""

    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.data_path = self.base_path / "data"
        self.spss_path = self.data_path / "spss"
        self.backup_path = self.base_path / "backup"

    def load_claude_missing_postids(self, subreddit: str) -> Set[str]:
        """Fix analysis: Load Claude missing post IDs from audit file."""
        audit_file = self.base_path / f"{subreddit}_missing_responses_audit_full.csv"

        if not audit_file.exists():
            logger.warning(f"Audit file not found: {audit_file}")
            return set()

        df = pd.read_csv(audit_file)
        claude_row = df[df['model_name'] == 'claude']

        if claude_row.empty:
            logger.warning(f"No Claude records found in {audit_file}")
            return set()

        postid_str = claude_row.iloc[0]['list_postid']
        postids = set(pid.strip() for pid in postid_str.split(',') if pid.strip())

        logger.info(f"Loaded {len(postids)} Claude missing post IDs for {subreddit}")
        return postids

    def create_backup(self, file_path: Path):
        """Fix analysis: Create backup of original file."""
        self.backup_path.mkdir(exist_ok=True)
        backup_file = self.backup_path / file_path.name
        shutil.copy2(file_path, backup_file)
        logger.info(f"Created backup: {backup_file}")

    def remove_records_from_csv(self, subreddit: str, missing_postids: Set[str]):
        """Fix analysis: Remove records matching missing post IDs from CSV files."""
        for response_source in ['llm', 'reddit']:
            csv_file = self.data_path / f"{subreddit}_evaluated_{response_source}_responses.csv"

            if not csv_file.exists():
                logger.warning(f"CSV file not found: {csv_file}")
                continue

            # Create backup
            self.create_backup(csv_file)

            # Load and filter data
            df = pd.read_csv(csv_file)
            original_count = len(df)

            if 'post_id' not in df.columns:
                logger.warning(f"No 'post_id' column found in {csv_file}")
                continue

            # Remove records with post_ids in missing list
            df['post_id_str'] = df['post_id'].astype(str)
            filtered_df = df[~df['post_id_str'].isin(missing_postids)]
            filtered_df = filtered_df.drop('post_id_str', axis=1)

            removed_count = original_count - len(filtered_df)

            # Save filtered data
            filtered_df.to_csv(csv_file, index=False)
            logger.info(f"Removed {removed_count} records from {csv_file} "
                       f"({original_count} -> {len(filtered_df)} records)")

    def remove_records_from_spss(self, subreddit: str, missing_postids: Set[str]):
        """Fix analysis: Remove records matching missing post IDs from SPSS files."""
        spss_patterns = [
            f"{subreddit}_model_responses-annotated.sav",
            f"{subreddit}_reddit_responses-annotated.sav"
        ]

        for pattern in spss_patterns:
            spss_file = self.spss_path / pattern

            if not spss_file.exists():
                logger.warning(f"SPSS file not found: {spss_file}")
                continue

            try:
                # Create backup
                self.create_backup(spss_file)

                # Load SPSS data
                df, meta = pyreadstat.read_sav(str(spss_file))
                original_count = len(df)

                if 'post_id' not in df.columns:
                    logger.warning(f"No 'post_id' column found in {spss_file}")
                    continue

                # Remove records with post_ids in missing list
                df['post_id_str'] = df['post_id'].astype(str)
                filtered_df = df[~df['post_id_str'].isin(missing_postids)]
                filtered_df = filtered_df.drop('post_id_str', axis=1)

                removed_count = original_count - len(filtered_df)

                # Save filtered data back to SPSS
                pyreadstat.write_sav(filtered_df, str(spss_file),
                                   variable_value_labels=meta.variable_value_labels,
                                   variable_display_width=meta.variable_display_width,
                                   variable_measure=meta.variable_measure)

                logger.info(f"Removed {removed_count} records from {spss_file} "
                           f"({original_count} -> {len(filtered_df)} records)")

            except Exception as e:
                logger.error(f"Error processing SPSS file {spss_file}: {e}")

    def process_subreddit(self, subreddit: str) -> Dict[str, int]:
        """Fix analysis: Process a single subreddit and remove matching records."""
        logger.info(f"Processing subreddit: {subreddit}")

        # Load Claude missing post IDs
        missing_postids = self.load_claude_missing_postids(subreddit)
        if not missing_postids:
            logger.info(f"No Claude missing post IDs found for {subreddit}")
            return {'csv_removed': 0, 'spss_removed': 0}

        # Remove records from CSV files
        logger.info(f"Removing records from CSV files for {subreddit}")
        self.remove_records_from_csv(subreddit, missing_postids)

        # Remove records from SPSS files
        logger.info(f"Removing records from SPSS files for {subreddit}")
        self.remove_records_from_spss(subreddit, missing_postids)

        return {'missing_postids_count': len(missing_postids)}

    def run_analysis_fix(self, subreddits: List[str] = None) -> Dict[str, Dict[str, int]]:
        """Run the Fix analysis methods for specified subreddits."""
        if subreddits is None:
            subreddits = ['AITAH', 'Anxiety']

        results = {}

        logger.info("Starting record removal pipeline...")

        for subreddit in subreddits:
            try:
                result = self.process_subreddit(subreddit)
                results[subreddit] = result

            except Exception as e:
                logger.error(f"Error processing {subreddit}: {e}")
                results[subreddit] = {'error': str(e)}

        return results

def main():
    """Main pipeline execution."""
    pipeline = DataPipeline()

    # Run pipeline for both subreddits
    results = pipeline.run_analysis_fix(['AITAH', 'Anxiety'])

    # Print summary
    print("\n=== Record Removal Pipeline Summary ===")
    total_missing = 0
    for subreddit, result in results.items():
        if 'missing_postids_count' in result:
            count = result['missing_postids_count']
            total_missing += count
            print(f"{subreddit}: Processed {count} Claude missing post IDs")
        elif 'error' in result:
            print(f"{subreddit}: Error - {result['error']}")
        else:
            print(f"{subreddit}: No missing post IDs to process")

    print(f"Total Claude missing post IDs processed: {total_missing}")
    print("Backups created in: backup/")

    return results

if __name__ == "__main__":
    results = main()