#Visualization for benchmark results

from analysis.results_data import BENCHMARK_RESULTS, MODEL_INFO, get_summary_stats

def ascii_bar_chart(title: str, data: dict, max_val: float = 100):
    """Create ASCII bar chart"""
    print("\n" + "="*70)
    print(title)
    print("="*70)
    bar_width = 40
    sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
    
    for name, value in sorted_data:
        bar_length = int((value / max_val) * bar_width)
        bar = "█" * bar_length + "░" * (bar_width - bar_length)
        
        # Add marker for open-source
        marker = "🔓" if MODEL_INFO.get(name, {}).get("type") == "open-source" else "🔒"
        
        print(marker + " " + name.ljust(20) + " |" + bar + "| " + str(round(value, 1)) + "%")


def compare_datasets():
    """Compare performance across datasets"""
    
    print("\n" + "="*70)
    print("DATASET COMPARISON: HumanEval vs Puzzle")
    print("="*70)
    print("Model".ljust(22) + " " + "HumanEval".rjust(12) + " " + "Puzzle".rjust(12) + " " + "Gap".rjust(12))
    print("-"*70)
    
    stats = get_summary_stats()
    sorted_stats = sorted(stats.items(), key=lambda x: x[1]['puzzle_gap'], reverse=True)
    
    for model, data in sorted_stats:
        gap = data['puzzle_gap']
        gap_str = f"-{gap:.1f}%" if gap > 0 else f"+{abs(gap):.1f}%"
        print(model.ljust(22) + " " + f"{data['humaneval_100']:>11.1f}%" + " " + f"{data['puzzle']:>11.1f}%" + " " + gap_str.rjust(12))
    
    print("-"*70)
    print("Gap = HumanEval - Puzzle (negative means Puzzle is harder)")


def compare_partial_correctness():
    """Compare 100% correct vs 50%+ correct"""
    
    print("\n" + "="*70)
    print("PARTIAL CORRECTNESS: 100% vs 50%+ correct")
    print("="*70)
    print("Model".ljust(22) + " " + "100% correct".rjust(14) + " " + "50%+ correct".rjust(14) + " " + "Gap".rjust(10))
    print("-"*70)
    
    stats = get_summary_stats()
    sorted_stats = sorted(stats.items(), key=lambda x: x[1]['partial_gap'], reverse=True)
    
    for model, data in sorted_stats:
        gap = data['partial_gap']
        print(f"{model:<22} {data['humaneval_100']:>13.1f}% {data['humaneval_50plus']:>13.1f}% +{gap:>8.1f}%")
    
    print("-"*70)
    print("Large gap = model often partially correct but misses edge cases")


def show_insights():
    """Show key insights from data"""
    
    stats = get_summary_stats()
    
    print("\n" + "="*70)
    print("🔍 KEY INSIGHTS")
    print("="*70)
    
    # Best overall
    best = max(BENCHMARK_RESULTS.items(), key=lambda x: x[1]["humaneval_100"])
    print("\nBest overall: " + best[0] + " (" + str(round(best[1]['humaneval_100'], 1)) + "%)")
    
    # Best open-source
    open_source = {k: v for k, v in BENCHMARK_RESULTS.items() 
                   if MODEL_INFO[k]["type"] == "open-source"}
    best_os = max(open_source.items(), key=lambda x: x[1]["humaneval_100"])
    print("Best open-source: " + best_os[0] + " (" + str(round(best_os[1]['humaneval_100'], 1)) + "%)")
    
    # Gap between best proprietary and best open-source
    gap = best[1]["humaneval_100"] - best_os[1]["humaneval_100"]
    print("Proprietary vs Open-source gap: " + str(round(gap, 1)) + "%")
    
    # Most affected by puzzle difficulty
    most_affected = max(stats.items(), key=lambda x: x[1]["puzzle_gap"])
    print("\nMost affected by Puzzle difficulty: " + most_affected[0])
    print("   (drops " + str(round(most_affected[1]['puzzle_gap'], 1)) + "% from HumanEval to Puzzle)")
    
    # Highest partial correctness
    most_partial = max(stats.items(), key=lambda x: x[1]["partial_gap"])
    print("\nHighest partial correctness: " + most_partial[0])
    print("   (+" + str(round(most_partial[1]['partial_gap'], 1)) + "% between 50%+ and 100% correct)")
    
    # Small model beats large
    print("\nInteresting: gemma2-9b-it (63.2%) > llama3-70b (31.9%)")
    print("   9B params outperforms 70B params by " + str(round(63.19 - 31.90, 1)) + "%!")

def create_all_visualizations():
    """All visualizations"""
    
    # HumanEval 100% correct
    humaneval_100 = {m: v["humaneval_100"] for m, v in BENCHMARK_RESULTS.items()}
    ascii_bar_chart("HUMANEVAL PERFORMANCE (100% Correct)", humaneval_100)
    
    # Puzzle performance
    puzzle = {m: v["puzzle"] for m, v in BENCHMARK_RESULTS.items()}
    ascii_bar_chart("PUZZLE PERFORMANCE", puzzle)
    
    # Comparisons
    compare_datasets()
    compare_partial_correctness()
    
    # Insights
    show_insights()


def try_matplotlib():
    """create matplotlib chart if available"""
    import matplotlib.pyplot as plt
    import numpy as np
    
    models = list(BENCHMARK_RESULTS.keys())
    humaneval = [BENCHMARK_RESULTS[m]["humaneval_100"] for m in models]
    puzzle = [BENCHMARK_RESULTS[m]["puzzle"] for m in models]
    
    x = np.arange(len(models))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    bars1 = ax.bar(x - width/2, humaneval, width, label='HumanEval (100%)', color='steelblue')
    bars2 = ax.bar(x + width/2, puzzle, width, label='Puzzle', color='coral')
    
    ax.set_ylabel('Accuracy (%)')
    ax.set_title('LLM Code Generation Benchmark Results')
    ax.set_xticks(x)
    ax.set_xticklabels(models, rotation=45, ha='right')
    ax.legend()
    ax.set_ylim(0, 100)
    ax.grid(axis='y', alpha=0.3)
    
    # Add value labels
    for bar in bars1:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}%',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=8)
    
    for bar in bars2:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}%',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=8)
    
    plt.tight_layout()
    plt.savefig('benchmark_results.png', dpi=150, bbox_inches='tight')
    print("\nChart saved to: benchmark_results.png")
    plt.show()
    
    return True


if __name__ == "__main__":
    create_all_visualizations()
    print("\n" + "-"*70)
    print("Creating matplotlib chart...")
    try_matplotlib()