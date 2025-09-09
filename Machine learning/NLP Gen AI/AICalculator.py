import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMMathChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import  AgentType
from langchain.agents import Tool, initialize_agent
from langchain.callbacks import StreamlitCallbackHandler

st.set_page_config(page_title="Text to Math Problem Solver")
st.title("Text to Math problem Solver using Gemini")

# Gemini API KEY = AIzaSyCW11sbsVA1lgKCyPo9h7dZ28MsjlL3w4U

gemini_api_key = st.sidebar.text_input(label = "Google Gemini API key",type='password')

if not gemini_api_key:
    st.info("Please add your gemini API key to continue")
    st.stop()

llm = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash',
                             google_api_key = gemini_api_key,temperature=0)

wikipedia_wrapper = WikipediaAPIWrapper()
wikipedia_tool = Tool(
    name = "Wikipedia",
    func = wikipedia_wrapper.run,
    description = "A tool for searching the Internet to find information on various object"
)
# Math tool
math_chain = LLMMathChain.from_llm(llm = llm)
calculator = Tool(
    name = "Calculator",
    func = math_chain.run,
    description = "A tool for answering math related questions"
)

prompt = """
You are my personal agent tasked with solving users' mathematical questions.

Question: {question}
Answer:
"""
question = st.text_input("Enter your problem here")
prompt_template = PromptTemplate(input_variables=['question'],template=prompt)
chain = LLMChain(llm = llm, prompt = prompt_template)

reasoning_tool = Tool(
    name = "Reasoning Tool",
    func = chain.run,
    description = "A tool for answering logic-based and reasoning questions."
)

assistant_agent = initialize_agent(
                        tools = [wikipedia_tool,calculator,reasoning_tool],
                        llm = llm,
                        agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                        verbose = False,
                        handle_parsing_errors = True)

if "messages" not in st.session_state:
    st.session_state['messages'] = [
        {'role': "assistant", 'content': "Hi, I'm a math chatbot powered by Gemini"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])


if st.button("Find my answer"):
    if question:
        with st.spinner("Generating Response..."):
            st.session_state.messages.append({'role':'user','content':question})
            st.chat_message("user").write(question)

            st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts = False)

            response = assistant_agent.run(st.session_state.messages,callbacks=[st_cb])

            st.session_state.messages.append({'role':'assistant','content':response})

            st.write("Response")
            st.success(response)

    else:
        st.warning("Please enter your question")