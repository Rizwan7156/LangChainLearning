# Hours 10-11 Summary

## Topic

Context Engineering and Memory Basics

---

## Concepts Covered

- Context Selection
- Conversation Summarization
- Short-Term Memory
- Long-Term Memory

---

## Technologies Demonstrated

✅ LLM

✅ Claude API

✅ LangChain

✅ LangGraph

✅ LangSmith

✅ Agent

✅ Tools

✅ Memory

✅ Browser UI

---

## Deliverable

Built a Memory Chatbot capable of:

- Storing user facts
- Storing user preferences
- Recalling stored memory
- Generating session summaries
- Using context-aware responses
- Executing memory tools through an Agent

---

## Components Implemented

### Memory Storage Tool

Stores:

- Name
- Role
- Favorite Color

Examples:

```text
My name is Rizwan
I am a Technical Lead
My favorite color is Blue
```

---

### Memory Recall Tool

Example:

```text
What do you know about me?
```

Returns:

```text
name: Rizwan
role: Technical Lead
favorite_color: Blue
```

---

### Summary Tool

Example:

```text
Show session summary
```

Uses Claude to summarize the conversation history.

---

### Short-Term Memory

Implemented using:

```python
chat_history
session_summary
```

Stores conversation during the browser session.

---

### Long-Term Memory

Implemented using:

```python
memory_store
```

Stores facts and preferences.

---

### Agent Routing

Routes requests to:

```text
memory_store
memory_recall
summary
chat
```

---

### Context Engineering

Claude receives:

```text
Context Memory
Session Summary
User Input
```

before generating responses.

---

## LangGraph Workflow

```text
User
 ↓
Agent
 ↓
Tool
 ↓
LLM
 ↓
Response
```

---

## Browser UI Features

- User Input
- Stored Memory Display
- Session Summary Display
- Chat History
- Claude Responses

---

## Testing Performed

### Test 1

```text
My name is Rizwan
```

✅ Stored Name

---

### Test 2

```text
I am a Technical Lead
```

✅ Stored Role

---

### Test 3

```text
My favorite color is Blue
```

✅ Stored Preference

---

### Test 4

```text
What do you know about me?
```

✅ Memory Recall

---

### Test 5

```text
Show session summary
```

✅ Conversation Summary

---

### Test 6

```text
Tell me about my profile
```

✅ Context-Aware Response

---

## Final Requirement Coverage

| Requirement | Status |
|------------|---------|
| Context Selection | ✅ |
| Conversation Summarization | ✅ |
| Short-Term Memory | ✅ |
| Long-Term Memory | ✅ |
| LLM | ✅ |
| Claude API | ✅ |
| LangChain | ✅ |
| LangGraph | ✅ |
| LangSmith | ✅ |
| Agent | ✅ |
| Tools | ✅ |
| Memory | ✅ |
| Browser UI | ✅ |

---

## Conclusion

Built a Memory-Aware Chatbot using Claude, LangChain, LangGraph, LangSmith, Agent Routing, Memory Tools, Short-Term Memory, Long-Term Memory, and Context Engineering.