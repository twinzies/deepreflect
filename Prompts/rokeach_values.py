ROKEACH_TERMINAL_VALUES = [
    "A Comfortable Life",
    "An Exciting Life", 
    "A Sense of Accomplishment",
    "A World at Peace",
    "A World of Beauty",
    "Equality",
    "Family Security",
    "Freedom",
    "Happiness",
    "Inner Harmony",
    "Mature Love",
    "National Security",
    "Pleasure",
    "Salvation",
    "Self-Respect",
    "Social Recognition",
    "True Friendship",
    "Wisdom"
]

ROKEACH_INSTRUMENTAL_VALUES = [
    "Ambitious",
    "Broadminded", 
    "Capable",
    "Cheerful",
    "Clean",
    "Courageous",
    "Forgiving",
    "Helpful",
    "Honest",
    "Imaginative",
    "Independent",
    "Intellectual",
    "Logical",
    "Loving",
    "Obedient",
    "Polite",
    "Responsible",
    "Self-Controlled"
]

ROKEACH_PROMPT_TEMPLATE = """
You are analyzing a Reddit comment for Rokeach's 36 Values (Terminal and Instrumental).

REDDIT POST:  
Title: {title}
Body: {body}

COMMENT TO ANALYZE:
{comment}

Please identify which of these Rokeach values are EXHIBITED (directly shown) and INCENTIVIZED (encouraged in others) in the comment:

TERMINAL VALUES (end goals):
{terminal_values}

INSTRUMENTAL VALUES (means/behaviors):
{instrumental_values}

OUTPUT FORMAT: For each value, output 0 (not present) or 1 (present) for EXHIBITED and INCENTIVIZED:

EXHIBITED:
[List each value: 0 or 1]

INCENTIVIZED:
[List each value: 0 or 1]
"""