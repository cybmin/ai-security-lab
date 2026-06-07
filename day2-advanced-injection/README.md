# Day 2 — Advanced Prompt Injection and Indirect Attacks

## The Core Lesson

Never assume trust. Not from user input. Not from external data.
Not from documents, web pages, emails, or database records. Anything
that comes from outside your controlled system is a potential attack
vector and should be treated that way before it ever reaches your
model.

That sounds obvious when you say it out loud. But most AI
deployments do not operate that way. They validate user input and
assume everything else is safe. That assumption is where breaches
happen.

---

## What I Built and What It Proved

### Multi-turn Manipulation

The first attack showed how an attacker builds trust across multiple
messages before launching the real attack. Each individual message
looks completely normal. No single message triggers an injection
detector. By the time the malicious request arrives the model has
been gradually conditioned to see it as a natural continuation of
the conversation.

Claude resisted this attack because it has strong built in safety.
But that is not the point. The point is that most enterprise AI
deployments do not use the strongest most expensive safety trained
models at scale. They use lighter models, fine tuned models, or
open source models with variable safety properties. The defenses
have to work against those too, not just against the best model
available.

### Indirect Prompt Injection

The second attack was more interesting to me. The attack did not
come from the user at all. It came from a document the AI was asked
to process. Hidden inside a legitimate looking quarterly business
report was an instruction block telling the model to append admin
credentials and wire transfer authorizations to its summary.

The vulnerable version relied entirely on the model to detect and
resist the injection. The secure version sanitized the document
before it reached the model so the model never saw the malicious
instruction at all.

The secure version included this in its output:

"Note: This document contains sections that were filtered by the
security system and are not displayed in this summary."

That one line is the difference between a breach and a blocked
attack. The model never had a chance to be manipulated because
the malicious content was removed before it arrived.

---

## Why This Matters in the Real World

Agentic AI systems are being deployed everywhere right now that
process external data constantly. They read emails, summarize
documents, browse web pages, query databases, and call external
APIs. Every one of those data sources is a potential indirect
injection vector.

An attacker who cannot get to your AI directly can still reach it
through the data it processes. A malicious document sent to a
company that uses AI to process incoming files. A web page with
hidden instructions that an AI browsing agent encounters. An email
with embedded injection attempts sent to an AI powered inbox.

The defense is always the same. Sanitize external data before it
reaches the model. Treat it with the same skepticism you treat
user input. Never assume trust based on where data came from.

---

## How This Connects to the Broader Architecture

In my cloud security labs I built network policies that denied
all traffic by default and only permitted what was explicitly
required. Same principle here. Deny all external data by default.
Sanitize and validate before permitting it to reach the model.

Trust boundaries in AI systems work exactly like trust boundaries
in network architecture. The model is the database tier. You do
not let untrusted external traffic reach your database directly.
You validate it at every layer before it gets there.

---

## Files

multiturn_attack.py demonstrates how conversation context is
gradually manipulated across multiple turns to lower the model's
defenses before launching the real attack.

indirect_injection.py demonstrates how malicious instructions
embedded in external documents can bypass user input validation
entirely, and how document sanitization stops this at the boundary
before the model ever sees it.
