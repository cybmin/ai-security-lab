# AI Security Engineering Lab

**Minhazul Abedin** | github.com/cybmin

---

## Why I Built This

Everyone is talking about AI right now. You hear about it everywhere.
Every company, every news headline, every job description. But most
people talking about it do not actually understand how it works, what
the risks are, or what happens when it goes wrong at scale.

We are entering something like a new industrial revolution. AI is
going to be embedded in critical systems, financial infrastructure,
healthcare, national security, and everyday life in ways that are
going to impact real people. That transition is creating attack
surfaces nobody fully understands yet. New vulnerabilities. New
threat models. New ways that a security failure can ripple through
society in ways we have not even imagined.

I spent the first part of my career learning how to secure
infrastructure. That foundation matters. But the security engineer
who only knows how to secure servers is going to be behind. This
lab is my attempt to get ahead of that curve.

---

## What I Learned Building This

The thing that surprised me most was that even the vulnerable chatbot
resisted basic prompt injection attacks. The model itself recognized
what I was trying to do and pushed back. I expected it to just leak
credentials immediately.

But that taught me something more important. The model's built in
safety is not a security architecture. It is one layer. If you
rely on it as your only defense you are building on a foundation
that changes every time someone switches providers, deploys a
different model, or fine tunes an open source alternative with
weaker safety properties. Real security assumes the model might
behave incorrectly and builds controls around it that work anyway.

Same principle I learned in the Kubernetes lab. You do not trust
the operating system to be your only defense. You add Gatekeeper,
network policies, and pod security controls on top. AI security
works the same way.

---

## The Model I Used and Why It Matters

For this lab I used Claude Haiku via the Anthropic Messages API.
Haiku is a fast lightweight model built for high throughput
applications like customer support chatbots that need to respond
quickly at scale.

But the specific model is actually less important than understanding
the architecture around it. The input validation, output filtering,
rate limiting, and system prompt hardening I built work the same
way whether the underlying model is Claude, GPT-4, Llama, or
anything else. That is intentional. The security architecture
should not depend on which model you are using or how safe that
model is by default. It should work regardless.

The distinction that matters most in enterprise AI security is
hosted versus self hosted. Hosted models from Anthropic and OpenAI
have strong built in safety training. Open source models deployed
on your own infrastructure have variable safety depending on how
they were fine tuned. Your security controls need to be stronger
for self hosted deployments because you cannot rely on anyone
else's safety work.

---

## AI Threat Modeling in Plain English

Threat modeling AI systems felt confusing to me at first because
the attack surface is not just infrastructure. The model itself
is an active participant that makes decisions. That is genuinely
different from securing a server.

The way it clicked for me was thinking in three layers.

The infrastructure layer is everything from my cloud security work.
Kubernetes clusters, S3 buckets, APIs, IAM roles. All of that
applies directly.

The application layer is the code around the model. Input
validation, output filtering, rate limiting, authentication.
Standard security plus AI specific controls.

The model behavior layer is the new one. The model itself as an
attack surface. How does it respond to adversarial inputs. What
can it be manipulated into doing. What does it know that it
should not reveal. This is where prompt injection and extraction
attacks live.

Most security engineers only know the first layer. Building
knowledge across all three is what this lab is about.

---

## What I Built

**vulnerable-chatbot.py** shows a customer support AI for a
fictional bank with secrets hardcoded into the system prompt
and no input or output controls. The attack surface is visible
and exploitable.

**secure_chatbot.py** wraps the same model with four independent
controls. Input validation catches injection patterns before they
reach the model. System prompt hardening removes all secrets so
there is nothing to steal. Output filtering scans every response
before it reaches the user. Rate limiting prevents denial of
service attacks from draining compute and cloud budget.

**threat-model.md** documents the assets, trust boundaries, and
attack surfaces for the system before a single line of code
was written.

---

## What Is Next

Day 9 covers prompt injection in depth. Real attacks that bypass
basic defenses. Multi-turn manipulation, indirect injection through
documents, and a proper input sanitization library.

Then agentic AI security, which is where it gets genuinely
interesting. An AI agent that can take real world actions has a
completely different threat model than a chatbot that only talks.
Least privilege for AI agents is one of the most important and
least understood concepts in security right now.

---

## Repository Structure
ai-security-lab/
├── vulnerable-chatbot.py     The threat model made visible
├── secure_chatbot.py         Four layer defense in depth
└── threat-model.md           AI system threat model document

---

*Everyone is talking about AI. Very few people are securing it.
That gap is where the most important security work of the next
decade is going to happen.*
