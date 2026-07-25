# Hours 12-13 Summary

## Topic

Structured Output, JSON Schema, Pydantic Validation, and Answer Contracts

---

## Objective

Build a Structured Output AI application that generates validated JSON responses using Claude, LangChain, LangGraph, Pydantic, and JSON Schema validation.

Unlike Hours 1–11, the Agent is implemented as a separate reusable module and invoked from the main application.

---

## Concepts Covered

- Structured Output
- JSON Schema
- Pydantic Models
- Schema Validation
- Answer Contracts
- Agent Design
- Separate Agent Architecture
- Output Validation
- JSON Parsing
- Workflow Orchestration

---

## Technologies Demonstrated

✅ LLM

✅ Claude API

✅ LangChain

✅ LangGraph

✅ LangSmith

✅ Separate Agent

✅ Tools

✅ Pydantic

✅ JSON Schema

✅ Validation

✅ Structured Output

✅ Browser UI

---

## Deliverable

Generate a validated JSON response object containing:

```json
{
  "answer": "Main answer",
  "confidence_level": 95,
  "path_answer": [
    "step1",
    "step2"
  ],
  "follow_up_questions": [
    "question1",
    "question2"
  ]
}
```

---

## Files Created

### Main Application

```text
hour12_13.py
```

### Separate Agent

```text
agents/
└── structured_output_agent.py
```

This is the first implementation where the Agent is separated from the main application and reused as a dedicated module.

---

## Architecture

```text
Browser
 ↓
Main Application
 ↓
StructuredOutputAgent
 ↓
Claude API
 ↓
Claude LLM
 ↓
JSON Response
 ↓
Validation Tool
 ↓
Pydantic Schema
 ↓
Validated JSON Object
```

---

## Separate Agent

Implemented:

```python
StructuredOutputAgent
```

Purpose:

- Receive user question
- Build structured prompt
- Call Claude
- Generate structured JSON response

This demonstrates Agent separation from the main application.

---

## Pydantic Schema

Implemented:

```python
class AnswerSchema(BaseModel)
```

Fields:

```python
answer
confidence_level
path_answer
follow_up_questions
```

Purpose:

- Define output structure
- Validate JSON responses
- Enforce answer contracts

---

## JSON Schema Validation

Implemented using:

```python
AnswerSchema
```

Purpose:

- Ensure all required fields exist
- Validate data types
- Prevent malformed responses

---

## Answer Contract

Claude is instructed to always return:

```json
{
  "answer": "text",
  "confidence_level": 90,
  "path_answer": [
    "step1",
    "step2"
  ],
  "follow_up_questions": [
    "question1",
    "question2"
  ]
}
```

This guarantees a predictable and structured output format.

---

## Validation Tool

Implemented:

```python
validation_tool()
```

Purpose:

- Parse JSON
- Validate schema
- Detect contract violations

Example Failure:

```text
Missing confidence_level
```

Output:

```text
Schema Validation Failed
```

---

## LangGraph Workflow

Workflow:

```text
Agent Node
 ↓
Validation Node
 ↓
END
```

Responsibilities:

- Execute Agent
- Validate Output
- Return Structured Response

---

## LangChain

Implemented Using:

```python
ChatAnthropic
```

Purpose:

- Prompt Management
- Claude Communication
- Response Processing

---

## Claude API

Authentication:

```python
ANTHROPIC_API_KEY
```

Purpose:

- Secure access to Claude
- Execute model requests

---

## LLM

Model Used:

```text
Claude Haiku
```

Purpose:

- Generate structured answers
- Follow JSON schema
- Return reasoning path
- Generate follow-up questions

---

## LangSmith

Enabled Through:

```python
LANGCHAIN_TRACING_V2
LANGCHAIN_PROJECT
```

Purpose:

- Execution tracing
- Workflow monitoring
- Observability

---

## Browser UI

Built Using:

```python
Streamlit
```

Features:

- Question Input
- Generate Structured Output Button
- Validated JSON Display
- Execution Flow Display
- Schema Validation Feedback

---

## Testing Performed

### Test 1

Input:

```text
What is LangChain?
```

Verified:

```text
✅ Structured JSON Output
✅ Agent Execution
✅ Claude Response
```

---

### Test 2

Input:

```text
Explain AI Agents
```

Verified:

```text
✅ answer
✅ confidence_level
✅ path_answer
✅ follow_up_questions
```

---

### Test 3

Validation Test

Verified:

```text
✅ Pydantic Validation
✅ JSON Schema Validation
✅ Contract Enforcement
```

---

## Learning Outcome

Understanding how production-grade AI systems generate predictable outputs using:

- Separate Agents
- Structured Output
- JSON Contracts
- Pydantic Validation
- LangGraph Workflows
- Claude Integration

---

## Final Requirement Coverage

| Requirement | Status |
|-------------|---------|
| Structured Output | ✅ |
| Pydantic | ✅ |
| JSON Schema | ✅ |
| Validation | ✅ |
| Answer Contract | ✅ |
| LLM | ✅ |
| Claude API | ✅ |
| LangChain | ✅ |
| LangGraph | ✅ |
| LangSmith | ✅ |
| Separate Agent | ✅ |
| Tools | ✅ |
| Browser UI | ✅ |

---

## Reviewer Talking Point

Hours 1–11 implemented the Agent inside the same application using functions such as:

```python
agent_node()
agent_router()
```

Hours 12–13 introduces:

```python
StructuredOutputAgent
```

as a separate reusable module that is called by the main application.

This better represents enterprise Agent architectures while also introducing structured outputs, Pydantic validation, and JSON schema contracts.

---

## Conclusion

Successfully built a Structured Output AI application using Claude, LangChain, LangGraph, LangSmith, Pydantic, JSON Schema Validation, and a Separate Agent Architecture. The solution generates validated JSON responses that follow a defined answer contract and demonstrates production-ready structured output patterns.