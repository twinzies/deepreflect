BASELINE_GENERATION_PROMPT = """
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