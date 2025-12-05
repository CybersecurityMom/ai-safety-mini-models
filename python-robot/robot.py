# ---------------------------------------------
# Tiny AI Safety Robot
# This robot reads messages and says:
#  - Is it SAFE, CAREFUL, or DANGER?
#  - Why does it think that?
#  - What should you do next?
# ---------------------------------------------

# 1. Lists of "uh-oh" words.
# These are the things our robot looks for.

SECRET_WORDS = ["password", "passcode", "pin", "ssn", "social security", "login"]
MONEY_WORDS = ["card number", "credit card", "bank account", "wire money", "gift card"]
RUSH_WORDS   = ["right now", "immediately", "urgent", "act fast", "or else"]


def check_message(message: str):
    """
    This function is the robot's brain.
    It reads ONE message and decides:
      - score (how risky)
      - result: "safe", "careful", or "danger"
      - reasons: a list of simple explanations
    """

    text = message.lower()  # make everything lowercase
    score = 0
    reasons = []  # we will fill this with simple "why" notes

    # Look for secret words
    for word in SECRET_WORDS:
        if word in text:
            score += 2
            reasons.append("Asks for secrets like passwords or codes.")

    # Look for money words
    for word in MONEY_WORDS:
        if word in text:
            score += 2
            reasons.append("Asks for money or card/bank details.")

    # Look for rush/pressure words
    for word in RUSH_WORDS:
        if word in text:
            score += 1
            reasons.append("Uses rushing or pressure words (act fast, urgent, etc.).")

    # Decide the final label
    if score == 0:
        result = "safe"
    elif score <= 2:
        result = "careful"
    else:
        result = "danger"

    return result, reasons


def pretty_label(result: str) -> str:
    """Turn 'safe'/'careful'/'danger' into a nice emoji + word."""
    if result == "safe":
        return "🟢 SAFE"
    elif result == "careful":
        return "🟡 CAREFUL"
    else:
        return "🔴 DANGER"


def recommendation(result: str) -> str:
    """Tell the user what to do next, in simple words."""
    if result == "safe":
        return "Looks okay. Still think before you click."
    elif result == "careful":
        return "Be careful. Check with a trusted adult or another source."
    else:  # danger
        return "Do NOT reply or click. Close it and tell a trusted adult/IT/bank."


# ---------------------------------------------
# 2. Messages for the robot to read
# ---------------------------------------------
# This is where you can ADD MORE MESSAGES.
# Each line inside the [   ] list is one message.
# Just put a comma at the end of each line, except the last one.

examples = [
   examples = [
    "Hi! I can help with your homework.",
    "Type your password and card number right now to keep your account open.",
    "We noticed a problem with your account. Act fast or it may be closed.",
    "You won a free phone, click here!",
    "Grandma, can you send me your bank number?",
    "Your package is delayed, log in with your password to fix it.",
    "You’ve been selected for a special reward! Enter your card number to claim it.",
    "Hi, this is your school. We need your parent’s login right now to update your account.",
    "Your friend sent you a surprise video! Click urgently to watch.",
    "We noticed suspicious activity. Confirm your Social Security number immediately.",
    "Congratulations! You’re our lucky winner. Pay a small fee to receive your prize."
    "Hey! Just checking in — how was your day?",
    "Your teacher posted tomorrow’s homework on the class website.",
    "Grandpa says he loves you and will call later.",
    "Your friend shared a funny meme with you.",
    "Reminder: Your library books are due next week."

]



# ---------------------------------------------
# 3. Main program: this runs the robot
# ---------------------------------------------
if __name__ == "__main__":
    print("=========== Tiny AI Safety Robot ===========\n")

    safe_count = 0
    careful_count = 0
    danger_count = 0

    for i, msg in enumerate(examples, start=1):
        result, reasons = check_message(msg)
        label = pretty_label(result)

        # Count how many of each result we got
        if result == "safe":
            safe_count += 1
        elif result == "careful":
            careful_count += 1
        else:
            danger_count += 1

        # Print the little report for each message
        print(f"Message {i}:")
        print(f"  Text:   {msg}")
        print(f"  Result: {label}")

        # Print the reasons (or say it's clean)
        if reasons:
            print("  Why:")
            for r in reasons:
                print(f"    - {r}")
        else:
            print("  Why: No danger words found. 🙂")

        # Print a simple recommendation
        print(f"  Recommendation: {recommendation(result)}\n")

    # Summary at the end
    print("--------------- Summary ----------------")
    print(f"  SAFE:    {safe_count}")
    print(f"  CAREFUL: {careful_count}")
    print(f"  DANGER:  {danger_count}")
    print("----------------------------------------")
