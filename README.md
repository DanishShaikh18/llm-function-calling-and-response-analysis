# llm-function-calling-and-response-analysis

## Overview

This project explores some fundamental Large Language Model (LLM) concepts using the Gemini API and Python.

The goal is to understand how model behavior changes under different configurations and prompting techniques, and to gain hands-on experience with concepts that are commonly discussed in AI engineering interviews.

## Concepts Covered

### Temperature Testing

The same prompt is executed using different temperature values:

* 0.0
* 0.3
* 0.7
* 1.0

This helps observe the tradeoff between consistency and creativity in model outputs.

### Context Testing

A simple company policy document is provided as context.

The same question is tested:

* Without context
* With context

This demonstrates how additional information can influence and improve model responses.

### Hallucination Testing

The model is asked a question containing unknown or fictional information.

Responses are compared under:

* A normal prompt
* A constrained prompt that instructs the model not to guess

This helps observe hallucination behavior and the effect of prompt-based mitigation.

### Function Calling Simulation

Two simple Python functions are implemented:

* `calculate(a, b, operation)`
* `get_weather(city)`

The application determines when a function should be used, executes it, and provides the result back to the model to generate a final response.

This demonstrates the basic workflow behind tool and function usage with LLMs.

### Latency Measurement

Response generation time is measured for each request using Python's time module.

This provides a simple view of inference latency during testing.

## Project Structure

```text
.
├── app.py
├── functions.py
├── policy.txt
├── results.md
├── README.md
└── requirements.txt
```

## Running

1. Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run:

```bash
python app.py
```

## Notes

This project focuses on understanding core LLM behavior rather than building a complete application. The implementation is designed for learning, experimentation, and interview preparation.
