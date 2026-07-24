# Hour 1 Summary

## Topic

Setup and Environment

---

## Objective

Set up the development environment and successfully connect a Streamlit application with Claude using LangChain, LangGraph, LangSmith, Agent, and Tool concepts.

---

## Concepts Covered

- Environment Setup
- Claude API Integration
- LangChain Fundamentals
- LangGraph Workflow
- LangSmith Tracing
- Agent Basics
- Tool Integration
- Browser-Based User Interface

---

## Technologies Demonstrated

✅ LLM

✅ Claude API

✅ LangChain

✅ LangGraph

✅ LangSmith

✅ Agent

✅ Tool

✅ Browser UI

---

## Deliverable

Created a browser-based application that:

- Connects to Claude Haiku using Claude API
- Uses LangChain to communicate with the LLM
- Uses LangGraph to orchestrate workflow execution
- Demonstrates Agent → Tool → LLM execution flow
- Displays responses through Streamlit UI
- Supports LangSmith tracing

---

## Solution Implemented

A simple AI workflow was created using:

```text
Streamlit
     ↓
LangGraph
     ↓
Agent
     ↓
Tool
     ↓
LangChain
     ↓
Claude API
     ↓
Claude Haiku LLM
```

The application invokes a tool, passes its output to Claude, and displays the generated response in a browser interface.

---

## Architecture

```text
Browser
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

### Agent

The Agent decides which action should be executed.

Implemented through:

```python
agent_node()
```

Responsibilities:

- Executes tool
- Stores tool result
- Passes state to next node

---

### Tool

Implemented:

```python
hello_tool()
```

Output:

```text
Hello from Hour 1 Tool
```

Purpose:

- Demonstrate external capability usage
- Provide