#Benchmark results
# Raw results

BENCHMARK_RESULTS = {
    "GPT-4o": {
        "humaneval_100": 91.41,
        "humaneval_50plus": 95.09,
        "puzzle": 72.97,
    },
    "GPT-3.5-turbo": {
        "humaneval_100": 47.85,
        "humaneval_50plus": 55.21,
        "puzzle": 32.43,
    },
    "llama3-70b-8192": {
        "humaneval_100": 31.90,
        "humaneval_50plus": 36.81,
        "puzzle": 27.03,
    },
    "gemma2-9b-it": {
        "humaneval_100": 63.19,
        "humaneval_50plus": 85.28,
        "puzzle": 45.95,
    },
    "mixtral-8x7b-32768": {
        "humaneval_100": 34.36,
        "humaneval_50plus": 46.01,
        "puzzle": 24.32,
    },
    "llama3-groq-8b-8192": {
        "humaneval_100": 50.92,
        "humaneval_50plus": 77.30,
        "puzzle": 16.22,
    },
}

# Model metadata
MODEL_INFO = {
    "GPT-4o": {"type": "proprietary", "provider": "OpenAI", "size": "unknown"},
    "GPT-3.5-turbo": {"type": "proprietary", "provider": "OpenAI", "size": "unknown"},
    "llama3-70b-8192": {"type": "open-source", "provider": "Meta", "size": "70B"},
    "gemma2-9b-it": {"type": "open-source", "provider": "Google", "size": "9B"},
    "mixtral-8x7b-32768": {"type": "open-source", "provider": "Mistral", "size": "8x7B"},
    "llama3-groq-8b-8192": {"type": "open-source", "provider": "Groq/Meta", "size": "8B"},
}


def get_summary_stats():
    """Summary statistics"""
    stats = {}
    
    for model, results in BENCHMARK_RESULTS.items():
        puzzle_gap = results["humaneval_100"] - results["puzzle"]
        partial_gap = results["humaneval_50plus"] - results["humaneval_100"]
        
        stats[model] = {
            **results,
            "puzzle_gap": puzzle_gap,
            "partial_gap": partial_gap,
            "is_open_source": MODEL_INFO[model]["type"] == "open-source",
        }
    
    return stats


def print_results_table():
    print("\n" + "="*80)
    print("BENCHMARK RESULTS SUMMARY")
    print("="*80)
    print(f"{'Model':<22} {'HumanEval 100%':>15} {'HumanEval 50%+':>15} {'Puzzle':>12}")
    print("-"*80)
    
    sorted_models = sorted(
        BENCHMARK_RESULTS.items(),
        key=lambda x: x[1]["humaneval_100"],
        reverse=True
    )
    
    for model, scores in sorted_models:
        print(f"{model:<22} {scores['humaneval_100']:>14.2f}% {scores['humaneval_50plus']:>14.2f}% {scores['puzzle']:>11.2f}%")
    
    print("="*80)

print_results_table()