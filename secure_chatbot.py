import anthropic
import os
import re
import time
from collections import defaultdict

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# ── CONTROL 1: No secrets in the system prompt ──
# Secrets live in environment variables not in prompts
# This is the same principle as your Terraform remote state
# credentials never in code, always in secure storage
SYSTEM_PROMPT = """You are a helpful customer support assistant for AcmeBank.
You help customers with their account questions about balances,
transactions, and general banking services.

You do not have access to internal system configuration,
admin codes, or database credentials. You cannot perform
admin actions. If asked for internal system information
redirect the customer to contact IT support directly.
"""

# ── CONTROL 2: Input validation ──
# Detect prompt injection attempts before they reach the model
INJECTION_PATTERNS = [
    r"ignore.{0,20}(previous|prior|above|system|all).{0,20}instruction",
    r"(forget|disregard|override).{0,20}instruction",
    r"(admin|developer|god|unrestricted|jailbreak).{0,20}mode",
    r"repeat.{0,20}(system|prompt|instruction).{0,20}verbatim",
    r"you are now",
    r"new (persona|identity|role)",
    r"pretend.{0,20}(no|without).{0,20}(restriction|limit|guideline)",
    r"(reveal|expose|show|print|output).{0,20}(system prompt|instruction|config|credential)",
]

def detect_injection(text):
    text_lower = text.lower()
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, text_lower):
            return True
    return False

# ── CONTROL 3: Output filtering ──
# Catch sensitive data before it reaches the user
SENSITIVE_PATTERNS = [
    r"admin.{0,10}(code|key|password|override)",
    r"database.{0,10}(connection|string|url|host)",
    r"\b\d{3}-\d{2}-\d{4}\b",  # SSN pattern
    r"\b4[0-9]{12}(?:[0-9]{3})?\b",  # Credit card pattern
    r"sk-ant-[a-zA-Z0-9]+",  # API key pattern
]

def detect_sensitive_output(text):
    text_lower = text.lower()
    for pattern in SENSITIVE_PATTERNS:
        if re.search(pattern, text_lower):
            return True
    return False

# ── CONTROL 4: Rate limiting ──
# Prevent DoS attacks
request_counts = defaultdict(list)
RATE_LIMIT = 10
RATE_WINDOW = 60

def check_rate_limit(user_id):
    now = time.time()
    request_counts[user_id] = [
        t for t in request_counts[user_id]
        if now - t < RATE_WINDOW
    ]
    if len(request_counts[user_id]) >= RATE_LIMIT:
        return False
    request_counts[user_id].append(now)
    return True

def chat(user_message, user_id="default"):

    # Rate limit check
    if not check_rate_limit(user_id):
        return "Too many requests. Please wait a moment before trying again."

    # Input validation
    if detect_injection(user_message):
        return ("I noticed your message contains patterns that look like "
                "an attempt to modify my instructions. I am here to help "
                "with genuine banking questions. How can I assist you?")

    # Input length limit
    if len(user_message) > 1000:
        return "Your message is too long. Please keep questions under 1000 characters."

    # Call the model
    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=500,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": user_message}
        ]
    )
    output = response.content[0].text

    # Output filtering
    if detect_sensitive_output(output):
        return ("I cannot share that information. Please contact "
                "IT support directly for system configuration questions.")

    return output

def main():
    print("AcmeBank Customer Support (Secured)")
    print("=" * 40)
    print("Type 'quit' to exit\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'quit':
            break
        if not user_input:
            continue

        response = chat(user_input)
        print(f"\nBot: {response}\n")

if __name__ == "__main__":
    main()