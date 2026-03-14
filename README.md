# Automated Testing for LLMOps

![CI](https://github.com/rezaparamarta/automated-testing-llmops/actions/workflows/tests.yml/badge.svg)

This project demonstrates how to build **automated evaluation pipelines for LLM-powered applications** using **Python, LangChain, PyTest, and GitHub Actions**.

The goal of this project is to explore how **software testing practices can be adapted for AI systems**, particularly applications powered by **Large Language Models (LLMs)**.

Unlike traditional software, LLM outputs are **non-deterministic**, meaning the same prompt may produce different responses. Because of this, AI systems require **specialized evaluation strategies**.

This repository showcases how to implement **automated LLM evaluation pipelines**.

---

# AI Quiz Generator Application

This project implements an **AI-powered quiz generator**.

The system uses a prompt template and a small knowledge base to generate quiz questions based on a requested topic.

Example prompt:

```
Generate a quiz about science.
```

Example output:

```
Question 1: What did Leonardo Da Vinci paint?
Question 2: True or False: Water slows the speed of light.
Question 3: What is the largest telescope in space?
```

Supported quiz topics include:

* Science
* Geography
* Art
* Indonesian Food

---

# System Architecture

The application follows a simple LLM pipeline.

```
User Prompt
     ↓
Prompt Template (LangChain)
     ↓
OpenAI LLM
     ↓
Generated Quiz
     ↓
Evaluation Pipeline
     ↓
Automated Tests (PyTest)
     ↓
CI/CD Validation (GitHub Actions)
```

Every code change automatically triggers the evaluation pipeline.

---

## LLM Evaluation Pipeline

The project implements a simplified **LLM testing pipeline** commonly used in AI production systems.

```
                ┌──────────────┐
                │   User Input │
                └──────┬───────┘
                       │
                       ▼
             ┌───────────────────┐
             │ Prompt Template   │
             │ (LangChain)       │
             └────────┬──────────┘
                      │
                      ▼
              ┌───────────────┐
              │ OpenAI LLM    │
              │ Quiz Generator│
              └──────┬────────┘
                     │
                     ▼
             ┌────────────────┐
             │ Generated Quiz │
             └──────┬─────────┘
                    │
        ┌───────────┴────────────┐
        ▼                        ▼
 Rule-Based Tests        Model-Graded Evaluation
 (keyword validation)    (LLM-as-a-judge)
        │                        │
        └───────────┬────────────┘
                    ▼
             PyTest Test Suite
                    │
                    ▼
             GitHub Actions CI
```

This architecture allows automated validation of LLM outputs on every code change.


# LLM Evaluation Strategies

This project demonstrates **two common approaches used in LLMOps pipelines**.

---

## 1. Rule-Based Evaluation

Rule-based evaluation checks whether the LLM output contains expected keywords related to the topic.

Example test:

```
Generate a quiz about science
```

Expected keywords:

```
davinci
telescope
physics
curie
```

If the generated output does not include relevant topics, the test fails.

This technique is commonly used to detect:

* topic drift
* hallucinations
* incorrect context usage

---

## 2. Model-Graded Evaluation (LLM-as-a-Judge)

This project also implements **model-graded evaluation**.

In this approach, another LLM evaluates whether the generated response follows the expected format.

Example evaluation rule:

```
Question 1: #### <question>
Question 2: #### <question>
Question 3: #### <question>
```

Evaluation output:

```
Y → Valid quiz format
N → Invalid format
```

This approach is widely used in **LLMOps pipelines for evaluating generative AI outputs**.

---

# Automated Testing

The project uses **PyTest** to automate LLM evaluation.

Current test coverage includes:

* Science quiz generation
* Geography quiz generation
* Indonesian food quiz generation
* Refusal behavior for unsupported topics
* Model-graded evaluation

Run tests locally:

```
pytest -v
```

---

# CI/CD Pipeline

The repository includes a **GitHub Actions CI pipeline**.

Every push triggers:

```
1. Python environment setup
2. Dependency installation
3. LLM evaluation tests
```

This ensures that prompt changes or code modifications **do not break expected LLM behavior**.

---

# Project Structure

```
automated-testing-llmops
│
├── app.py
│   Main LLM quiz generator
│
├── eval_model.py
│   Model-graded evaluation logic
│
├── test_assistant.py
│   Rule-based automated tests
│
├── test_release_evals.py
│   Model-based evaluation tests
│
├── requirements.txt
│   Project dependencies
│
├── .github/workflows/tests.yml
│   GitHub Actions CI pipeline
│
└── README.md
```

---

# Running the Project Locally

Clone the repository:

```
git clone https://github.com/rezaparamarta/automated-testing-llmops.git
```

Install dependencies:

```
pip install -r requirements.txt
```

Create a `.env` file:

```
OPENAI_API_KEY=your_openai_api_key
```

Run tests:

```
pytest -v
```

---

# Example Knowledge Dataset

The quiz generator uses a simple knowledge base.

Example:

```
Subject: Leonardo Da Vinci
Facts:
- Painted the Mona Lisa
- Studied anatomy and optics
- Designed early flying machines
```

Example Indonesian food dataset:

```
Subject: Rendang
Facts:
- Traditional Indonesian dish from West Sumatra
- Made with beef and coconut milk
- Often considered one of the world's best foods
```

---

# Why This Project Matters

Testing AI systems is fundamentally different from traditional software testing.

Traditional testing:

```
Input → Deterministic Output
```

LLM systems:

```
Input → Probabilistic Output
```

This project demonstrates techniques used in **AI reliability engineering** and **LLMOps**.

Skills demonstrated in this project:

* Prompt engineering
* LLM application development
* Automated evaluation pipelines
* Model-graded evaluation
* CI/CD for AI systems

---

# Future Improvements

Potential improvements include:

* Semantic evaluation instead of keyword matching
* Dataset-driven testing
* LLM output scoring systems
* Prompt regression testing
* LLM observability

---

# Author

Reza Paramarta

QA Engineer interested in:

* AI Testing
* LLMOps
* Automation Testing
* AI Reliability

GitHub:
https://github.com/rezaparamarta
