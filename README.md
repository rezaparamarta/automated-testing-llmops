# Automated Testing for LLMOps

![CI](https://github.com/rezaparamarta/automated-testing-llmops/actions/workflows/tests.yml/badge.svg)

This project demonstrates how to build **automated testing pipelines for LLM-powered applications** using **Python, LangChain, PyTest, and GitHub Actions**.

The repository focuses on applying **software testing principles to AI systems**, particularly applications powered by **Large Language Models (LLMs)**.

Unlike traditional software systems, LLMs produce **probabilistic outputs**, which makes testing more complex. Because of this, AI systems require **specialized evaluation pipelines** rather than simple deterministic assertions.

This project implements **five layers of automated LLM evaluation** commonly used in modern **LLMOps and AI reliability engineering**.

---

# Project Overview

The sample application is an **AI-powered quiz generator** built using LangChain and OpenAI.

Example input:

```
Generate a quiz about science
```

Example output:

```
Question 1: What did Leonardo Da Vinci paint?
Question 2: True or False: Water slows the speed of light.
Question 3: What is the largest telescope in space?
```

Supported quiz categories include:

* Science
* Geography
* Art
* Indonesian Food

---

# System Architecture

The application follows a modular LLM workflow.

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

Every push to the repository automatically runs the **AI evaluation pipeline**.

---

# 5-Layer LLM Evaluation Framework

This project implements a **five-layer automated testing framework for LLM applications**.

These layers simulate the types of evaluation systems used in real-world AI platforms.

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
 Rule-Based Evaluation    Model-Graded Evaluation
        │                        │
        └───────────┬────────────┘
                    ▼
          Dataset-Driven Evaluation
                    │
                    ▼
          Hallucination Detection
                    │
                    ▼
             Quality Scoring
                    │
                    ▼
             PyTest Test Suite
                    │
                    ▼
            GitHub Actions CI/CD
```

---

# Layer 1 — Rule-Based Evaluation

This layer validates that the generated quiz contains **expected keywords related to the requested topic**.

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

This helps detect:

* topic drift
* prompt misalignment
* irrelevant responses

---

# Layer 2 — Model-Graded Evaluation

A second LLM evaluates whether the quiz output **follows the correct structure**.

Expected format:

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

This approach is commonly called:

**LLM-as-a-Judge**

---

# Layer 3 — Dataset-Driven Evaluation

The system evaluates LLM outputs using **multiple prompts from a dataset**.

Example dataset input:

```
"I'm trying to learn science, give me a quiz"
"I'm a geography expert, quiz me"
"Generate a quiz about Indonesian food"
```

This allows scalable automated evaluation across many prompts.

---

# Layer 4 — Hallucination Detection

LLMs sometimes generate **facts not present in the source dataset**.

This layer checks whether quiz questions only reference facts from the **quiz knowledge base**.

Example rule:

```
If a quiz contains facts not found in the quiz bank → FAIL
```

This prevents:

* fabricated information
* hallucinated facts
* unsafe educational content

---

# Layer 5 — Quality Scoring Evaluation

This layer evaluates the **overall quality of the generated quiz**.

The LLM grader assigns a score from **0 to 10** based on:

* format correctness
* topic relevance
* clarity of questions
* educational usefulness

Example output:

```
Score: 8
Explanation: The quiz follows the correct format and references valid facts from the dataset.
```

This mimics evaluation systems used in **real-world LLM platforms**.

---

# Automated Test Suite

The repository currently contains **9 automated LLM tests**.

Test coverage includes:

* science quiz generation
* geography quiz generation
* Indonesian food quiz generation
* refusal behavior
* model-graded evaluation
* dataset-driven testing
* hallucination detection
* AI quality scoring

Run tests locally:

```
pytest -v
```

Example output:

```
9 passed
```

---

# CI/CD Pipeline

The project uses **GitHub Actions** to run automated evaluations on every push.

Pipeline steps:

```
1. Setup Python environment
2. Install dependencies
3. Run PyTest LLM evaluation tests
```

This ensures that updates to prompts or code **do not degrade model output quality**.

---

# Project Structure

```
automated-testing-llmops
│
├── app.py
│   LLM quiz generator
│
├── eval_model.py
│   model-graded evaluation
│
├── hallucination_eval.py
│   hallucination detection
│
├── quality_eval.py
│   LLM quality scoring
│
├── test_assistant.py
│   rule-based tests
│
├── test_release_evals.py
│   model-graded tests
│
├── test_dataset_evals.py
│   dataset testing
│
├── test_hallucination_eval.py
│   hallucination tests
│
├── test_quality_eval.py
│   quality scoring tests
│
├── datasets
│   └── quiz_bank.txt
│
├── requirements.txt
│
└── .github/workflows/tests.yml
```

---

# Running the Project

Clone the repository:

```
git clone https://github.com/rezaparamarta/automated-testing-llmops.git
```

Install dependencies:

```
pip install -r requirements.txt
```

Create `.env` file:

```
OPENAI_API_KEY=your_api_key
```

Run tests:

```
pytest -v
```

---

# Skills Demonstrated

This project demonstrates several advanced AI testing techniques:

* LLM Application Testing
* Prompt Engineering Validation
* Automated LLM Evaluation Pipelines
* Model-Graded Evaluation (LLM-as-a-Judge)
* Dataset-Driven Testing
* Hallucination Detection
* AI Output Quality Scoring
* CI/CD for AI Systems

These techniques are commonly used in **LLMOps, AI reliability engineering, and AI testing frameworks**.

---

# Author

Reza Paramarta
QA Engineer | AI Testing | LLMOps

GitHub
https://github.com/rezaparamarta
