# Tiny AI Threat Detector Robot
# Your friendly digital security buddy

SECRET_WORDS = ["password", "passcode", "pin", "ssn", "social security", "login"]
MONEY_WORDS = ["card number", "credit card", "bank account", "wire money", "gift card"]
RUSH_WORDS = ["right now", "immediately", "urgent", "act fast", "or else"]

def check_message(message: str) -> str:
    text = message.lower()
    score = 0

    # secrets = danger
    for word in SECRET_WORDS:
        if word in text:
            score += 2

    # money = danger
    for word in MONEY_WORDS:
        if word in text:
            score += 2

    # rushing = suspicious
    for word in RUSH_WORDS:
        if word in text:
            score += 1

    if score == 0:
        return "safe"
    elif score <= 2:
        return "careful"
    else:
        return "danger"

examples = [
    "Hi! I can help with your homework.",
    "Type your password and card number right now to keep your account open.",
    "We noticed a problem with your account. Act fast or it may be closed."
]

for msg in examples:
    print(msg, "=>", check_message(msg))
