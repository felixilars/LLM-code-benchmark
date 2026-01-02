# LLM Code Generation Benchmark

> A benchmarking framework for evaluating Large Language Models on code synthesis tasks.
> 
> Developed during a research internship at **IRISA/DIVERSE Team** (Inria Rennes, France), June - August 2024.

---

## 📖 Introduction

This project provides tools to systematically evaluate LLMs on programming tasks. The goal is to:

1. **Compare models** - Both proprietary (GPT-4o, GPT-3.5) and open-source (LLaMA, Gemma, Mixtral)
2. **Identify weaknesses** - Find problem types where AI struggles compared to humans
3. **Measure progress** - Track improvements across model generations

### Why this matters?

While LLMs show impressive coding abilities, they still fail on certain problem types. Understanding *where* and *why* they fail helps:
- Researchers improve model training
- Developers know when to trust AI-generated code
- Educators understand AI limitations

---

## 📊 Current Results

### Model Comparison (6 models tested)

| Model | HumanEval (100%) | HumanEval (50%+) | Puzzle |
|-------|:----------------:|:----------------:|:------:|
| 🥇 **GPT-4o** | **91.41%** | **95.09%** | **72.97%** |
| 🥈 gemma2-9b-it | 63.19% | 85.28% | 45.95% |
| 🥉 llama3-groq-8b | 50.92% | 77.30% | 16.22% |
| GPT-3.5-turbo | 47.85% | 55.21% | 32.43% |
| mixtral-8x7b | 34.36% | 46.01% | 24.32% |
| llama3-70b | 31.90% | 36.81% | 27.03% |

### Key Findings

| Finding | Details |
|---------|---------|
| 🏆 GPT-4o dominates | 91.4% accuracy, nearly 2x better than GPT-3.5 |
| 🧩 Puzzle is harder | All models drop 15-35% compared to HumanEval |
| 💡 Size ≠ Performance | gemma2-9b (63%) beats llama3-70b (32%) |
| 🔄 Partial correctness | Some models often "almost right" but miss edge cases |

---

## ✅ Progress & Roadmap

### Done

- [x] Benchmark pipeline for datasets such as HumanEval, puzzel_human-labeled
- [x] Test different LLMs (GPT-4o, GPT-3.5, LLaMA, Gemma, Mixtral)
- [x] Automated code extraction from LLM responses
- [x] Sandboxed code execution with timeout handling
- [x] Results analysis and visualization
- [x] Pass@k metrics implementation

### In Progress

- [ ] Detailed error categorization (syntax error, logic error, timeout, etc.)
- [ ] Per-problem difficulty analysis

### Future Improvements

- [ ] Add more datasets (MBPP, CodeContests, APPS)
- [ ] Test newer models (Claude 3, Gemini Pro, DeepSeek Coder)

### Potential Extensions

> 💡 **This framework can be extended to:**
> - Compare prompt engineering techniques
> - Test chain-of-thought vs direct generation
> - Evaluate code explanation capabilities
> - Benchmark debugging abilities

---

## 🚀 Quick Start

### Prerequisites

```bash
Python 3.8+
OpenAI API key (for GPT models)
Groq API key (for open-source models, optional)
```
### Installation

```bash

git clone https://github.com/felixilars/llm-code-benchmark.git
pip install -r requirements.txt

# Set up API keys
export OPENAI_API_KEY="your-openai-key"
export GROQ_API_KEY="your-groq-key"  # optional
```
### Run Benchmark
```bash

# Generate code with GPT-4
python generate_response.py -d HumanEval -m gpt-4 -n 5 -t 1.0 -s 0

# Analyze results
python intermedia_analyze.py -f ./log/dataset_HumanEval_model_gpt-4_topn_5_temperature_1.0.log_0
```
### View Results
```bash

# Quick analysis
python run_analysis.py

# Or run individual modules
python -m analysis.results_data      # View results table
python -m analysis.visualize         # Create visualizations
python -m analysis.metrics           # Calculate Pass@k

```
## 📚 References

- [HumanEval](https://github.com/openai/human-eval) - OpenAI's code generation benchmark
- [Evaluating Large Language Models Trained on Code](https://arxiv.org/abs/2107.03374) - Codex paper (Pass@k methodology)
- [Programming Puzzles](https://github.com/microsoft/PythonProgrammingPuzzles) - Microsoft's puzzle dataset

---

## 🙏 Acknowledgments

This project was developed during a research internship at **IRISA/DIVERSE Team** (Inria Rennes, France) in Summer 2024.

I would like to thank:

- **DIVERSE Team at IRISA** - For the opportunity, research supervision, mentorship, and providing access to computational resources and API credits
- **Inria Rennes** - For hosting and supporting this research internship
