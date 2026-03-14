<<<<<<< HEAD
![Tests](https://github.com/rezaparamarta/automated-testing-llmops/actions/workflows/tests.yml/badge.svg)

=======
>>>>>>> 32c763fb8f1c19edd26990480da744566822c302
# Automated Testing for LLMOps – AI Quiz Generator

This project demonstrates how to build **automated evaluation pipelines for LLM-powered applications** using Python, LangChain, and Pytest.
The goal is to ensure that an LLM-based application behaves consistently through **automated regression testing**.

The application generates quizzes from a predefined knowledge base and verifies the output using automated tests.

---

## Overview

Large Language Models (LLMs) produce **non-deterministic outputs**, making traditional software testing approaches insufficient.
This project demonstrates how to validate LLM behavior using **keyword-based automated evaluations** and integrate them into a **CI/CD workflow**.

The system consists of:

* Prompt engineering
* LLM inference
* Output parsing
* Automated evaluation tests
* CI/CD integration

---

## Project Architecture

User Question
↓
Prompt Template
↓
LLM (OpenAI via LangChain)
↓
Output Parser
↓
Automated Evaluation (Pytest)

The system ensures that generated outputs contain expected knowledge from the dataset.

---

## Features

* AI-powered quiz generator
* Prompt-based LLM pipeline using LangChain
* Automated evaluation with Pytest
* Regression testing for prompt changes
* Ready for CI/CD integration

---

## Tech Stack

* Python
* LangChain
* OpenAI API
* Pytest
* Python Dotenv

---

## Project Structure

```
Automated-Testing-for-LLMOps
│
├── app.py
├── test_assistant.py
├── requirements.txt
├── .env.example
└── README.md
```

### app.py

Defines the LLM pipeline including:

* Prompt template
* OpenAI model configuration
* Output parser
* Assistant chain

### test_assistant.py

Contains automated evaluation tests for the LLM application.

---

## Dataset

The quiz generator uses a small internal knowledge base:

Subjects include:

* Leonardo DaVinci
* Paris
* Telescopes
* Starry Night
* Physics

Each subject contains factual information used to generate quiz questions.

---

## Automated Evaluations

The evaluation strategy uses **keyword assertions** to validate LLM responses.

Example:

```python
assert any(word in answer.lower() for word in expected_words)
```

This approach works because LLM outputs are **probabilistic** and cannot always be matched exactly.

---

## Example Test Cases

### Science Quiz

Input:

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

---

### Geography Quiz

Input:

```
Generate a quiz about geography
```

Expected keywords:

```
paris
france
louvre
```

---

### Refusal Test

Input:

```
Generate a quiz about Rome
```

Expected output:

```
I'm sorry I do not have information about that
```

---

## Running the Project

### 1. Clone the repository

```
git clone https://github.com/yourusername/automated-testing-llmops.git
cd automated-testing-llmops
```

### 2. Create virtual environment

```
python -m venv venv
```

Activate:

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Configure API key

Create `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

### 5. Run automated evaluations

```
pytest -s -v
```

Example output:

```
test_science_quiz PASSED
test_geography_quiz PASSED
test_refusal PASSED
```

---

## CI/CD Integration

This project can be integrated with CI/CD pipelines to automatically evaluate LLM behavior after each commit.

Typical workflow:

```
Git Push
↓
CI Pipeline
↓
Run Pytest
↓
Validate LLM Outputs
↓
Block deployment if tests fail
```

This prevents prompt changes from breaking application behavior.

---

## Why Automated LLM Evaluations Matter

Traditional software testing relies on deterministic outputs.

LLM-based systems require **behavioral testing strategies** such as:

* keyword validation
* semantic similarity checks
* LLM-as-a-judge evaluation

This project demonstrates the **simplest form of automated LLM regression testing**.

---

## Future Improvements

Possible enhancements:

* semantic similarity evaluation
* LLM-as-a-judge evaluation
* LangSmith tracing
* RAG-based knowledge sources
* automated evaluation dashboards

---

## Author

Reza Paramarta
Software Test Engineer

Interested in:

* AI Testing
* LLM Evaluation
* NLP Systems
* LLMOps

---
