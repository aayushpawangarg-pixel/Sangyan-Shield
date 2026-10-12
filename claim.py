def extract_claims(text):
    claims = []
    text_lower = text.lower()

    claim_patterns = {
        "Guaranteed return": [
            "guaranteed",
            "assured profit",
            "risk-free",
            "risk free",
            "no loss"
        ],
        "Regulatory approval": [
            "sebi approved",
            "sebi registered",
            "government approved"
        ],
        "Urgency": [
            "limited slots",
            "limited time",
            "act now",
            "today only",
            "last chance"
        ]
    }

    for category, phrases in claim_patterns.items():
        for phrase in phrases:
            if phrase in text_lower:
                claims.append({
                    "category": category,
                    "matched_phrase": phrase,
                    "status": "not_verified"
                })

    return claims


if __name__ == "__main__":
    sample_text = """
    Guaranteed 30% monthly returns.
    SEBI approved.
    Limited slots available.
    """

    results = extract_claims(sample_text)

    for claim in results:
        print(claim)