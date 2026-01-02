#Metrics calculation for LLM code generation benchmark
import json
import os
from typing import List, Dict


def estimate_pass_at_k(n: int, c: int, k: int) -> float:
    """
    Unbiased estimator for pass@k
    
    Args:
        n: total number of samples
        c: number of correct samples  
        k: k in pass@k
    """
    if n - c < k:
        return 1.0
    if c == 0:
        return 0.0
    
    result = 1.0
    for i in range(k):
        result *= (n - c - i) / (n - i)
    
    return 1.0 - result

def calculate_pass_at_k_from_file(results_file: str, k_values: List[int] = [1, 5]) -> Dict:
    """
    Calculate pass@k metrics from log file
    """
    if not os.path.exists(results_file):
        print(f"File not found: {results_file}")
        return None
    
    problems = []
    with open(results_file, 'r') as f:
        for line in f:
            if line.strip():
                problems.append(json.loads(line))
    
    print(f"Loaded {len(problems)} problems from {results_file}")
    
    pass_at_k_results = {k: [] for k in k_values}
    problem_details = []
    
    for problem in problems:
        name = problem.get('name', 'unknown')
        candidates = problem.get('code_candidates', [])
        n = len(candidates)
        cnt = 0
        for candidate in candidates:
            passed = candidate.get('passed_case', [])
            
            if passed == 'Pass':
                cnt += 1
            elif isinstance(passed, list):
                # For HumanEval: check if all tests passed
                case_status = candidate.get('case_status', [])
                if case_status:
                    pass_count = sum(1 for s in case_status if s not in ['Timeout', 'Exception', 'execution error'])
                    if pass_count == len(case_status) and len(passed) > 0:
                        cnt += 1
                elif len(passed) > 0:
                    cnt += 1
        
        # pass@k
        for k in k_values:
            if n >= k:
                p_at_k = estimate_pass_at_k(n, cnt, k)
                pass_at_k_results[k].append(p_at_k)
        
        problem_details.append({
            'name': name,
            'n_samples': n,
            'n_correct': cnt,
            'pass_rate': cnt/n if n>0 else 0
        })
    
    # Calculate averages
    summary = {}
    for k in k_values:
        if pass_at_k_results[k]:
            avg = sum(pass_at_k_results[k]) / len(pass_at_k_results[k])
            summary[f'pass@{k}'] = avg
        else:
            summary[f'pass@{k}'] = 0.0
    
    return {
        'summary': summary,
        'total_problems': len(problems),
        'details': problem_details
    }


def analyze_all_results(record_dir: str = "./log/record"):
    """Analyze all result files in record directory"""
    
    if not os.path.exists(record_dir):
        print(f"Directory not found: {record_dir}")
        return
    
    print("\n" + "="*70)
    print("ANALYZING ALL RESULT FILES")
    print("="*70)
    
    for filename in os.listdir(record_dir):
        filepath = os.path.join(record_dir, filename)
        
        if os.path.isfile(filepath) and not filename.startswith('.'):
            print(f"\n📁 {filename}")
            print("-"*50)
            
            results = calculate_pass_at_k_from_file(filepath)
            
            if results:
                print(f"   Total problems: {results['total_problems']}")
                for metric, value in results['summary'].items():
                    print(f"   {metric}: {value:.2%}")
                
                # Hardest problems
                sorted_problems = sorted(
                    results['details'],
                    key=lambda x: x['pass_rate']
                )
                
                print(f"\n   Hardest problems (0% pass rate):")
                hard_count = 0
                for p in sorted_problems:
                    if p['pass_rate'] == 0 and hard_count < 5:
                        print(f"      - {p['name']}")
                        hard_count += 1


if __name__ == "__main__":
    analyze_all_results()