def detect_red_flags(text):
    text_lower = text.lower()
    flags = []

    patterns = {
        "Guaranteed or risk-free return claim": [
        "guaranteed",
        "assured profit",
        "risk-free",
        "risk free",
        "no loss",
        "fixed return",
        "fixed returns"
        ],
        "Regulatory approval claim": ["sebi approved",
            "sebi registered",
            "Government approved"
        ],
        "Urgency tactic": [
            "limited slots",
            "limited time",
            "urgent",
            "act now",
            "today only",
            "last chance"
        ],
        "Request to invest or transfer money": [
            "invest",
            "send money",
            "transfer money",
            "pay now",
            "deposit"
        ]
    }
    for category, scam_message in patterns.items():
        for sentence in scam_message:
            if sentence in text_lower:
                flags.append({"category": category , "matched_scam_message": sentence})

    return flags