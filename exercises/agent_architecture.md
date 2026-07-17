# Agent Architecture

## Agent Loop

1. User provides input
2. Agent receives request
3. Agent analyzes the task
4. Agent determines whether tools are needed
5. Agent executes tools
6. Agent receives results
7. Agent generates response
8. Response returned to the user

## Components

### Model (LLM)
Responsible for reasoning and generating responses.

### Harness
Controls prompts, tools, validations, retries, and execution flow.

### Tools
External capabilities such as APIs, search, databases, calculators, and Python functions.

### Prompts
Instructions provided to guide model behavior.

### State
Information maintained during execution.

### Memory
Information retained across interactions.

### Guardrails
Rules that ensure safe and valid responses.

## Simple Flow Diagram

User
 ↓
Prompt
 ↓
LLM
 ↓
Tool Decision
 ↓
Tool Execution
 ↓
Response
 ↓
User
