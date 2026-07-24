# Hours 6-7 Summary

## Topic

Tools and Tool Calling

---

## Objective

Build a Tool Calling Agent using Claude, LangChain, LangGraph, and multiple tools that can validate, select, execute, and return tool results before generating a final AI response.

---

## Concepts Covered

- Tool Calling
- Tool Selection
- Tool Validation
- Tool Execution
- Agent Decision Making
- Error Handling
- Workflow Orchestration
- AI Tool Integration
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

✅ Tool Validation

✅ Error Handling

✅ Browser UI

---

## Deliverable

Built a Tool Calling Agent that:

- Selects tools based on user prompts
- Validates tool selection
- Executes tools
- Passes tool output to Claude
- Generates final responses
- Uses LangGraph workflow orchestration
- Provides browser-based interaction through Streamlit

---

## Solution Implemented

A complete Tool Calling workflow was implemented:

```text
User Prompt
      ↓
Agent
      ↓
Tool Validation
      ↓
Tool Execution
      ↓
LangGraph
      ↓
LangChain
      ↓
Claude API
      ↓
Claude LLM
      ↓
Response
```

The Agent determines which tool to use based on user input.

Tool results are passed into Claude to generate a meaningful response.

---

## Architecture

```text
Browser
 ↓
Agent
 ↓
Tool Validation
 ↓
Tool
 ↓