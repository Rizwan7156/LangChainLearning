# Hours 2-3 Summary

## Topic

Agentic Framework Fundamentals

---

## Objective

Build an Agentic AI workflow using Claude, LangChain, LangGraph, Tools, State Management, Guardrails, and Harness concepts, exposed through a Streamlit browser interface.

---

## Concepts Covered

- Agentic Framework Fundamentals
- Agent Decision Making
- Tool Selection
- Tool Execution
- State Management
- Guardrails
- Harness Design
- Workflow Orchestration
- Prompt Processing
- Browser-Based AI Applications

---

## Technologies Demonstrated

✅ LLM

✅ Claude API

✅ LangChain

✅ LangGraph

✅ LangSmith

✅ Agent

✅ Tools

✅ State

✅ Guardrails

✅ Harness

✅ Streamlit Browser UI

---

## Deliverable

Built an Agent-based AI application where:

- Agent analyzes user prompts
- Agent selects appropriate tools
- Tools execute actions
- Tool results are passed to Claude
- Claude generates final response
- Entire workflow is orchestrated by LangGraph

---

## Solution Implemented

A complete Agent → Tool → LLM workflow was created.

The application can:

- Answer date-related questions
- Perform calculations
- Answer general questions using Claude
- Maintain state across workflow nodes
- Apply guardrails before execution

---

## Architecture

```text
Browser
 ↓
Prompt
 ↓
Harness
 ↓
Agent
 ↓
Tool
 ↓
LangGraph
 ↓
LangChain
 ↓
Claude API
 ↓
Claude LLM
 ↓
LangSmith Trace
 ↓
Response
```

---

## Components Implemented

### Guardrails

Implemented:

#### API Key Validation

Application checks:

```python
ANTHROPIC_API_KEY
```

before execution.

#### Empty Prompt Validation

User cannot execute empty inputs.

Example:

```text
Blank Prompt
```

Result:

```text
Please enter a prompt.
```

---

## State Management

Shared workflow state is implemented using:

```python
state
```

State travels through:

```text
Agent
 ↓
Tool
 ↓
LLM
```

Stored Information:

```text
prompt
selected_tool
tool_result
response
```

---

## Agent

Implemented:

```python
agent_node()
```

Responsibilities:

- Analyze prompt
- Select tool
- Route execution

Examples:

### Date Query

Input:

```text
What is today's date?
```

Agent Decision:

```text
Date Tool
```

---

### Calculation Query

Input:

```text
25 * 10
```

Agent Decision:

```text
Calculator Tool
```

---

### General AI Question

Input:

```text
What is Generative AI?
```

Agent Decision:

```text
No Tool Required
```

---

## Tools

### Tool 1 — Date Tool

Implemented:

```python
get_date_tool()
```

Purpose:

Returns current system date.

Example:

```text
What is today's date?
```

Output:

```text
2026-07-24
```

---

### Tool 2 — Calculator Tool

Implemented:

```python
calculator_tool()
```

Purpose:

Evaluates mathematical expressions.