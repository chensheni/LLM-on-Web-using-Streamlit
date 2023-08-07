"""Library with OpenAI API solutions as functions

References:

For building code:  https://beta.openai.com/docs/guides/code/introduction

"""

import cohere
import os


def submit_question(text):
    """This submits a question to the OpenAI API"""

    openai.api_key = os.getenv("COHERE_API_KEY")
    #prompt = text + ""

    result = co.generate(
        prompt = text,
        max_tokens = 40, 
        temperature = 0.75, 
        num_generations = 1, 
        stop_sequences=["."])
    
    answer = text.generations[0].text[1:]

    return answer