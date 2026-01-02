# 🤖 LLM Code Generation Benchmark

> A benchmarking framework for evaluating Large Language Models on code synthesis tasks.
> 
> Developed during a research internship at **IRISA/DIVERSE Team** (Inria Rennes, France).

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

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

- [x] Benchmark pipeline for HumanEval dataset (164 problems)
- [x] Benchmark pipeline for Puzzle dataset (37 problems)  
- [x] Test 6 different LLMs (GPT-4o, GPT-3.5, LLaMA, Gemma, Mixtral)
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
- [ ] Fine-grained analysis of failure patterns
- [ ] Web dashboard for interactive exploration
- [ ] Support for more programming languages (JavaScript, Java, C++)

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