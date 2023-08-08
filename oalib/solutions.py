"""Library with Cohere API solutions as functions

References:

For building code:  https://docs.cohere.com/docs/command-beta

"""

# here use 3.10 version, higher version has No module named '_lzma' problem
import cohere
import os


def submit_question(text):
    """This submits a question to the Cohere API"""

    COHERE_API_KEY = os.getenv("COHERE_API_KEY")
    co = cohere.Client(COHERE_API_KEY)

    result = co.generate(
        prompt = text,
        max_tokens = 40, 
        temperature = 0.75, 
        num_generations = 1, 
        stop_sequences=["."])
    
    answer = result.generations[0].text[1:]

    return answer