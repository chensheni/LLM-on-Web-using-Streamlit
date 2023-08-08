import streamlit as st
import cohere

# Get the Cohere API Key
api_key = st.sidebar.text_input("OpenAI API Key:", type="password")
st.sidebar.markdown("This QA bot is built on top of Cohere LLM. A brief introduction can be found at: https://docs.cohere.com/docs/the-cohere-platform.")
st.sidebar.markdown("For question to be answered, an API key is required. To get a API key, sign up at: https://dashboard.cohere.ai/welcome/register.")


# Setting up the Title
st.title("🕹️ AI Question Answering Bot")

st.write(
    "_**Smart LLM will answer all your simple questions, but please don't trap him :)**_"
)

QUESTION = st.text_input("Input Question 👇")


@st.cache
def submit_question(question):
    """This submits a question to the Cohere API"""

    co = cohere.Client(api_key)

    result = co.generate(
        prompt = question,
        max_tokens = 100, 
        temperature = 0.80, 
        num_generations = 1, 
        stop_sequences=["."])
    
    answer = result.generations[0].text[1:]

    return answer


if st.button("Submit"):
    st.write("**Output**")
    st.write("""---""")
    with st.spinner(text="In progress"):
        report_text = submit_question(QUESTION)
        st.markdown(report_text)
