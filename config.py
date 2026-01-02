# Configuration for LLM Code Benchmark

import os

# API
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")

# Model options
AVAILABLE_MODELS = [
    "gpt-3.5-turbo",
    "gpt-4",
    "gpt-4-turbo",
]

# Default parameters
DEFAULT_TOPN = 5
DEFAULT_TEMPERATURE = 1.0
DEFAULT_TIMEOUT = 3  # seconds

# Paths
DATASETS_DIR = "./Datasets"
LOG_DIR = "./log"
RECORD_DIR = "./log/record"

# HumanEval paths
HUMANEVAL_PATH = f"{DATASETS_DIR}/HumanEval/HumanEval.jsonl"
HUMANEVAL_NEW_PATH = f"{DATASETS_DIR}/HumanEval/HumanEval_new.jsonl"

# Puzzle paths  
PUZZLE_PATH = f"{DATASETS_DIR}/puzzle_human-labeled/puzzle_new.jsonl"
PUZZLE_FILTERED_PATH = f"{DATASETS_DIR}/puzzle_human-labeled/puzzle_filtered.jsonl"