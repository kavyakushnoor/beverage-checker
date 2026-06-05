import json
from rapidfuzz import fuzz

with open("configs/beverage_rules.json", "r") as f:
    RULES = json.load(f)

def fuzzy_contains(text, target, threshold=80):
    score = fuzz.partial_ratio(text.lower(), target.lower())
    return score >= threshold

def evaluate_rules(text):
    if not text:
        return {"status": "FAIL", "issues": ["No text detected"]}

    issues = []

    for word in RULES["required_words"]:
        if not fuzzy_contains(text, word):
            issues.append(f"Missing: {word}")

    for phrase in RULES["must_contain"]:
        if not fuzzy_contains(text, phrase, 75):
            issues.append(f"Missing phrase: {phrase[:35]}...")

    if len(issues) == 0:
        status = "PASS"
    elif len(issues) <= 2:
        status = "WARNING"
    else:
        status = "FAIL"

    return {"status": status, "issues": issues}
