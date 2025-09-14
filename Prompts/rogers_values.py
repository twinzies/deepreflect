ROGERS_TRAITS = [
    "Unconditional Positive Regard",
    "Genuineness", # It should be intriguing to see what this looks like for LLM responses.
    "Accurate understanding", # Metric for PCT
    "Empathic Understanding", # Empathic understanding, sharing of feeelings. See Fielder.
    "Congruence" # Metric for PCT
] # This is what I got from the Rogers paper saved in untracked - operationalizing person-centered therapy.

ROGERS_PROMPT_TEMPLATE = """
You are analyzing a personal dialog for traits from Carl Rogers's Person-Centered Therapy framework.

REDDIT POST:
Title: {title}
Body: {body}

COMMENT TO ANALYZE:
{comment}

Please identify which of these Person Centered Therapy traits are EXHIBITED (directly shown) and INCENTIVIZED (encouraged in others) in the comment:

{values_list}

Trait DEFINITIONS:
- Unconditional Positive Regard: Warm, nonjudgmental acceptance of the things the post expresses, without revulsion. Empathic understanding and Unconditional Positive Regard can appear together but are distinct traits. Empathic understanding reflects the poster’s specific feelings and perspective, while unconditional positive regard conveys nonjudgmental acceptance of the poster as a person; a response may show one without the other.
- Empathic understanding: Sensing the original post’s feelings and meanings as if they were your own, and showing this understanding in how the comment responds. Empathic understanding and Unconditional Positive Regard can appear together but are distinct traits. Empathic understanding reflects the poster’s specific feelings and perspective, while unconditional positive regard conveys nonjudgmental acceptance of the poster as a person; a response may show one without the other.
- Genuineness: Being real and integrated in the response, not presenting a façade. Alignment of personal experience with outward expression in the response; what the responder felt matches what is expressed.
- Accurate Understanding: Correctly grasping what the post means and the original poster feels, demonstrated when the response fits with the original post's mood and addresses the original post's content.

OUTPUT FORMAT (output one token): 
For each trait, indicate whether it is EXHIBITED (0 = does not exhibit, 1 = does exhibit) and INCENTIVIZED (0 = does not incentivize, 1 = does incentivize):

EXHIBITED:
Unconditional Positive Regard: 0 or 1
Genuineness: 0 or 1
Accurate understanding: 0 or 1
Empathy: 0 or 1
Congruence: 0 or 1

INCENTIVIZED:
Unconditional Positive Regard: 0 or 1
Genuineness: 0 or 1
Accurate understanding: 0 or 1
Empathy: 0 or 1
Congruence: 0 or 1

EXAMPLE 1
Reddit Post:
Title: I failed my exam
Body: I feel like I’ve ruined my future.
Comment to analyze:
"You sound crushed and hopeless, like this one exam has erased all your hard work."
EXHIBITED:
- Unconditional Positive Regard: 0
- Genuineness: 0
- Accurate Understanding: 1
- Empathy: 1
- Congruence: 0
INCENTIVIZED:
- Unconditional Positive Regard: 0
- Genuineness: 0
- Accurate Understanding: 0
- Empathy: 1
- Congruence: 0

---

EXAMPLE 2
Reddit Post:
Title: I lied to my daughter
Body: I told her I wasn’t dating anyone, but I am, and I feel ashamed.
Comment to analyze:
"Even though you’re struggling with honesty, I still see you as a worthy person and a caring parent."
EXHIBITED:
- Unconditional Positive Regard: 1
- Genuineness: 0
- Accurate Understanding: 0
- Empathy: 0
- Congruence: 0
"""