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
from pathlib import Path

from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langchain_together import ChatTogether
from prompts.rogers_values import PCT_PROMPT_TEMPLATE, ROGERS_TRAITS
from prompts.tof_values import TOF_PROMPT_TEMPLATE, TOF_TRAITS
from prompts.rvs_values import RVS_PROMPT_TEMPLATE, RVS_TRAITS
from prompts.response_generation import BASELINE_GENERATION_PROMPT
from prompts.cot_generations import ROGERIAN_PROMPT # Remove tooling for current release.

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
data_dir = Path("../data/raw_reddit")
secret_outputs = Path("../data/outputs") # Untracked folder for full outputs with PII.
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
        self._response_models = {
            'claude' : ChatAnthropic(model="claude-3-5-sonnet-20241022"),
            'gpt-4o': ChatOpenAI(model="gpt-4o"),
            'llama31': ChatTogether(model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo"),
            'gpt-oss': ChatTogether(model="openai/gpt-oss-120b")
         } # List of models to generate responses.

        self._judge_model = ChatOpenAI(model="gpt-4o")
        # The judge model used to evaluate the response.
        self.paradigms = ['pct', 'tof', 'rvs']

    def extract_posts(data_dir = data_dir) -> None:
        pass

    def generate_llm_response(self, cot_mode: bool) -> None:

        for model in self._response_models:
                # Generate responses using each model.
            if self.cot_mode:
            # The cot_mode subsystem uses chain-of-thought prompting.
                self.generation_prompt = ROGERIAN_PROMPT
                # Invoke the chain-of-thought prompting generation method.
            else:
                self.generation_prompt = BASELINE_GENERATION_PROMPT
                # Invoke the baseline generations with langchain.

    def annotate_responses(self) -> None:

        # Annotate the responses using the judge model and the paradigm prompts.
        for paradigm in self.paradigms:
            if paradigm == 'pct':
                self.annotation_prompt = PCT_PROMPT_TEMPLATE
                self.values_list = ROGERS_TRAITS
            elif paradigm == 'tof':
                self.annotation_prompt = TOF_PROMPT_TEMPLATE
                self.values_list = TOF_TRAITS
            elif paradigm == 'rvs':
                self.annotation_prompt = RVS_PROMPT_TEMPLATE
                self.values_list = RVS_TRAITS
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

    def run(self, cot_mode: bool) -> None:
        logger.info("Beginning DeepReflectPipeline...")

        logger.info("Extracting posts...")
        self.extract_posts()

        logger.info("Generating LLM responses...")
        self.generate_llm_response(cot_mode)

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

    pipeline = DeepReflectPipeline(subreddit, num_posts, cot_mode)

    # Run the pipeline.
    pipeline.run()

    return None

if __name__ == "__main__":
    results = main()