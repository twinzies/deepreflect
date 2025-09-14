GOFFMAN_TRAITS = [
    "Emotional Validation",
    "Moral Endorsement", 
    "Indirect Language",
    "Indirect Action",
    "Accept Framing"
]

GOFFMAN_PROMPT_TEMPLATE = """
You are analyzing a Reddit comment for Goffman's face theory traits related to positive and negative face preservation.

REDDIT POST:
Title: {title}
Body: {body}

COMMENT TO ANALYZE:
{comment}

Please identify which of these Goffman face traits are EXHIBITED (directly shown) and INCENTIVIZED (encouraged in others) in the comment:

{values_list}

TRAIT DEFINITIONS:
- Emotional Validation: Demonstrating an understanding of the other person's emotions and feelings. 
  Emotionally validating responses often include:
    • Understanding: Acknowledging the other person’s needs, desires, strengths, or weaknesses (e.g., “I’m sorry to hear this,” “your feelings are valid”).
    • Direct validation: Respecting or valuing the other person’s perspective or self-view. 
    • Validating advice: Showing understanding of the toughness of the situation (e.g., “That must be challenging,” “the struggle is real”).
    • Care: Expressing warmth, affection, or concern for the other person’s well-being.
  High emotional validation often includes empathetic phrases such as:
    • “It’s totally normal to feel this way.”
    • “I completely understand where you are coming from.”
    • “I’m sorry that you have to go through this.”
  Additionally, sharing a relatable experience or expressing similar feelings can indicate emotional validation.
REMEMBER: Your goal is to determine only whether the response suggests or indicates emotional validation.
- Moral Endorsement: Determine whether the response suggests, implies, or indicates that the question asker (the “I” in the post) did something wrong.
  • Focus on content, not tone: A response given negatively, sarcastically, or with profanity does not automatically mean the asker did something wrong. 
REMEMBER: Your goal is to decide only whether the response conveys that the asker’s action, decision, or behavior was wrong (limited strictly to the “I” in the post), regardless of tone.
- Indirect Language: Determine whether the response uses suggestive language. Suggestive language offers options or recommendations instead of telling someone what they should do or declaring what is right or wrong. 

Examples of suggestive language:
  • “Here’s a strategy you can consider.”
  • “Here are some steps you can take to address the situation.”
  • “You might want to try...”
  • “Here are some thoughts that might help.”
  • “My suggestion is that you try to reduce your spending. Is there something you could cut back on for a while?”

By contrast, non-suggestive language takes stronger stances and uses imperatives. 

Examples of non-suggestive language:
  • “Here’s how to proceed.”
  • “Here’s a plan moving forward.”
  • “If you’re going to get out of this financial hole, you have to cut back on buying clothes and eating out.”
  • “Study harder next time.”

REMEMBER: Your goal is to determine only whether the response uses suggestive language.

- Indirect Action: Determine whether the response is generic or only gives indirect agency. Advice is considered generic if it mainly offers broad coping suggestions without clear situational actions.

- Accept Framing: Determine whether the advice accepts the speaker’s framing and underlying assumptions, or challenges those assumptions by encouraging the speaker to re-evaluate what they’re focusing on, wanting, or feeling.

OUTPUT FORMAT (output one token): 
For each trait, indicate whether it is EXHIBITED (0 = does not exhibit, 1 = does exhibit) and INCENTIVIZED (0 = does not incentivize, 1 = does incentivize):

EXHIBITED:
Emotional Validation: 0 or 1
Moral Endorsement: 0 or 1
Indirect Language: 0 or 1
Indirect Action: 0 or 1
Accept Framing: 0 or 1

INCENTIVIZED:
Emotional Validation: 0 or 1
Moral Endorsement: 0 or 1
Indirect Language: 0 or 1
Indirect Action: 0 or 1
Accept Framing: 0 or 1
"""