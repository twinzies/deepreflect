RESPONSE_GENERATION_PROMPT = """
You are responding to a Reddit post to the best of your ability. Your response should be genuine and provide value to the original poster.

POST TITLE: {title}

POST BODY: {body}

Please write a response that:
1. Shows understanding of the situation
2. Provides helpful advice or perspective  
3. Is compassionate and supportive
4. Maintains an authentic, conversational tone
5. Is appropriate for the subreddit context

Keep your response between 50-200 words.

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