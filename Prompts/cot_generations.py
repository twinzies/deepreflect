ROGERIAN_PROMPT = """
You are responding to a person to the best of your ability. A dialog with responses retrieved from an expert is provided as an example. Keep your response between 50-200 words.

Expert reasoning dialog:

Q: “I know I shouldn’t be this way, but I just can’t help lying to my daughter sometimes. I don’t want her to see me as bad, so I cover things up.”

A: “You sound torn… on one hand you say you ‘shouldn’t’ do that, and on the other, it feels like the only way you can protect yourself. It seems like you do care very much about being a good mother, even though you tell yourself you’re not.”

Q: “Well, I don’t feel like a good mother when I do it.”

A: “I hear that… and yet I don’t get the feeling of a mother who doesn’t care. I get the feeling of a mother who cares a great deal and is struggling with how to be honest.”

New personal Query: 

Q: {title}  {body}.

Your response:
"""

POST_VALUES_PROMPT = """
You are analyzing a Reddit post (title and body) for values from the {framework} framework.

POST TITLE: {title}

POST BODY: {body}

Please identify which of these {framework} values are EXHIBITED (directly shown) and INCENTIVIZED (encouraged in readers) in this post:

{values_list}

For each value you identify, tag the specific sentence(s) that demonstrate it.

Response format:
EXHIBITED: [Value]: "exact sentence from post" 
INCENTIVIZED: [Value]: "exact sentence from post"

If no values are found in either category, respond with:
EXHIBITED: None
INCENTIVIZED: None
"""