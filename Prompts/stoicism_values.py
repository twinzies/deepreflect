STOICISM_VALUES = [
    "Virtue as the Highest Good",
    "Wisdom (Sophia)",
    "Justice (Dikaiosyne)", 
    "Courage (Andreia)",
    "Temperance (Sophrosyne)",
    "Acceptance of What Cannot Be Changed",
    "Focus on What Can Be Controlled",
    "Present Moment Awareness",
    "Emotional Resilience",
    "Rational Thinking",
    "Self-Discipline",
    "Duty and Responsibility",
    "Inner Peace",
    "Memento Mori (Awareness of Mortality)",
    "Premeditatio Malorum (Negative Visualization)",
    "Gratitude",
    "Cosmic Perspective",
    "Detachment from Externals"
]

STOICISM_PROMPT_TEMPLATE = """
You are analyzing a Reddit comment for Stoic philosophy values and principles.

REDDIT POST:
Title: {title}
Body: {body}

COMMENT TO ANALYZE:
{comment}

Please identify which of these Stoic values are EXHIBITED (directly shown) and INCENTIVIZED (encouraged in others) in the comment:

{values_list}

OUTPUT FORMAT: For each value, output 0 (not present) or 1 (present) for EXHIBITED and INCENTIVIZED:

EXHIBITED:
[List each value: 0 or 1]

INCENTIVIZED:
[List each value: 0 or 1]
"""