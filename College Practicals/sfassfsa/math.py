import streamlit as st
from langchain_classic.chains.llm import LLMChain
from langchain_classic.chains.llm_math.base import LLMMathChain
from langchain_core.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_classic.agents.agent_types import AgentType
from langchain_classic.agents import Tool,initialize_agent
from langchain_classic.callbacks import StreamlitCallbackHandler
from langchain_groq import ChatGroq

st.set_page_config(page_title="Math solver")
st.title("Ask Any Math Problem")

api = st.sidebar.text_input("Enter GROQ API key",type="password")

if not api:
    st.info("please enter an api key")
    st.stop()

llm = ChatGroq(model="llama-3.3-70b-versatile",api_key=api)


search = DuckDuckGoSearchRun(name="search")

math_chain = LLMMathChain.from_llm(llm=llm)
calculator = Tool(
    name="calculator",
    func=math_chain.run,
    description="ONLY use this tool for strict math expressions. DO NOT explain. DO NOT add text. ONLY return raw calculations."
)

prompt = """
you are an agent tasked to solve any asked mathematic question pointwise in a logical manner easy to understand, 
solve the question asked below:\n\n {question}
"""

prompt_template = PromptTemplate(
    input_variables=["question"],
    template=prompt
)

chain = LLMChain(llm=llm,prompt=prompt_template)

reasoning_tool = Tool(
    name="reasoning tool",
    func=chain.run,
    description="tool for answering logic based and reasoning question"
)

assistant_agent=initialize_agent(
    tools=[calculator,reasoning_tool,search],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role":"assistant","content":"Hi, I'm a math problem solver, ask anything!"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

question = st.text_area("enter your question")

if st.button("find the answer!"):
    try:
        if not question:
            st.info("enter a question please")
        elif question:
            with st.spinner("suffer while we find the answer"):
                st.session_state.messages.append({"role":"user","content":question})
                st.chat_message("user").write(question)
                st_cb = StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
                response = assistant_agent.run(st.session_state.messages,callbacks=[st_cb])

                st.session_state.messages.append({"role":"assistant","content":response})
                st.success(response)
    except Exception as e:
            st.error(f"Error: {e}")
            st.exception(e)  