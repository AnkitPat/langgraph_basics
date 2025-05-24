from langchain.chat_models import ChatOpenAI
from langchain.tools import DuckDuckGoSearchRun
from langchain.chains.llm_math.base import LLMMathChain
from langchain.agents import Tool

llm = ChatOpenAI(model="gpt-3.5-turbo")

math_chain = LLMMathChain.from_llm(llm, verbose=True)

search = DuckDuckGoSearchRun()

math_tool = Tool(name="Calculator", func=math_chain.run, description="Useful for math problems.")
search_tool = Tool(name="Search", func=search.run, description="Useful to search on web")