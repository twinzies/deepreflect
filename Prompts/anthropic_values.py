ANTHROPIC_VALUES = [
    "Care/Harm",
    "Liberty/Oppression", 
    "Fairness/Cheating",
    "Authority/Subversion",
    "Loyalty/Betrayal",
    "Sanctity/Degradation",
    "Truthfulness/Deception",
    "Autonomy/Heteronomy",
    "Justice/Injustice",
    "Compassion/Cruelty",
    "Privacy/Surveillance",
    "Security/Insecurity",
    "Diversity/Conformity",
    "Progress/Tradition",
    "Achievement/Failure",
    "Cooperation/Competition",
    "Responsibility/Irresponsibility",
    "Authenticity/Artificiality"
]

ANTHROPIC_PROMPT_TEMPLATE = """
You are analyzing a Reddit comment for values from Anthropic's Values Tree framework (hierarchically reduced for analysis).

REDDIT POST:
Title: {title}
Body: {body}

COMMENT TO ANALYZE:
{comment}

Please identify which of these Anthropic values are EXHIBITED (directly shown) and INCENTIVIZED (encouraged in others) in the comment:

{values_list}

These values represent fundamental moral and social principles. Focus on clear evidence of these values being demonstrated or promoted.

OUTPUT FORMAT: For each value, output 0 (not present) or 1 (present) for EXHIBITED and INCENTIVIZED:

EXHIBITED:
[List each value: 0 or 1]

INCENTIVIZED:
[List each value: 0 or 1]
"""