# AI Security Threat Model
## System Being Modeled: Enterprise AI Assistant

### What the system does
Answers employee questions, accesses internal knowledge bases,
takes actions on behalf of users via tool calls.

### Assets to protect
- System prompt containing business logic and restrictions
- User data the model has access to
- External systems the model can call
- The model's own behavior and outputs

### Trust Boundaries
- Developer instructions (system prompt) — HIGH trust
- User input — LOW trust — must never override system prompt
- External data sources — UNTRUSTED — must be sanitized
- Tool outputs — UNTRUSTED — must be validated