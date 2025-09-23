"""
DeepReflect: A Pipeline for Analyzing and generating responses to personal queries.
===========================================

This module implements a pipeline to analyze and generate responses to personal queries using LLMs.

Author: Tara K. Jain
Copyright (c) 2025. All rights reserved.
Version: 1.0.0
License: Proprietary
"""

import argparse
import logging
import os
import sys
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langchain_together import ChatTogether

# Add the project root to Python path
sys.path.append(str(Path(__file__).parent.parent))
from prompts.cot_generations import (
    ROGERIAN_PROMPT,  # Remove tooling for current release.
)
from prompts.goffman_behaviors import TOF_PROMPT_TEMPLATE, TOF_TRAITS
from prompts.response_generation import BASELINE_GENERATION_PROMPT
from prompts.rogers_values import PCT_PROMPT_TEMPLATE, PCT_TRAITS
from prompts.rokeach_values import RVS_PROMPT_TEMPLATE, RVS_INSTRUMENTAL_TRAITS, RVS_TERMINAL_TRAITS
from prompts.goffman_behaviors import TOF_PROMPT_TEMPLATE, TOF_TRAITS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
data_dir = Path("data/raw_reddit/")
secret_outputs = Path("data/outputs") # Untracked folder for full outputs with PII.
output_dir = Path("data/dr-outputs")

# Load environment variables from .env file
load_dotenv()

class DeepReflectPipeline:
    """Pipeline to analyze and compare Reddit human-authored responses and LLM generated ones to personal queries."""

    def __init__(self, cot_mode: bool = False, num_posts: int = 5, subreddit: str = None) -> None:

        self.data_dir = data_dir
        self.output_dir = output_dir
        self.subreddit = subreddit # If None, dataset not expected to be RedArcs.
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.num_posts = num_posts
        self.cot_mode = cot_mode
        self.df = None # Start with the audited records. 

        # Ensure API keys are set for the pipeline to run.
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        if not os.getenv("ANTHROPIC_API_KEY"):
            raise ValueError("ANTHROPIC_API_KEY not found in environment variables")
        if not os.getenv("TOGETHER_API_KEY"):
            raise ValueError("TOGETHER_API_KEY not found in environment variables")

        self._response_models = {
            'claude' : ChatAnthropic(model="claude-3-5-sonnet-20241022"),
            'gpt-4o': ChatOpenAI(model="gpt-4o"),
            'llama31': ChatTogether(model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo"),
            'gpt-oss': ChatTogether(model="openai/gpt-oss-120b")
         } # List of models to generate responses.

        self._judge_model = ChatOpenAI(model="gpt-4o")
        # The judge model used to evaluate the response.
        self.paradigms = ['pct', 'tof', 'rvs']

    def extract_posts(self) -> None:
        self.df = pd.read_csv(f"{data_dir}/audited_top_posts_{self.subreddit}.csv", header=0)
        self.df = self.df.head(self.num_posts) # Limit to num_posts for processing.

        logger.info(f"Loaded {len(self.df)} posts from r/{self.subreddit}")

    def generate_llm_response(self, batch_size:int = 50) -> None:

        if self.num_posts <= batch_size:
            batch_size = self.num_posts

        # Error out if no posts loaded.
        if self.df is None or len(self.df) == 0:
            logger.warning("No posts loaded. Run extract_posts() first.")
            return

        logger.info(f"Generating responses for {len(self.df)} posts")
    
        model_responses = []

        # Generate responses for each post using each model.
        for model_name, llm in self._response_models.items():
            logger.info(f"Generating responses using model: {model_name}")

            # Prepare prompt templates.
            if self.cot_mode:
            # The cot_mode subsystem uses chain-of-thought prompting.

                # Prompts for the chain-of-thought prompting generation method.
                prompts = [
                    ROGERIAN_PROMPT.format(title=self.df['title'], body=self.df['body'])
                    for post in self.df.post_id
                ]

            else:

                # Prompts for the baseline generation method.
                prompts = [
                    BASELINE_GENERATION_PROMPT.format(
                    title=self.df['title'], body=self.df['body'])
                    for post in self.df.post_id
                ]

            # Chunk prompts into batches to avoid rate limits.
            for start in range(0, len(prompts), batch_size):
                end = start + batch_size
                batch_prompts = prompts[start:end]

                responses = llm.batch(batch_prompts)

                for idx, resp in enumerate(responses):
                    model_responses.append(
                        {
                            "post_id": self.df.iloc[start + idx]["post_id"],
                            "model": model_name,
                            "post": self.df.iloc[start + idx]["body"],
                            "title": self.df.iloc[start + idx]["title"],
                            "response": resp.content,
                        }
                    )
                logger.info(f"Generated {len(responses)} responses in batch {start // batch_size + 1}")

                # Save intermediate results to avoid data loss.
                interim_df = pd.DataFrame(model_responses)
                outpath = self.output_dir / f"interim_responses_{self.subreddit}.csv"
                interim_df.to_csv(outpath, index=False)
                logger.info(f"Saved interim results to {outpath}")

                # Invoke langchain for the baseline generations.

        df_llm_responses = pd.DataFrame(model_responses)
        outpath = self.output_dir / f"all_llm_responses_{self.subreddit}.csv" # Save the full responses to the untracked folder.llm_responses_{self.subreddit}. 
        df_llm_responses.to_csv(outpath, index=False)
        logger.info(f"Saved full LLM responses to {outpath}")


    def annotate_responses(self) -> None:

        # Annotate the responses using the judge model and the paradigm prompts.
        for paradigm in self.paradigms:
            if paradigm == 'pct':
                self.annotation_prompt = PCT_PROMPT_TEMPLATE
                self.values_list = PCT_TRAITS
            elif paradigm == 'tof':
                self.annotation_prompt = TOF_PROMPT_TEMPLATE
                self.values_list = TOF_TRAITS
            elif paradigm == 'rvs':
                self.annotation_prompt = RVS_PROMPT_TEMPLATE
                self.values_list = RVS_TERMINAL_TRAITS + RVS_INSTRUMENTAL_TRAITS
            else:
                logger.warning(f"Unknown paradigm: {paradigm}")
                continue

            # Annotate each response for each paradigm.
            pass

    def save_full_outputs(self) -> None:
        # Save the full outputs to the untracked folder.
        pass

    def save_outputs(self) -> None:
        pass

    def run(self) -> None:
        logger.info("Beginning DeepReflectPipeline...")

        logger.info("Extracting posts...")
        self.extract_posts()

        logger.info("Generating LLM responses...")
        self.generate_llm_response()

        logger.info("Loading paradigms...")
        self.load_paradigms()

        logger.info("Annotating responses...")
        self.annotate_responses()

        logger.info("Saving annotated outputs...")
        self.save_outputs()
        return True

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

    pipeline = DeepReflectPipeline(subreddit=subreddit, num_posts=num_posts, cot_mode=cot_mode)

    # Run the pipeline.
    pipeline.run()

    return None

if __name__ == "__main__":
    results = main()