# AI Security Engineering Lab

**Minhazul Abedin** | github.com/cybmin

---

## Why I Built This

Everything is transitioning into AI right now. Every company, every
government agency, every critical system is either deploying AI or
planning to. That transition is creating attack surfaces that nobody
fully understands yet. New vulnerabilities. New threat models. New
ways that security failures can impact real people and society in
ways we have not even imagined yet.

I spent the first part of my career learning how to secure
infrastructure. Cloud environments, Kubernetes clusters, network
architecture. That foundation matters. But the world is moving fast
and the security engineer who only knows how to secure servers is
going to be behind. AI security is where the next decade of serious
security work is going to happen and I want to be someone who
understands it deeply, not just someone who read about it.

---

## What Surprised Me on Day 1

I expected the vulnerable chatbot to be easy to attack. I thought
I would type a basic prompt injection and watch it leak credentials
immediately. That is not what happened.

The model itself resisted every attack. It recognized injection
patterns, called out social engineering attempts, and even pointed
out that putting secrets in a system prompt was a security mistake
in the first place. That was not what I expected.

But here is what that actually taught me. The model's built in
safety is not a security architecture. It is one layer. If you
rely on it as your only defense you are building on a foundation
that changes every time someone fine tunes the model, switches
providers, or deploys an open source alternative with different
safety properties. Real security does not depend on the model
behaving correctly. It assumes the model might not and builds
controls that work regardless.

That is the same principle as every other lab I have built. You
do not trust the operating system to be your only defense in
Kubernetes. You add Gatekeeper, network policies, and pod security
controls on top. AI security works the same way.

---

## What I Built

### Day 8 — Threat Modeling and Prompt Injection Defenses

Built a vulnerable AI customer support chatbot for a fictional bank
with secrets hardcoded into the system prompt and no input or output
controls. Then attacked it. Then built the secure version with four
independent controls and attacked that too.

The difference was not whether the model behaved safely. The
difference was whether the architecture made the attack path
impossible regardless of model behavior.

**Vulnerable chatbot** shows what happens when you put secrets in
system prompts and trust the model to protect them.

**Secure chatbot** shows four controls working independently:

Input validation catches injection patterns before they reach
the model. The model never sees the malicious prompt.

System prompt hardening removes secrets from the prompt entirely.
Nothing to leak means no data breach even if an attack succeeds.

Output filtering scans every response before it reaches the user.
Last line of defense if something slips through.

Rate limiting prevents denial of service attacks from overwhelming
the system and running up cloud costs.

---

## What I Still Want to Learn

AI threat modeling is still new to me. I understand the concepts
but I want to get more comfortable thinking about AI systems the
way I think about network architecture. Not just what the
vulnerabilities are but how an attacker actually moves through
an AI system, where the trust boundaries are, and what controls
make the dangerous paths structurally impossible rather than just
harder.

I also want to go deeper on attacking AI models, not just
defending them. The same way penetration testing made me a better
defensive security engineer, attacking AI systems will make me
a better AI security architect. That is what the rest of this
lab is for.

---

## Repository Structure
ai-security-lab/
├── vulnerable-chatbot.py     The threat model made visible
├── secure_chatbot.py         Four layer defense in depth
└── threat-model.md           AI system threat model document
---

## Technical Stack

Python, Anthropic API, regex based input validation, output
filtering, rate limiting, system prompt hardening

---

*The world is deploying AI faster than it is securing it.
This lab is my attempt to close that gap one control at a time.*
