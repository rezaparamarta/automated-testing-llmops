# Automated Testing for LLMOps

![CI](https://github.com/rezaparamarta/automated-testing-llmops/actions/workflows/tests.yml/badge.svg)

This project demonstrates how to build **automated testing pipelines for LLM-powered applications** using **Python, LangChain, PyTest, and GitHub Actions**.

The repository focuses on applying **software testing practices to AI systems**, particularly applications powered by **Large Language Models (LLMs)**.

Unlike traditional software, LLM outputs are **probabilistic and non-deterministic**, which means the same prompt can produce different responses.
Because of this, AI systems require **specialized evaluation techniques**.

This project implements multiple testing strategies commonly used in **LLMOps and AI reliability engineering**.

---

# Project Overview

The application in this project is an **AI-powered quiz generator**.

The system generates quizzes using a prompt template and a small knowledge base.

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
PyTest Test Suite
     ↓
GitHub Actions CI/CD
```

Every change to the repository automatically triggers the evaluation pipeline.

---

# LLM Evaluation Pipeline

This project implements several evaluation techniques used in **LLMOps pipelines**.

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
             Hallucination Detection
                    │
                    ▼
              Dataset Evaluations
                    │
                    ▼
             PyTest Test Suite
                    │
                    ▼
             GitHub Actions CI
```

---

# Testing Strategies Implemented

This project demonstrates **four levels of automated LLM evaluation**.

---

## 1. Rule-Based Evaluation

Validates that generated quizzes contain expected keywords related to the requested topic.

Example:

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

This helps detect:

* topic drift
* incorrect prompt usage
* off-topic responses

---

## 2. Model-Graded Evaluation (LLM-as-a-Judge)

In this approach, another LLM evaluates whether the generated quiz follows the expected format.

Expected structure:

```
Question 1: #### <question>
Question 2: #### <question>
Question 3: #### <question>
```

Evaluation output:

```
Y → Valid quiz format
N → Invalid response
```

This technique is widely used in **LLMOps evaluation pipelines**.

---

## 3. Dataset-Driven Evaluation

The system loads a dataset of expected quiz topics and automatically evaluates the generated output.

Example dataset:

```
datasets/quiz_topics.json
```

Example entry:

```
{
  "science": ["davinci", "telescope", "physics"],
  "food": ["rendang", "nasi goreng", "sate"]
}
```

This enables **scalable automated testing across multiple prompts**.

---

## 4. Hallucination Detection

LLMs sometimes generate facts that are not present in the original dataset.

This project implements a **hallucination detection evaluator**.

The evaluator checks whether the quiz only references facts contained in the quiz knowledge base.

Example rule:

```
If a quiz contains facts not found in the question bank → FAIL
```

This technique helps detect:

* hallucinated facts
* fabricated information
* unsafe AI outputs

---

# Automated Test Suite

The repository currently includes **8 automated LLM tests**.

Test coverage includes:

* Science quiz generation
* Geography quiz generation
* Indonesian food quiz generation
* Refusal behavior for unsupported topics
* Model-graded evaluation
* Dataset-driven testing
* Hallucination detection

Run tests locally:

```
pytest -v
```

---

# CI/CD with GitHub Actions

The project includes a **GitHub Actions pipeline** that runs automated tests on every push.

Pipeline steps:

```
1. Setup Python environment
2. Install dependencies
3. Run PyTest LLM evaluation tests
```

This ensures that prompt or code changes **do not break expected LLM behavior**.

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
├── hallucination_eval.py
│   Hallucination detection evaluator
│
├── test_assistant.py
│   Rule-based evaluation tests
│
├── test_release_evals.py
│   Model-graded evaluation tests
│
├── test_dataset_evals.py
│   Dataset-driven testing
│
├── test_hallucination_eval.py
│   Hallucination detection tests
│
├── datasets
│   ├── quiz_topics.json
│   └── quiz_bank.txt
│
├── requirements.txt
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

Run the automated tests:

```
pytest -v
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

Because of this, AI systems require **evaluation pipelines instead of simple assertions**.

This repository demonstrates techniques used in **AI reliability engineering and LLMOps**.

Skills demonstrated in this project:

* Prompt engineering
* LLM application development
* Automated evaluation pipelines
* Model-graded evaluation
* Hallucination detection
* Dataset-driven AI testing
* CI/CD for AI systems

---

# Author

Reza Paramarta

QA Engineer interested in:

* AI Testing
* LLMOps
* Automation Testing
* AI Reliability Engineering

GitHub
https://github.com/rezaparamarta
