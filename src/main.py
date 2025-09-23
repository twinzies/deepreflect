import argparse
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
data_dir = Path("../data/raw_reddit")
output_dir = Path("../data/dr-outputs")

class DeepReflectPipeline:
    """Pipeline to analyze and compare Reddit human-authored responses and LLM generated ones to personal queries."""

    def __init__(self, data_dir: Path, output_dir: Path, cot_mode: bool = False, num_posts: int = 1, subreddit: str = None) -> None:
        self.data_dir = data_dir
        self.output_dir = output_dir
        self.subreddit = subreddit # If None, dataset not expected to be RedArcs.
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.num_posts = num_posts
        self.cot_mode = cot_mode

    def run(self, cot_mode: bool) -> None:
        pass

def main():
    # Read in csv file as per the argument.

    parser = argparse.ArgumentParser(
        description='Subreddit to process the raw data from.'
    )

    parser.add_argument('--subreddit', 
                       type=str, 
                       choices=['Anxiety', 'AITAH'],
                       help='Choose the scenario to analyze: Anxiety or AITAH')

    parser.add_argument('--num_posts',
                       type=int,
                       default=10,
                       help='Number of top posts to process from the subreddit.')

    parser.add_argument('--cot_mode',
                          action='store_true',
                          help='If set, use chain-of-thought prompting for generating the LLM responses.') 

    args = parser.parse_args()
    subreddit = args.subreddit
    num_posts = args.num_posts
    cot_mode = args.cot_mode

    pipeline = DeepReflectPipeline(subreddit, num_posts, cot_mode)

    # Run the pipeline.
    pipeline.run()

    return None

if __name__ == "__main__":
    results = main()