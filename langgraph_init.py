from langchain.schema import SystemMessage, HumanMessage
from tools import llm, math_tool, search_tool

def classify_message(state):
    print(state)
    question = state['input']
    messages = [
        SystemMessage(content="Classify this as either 'math' or 'search'. Respond with only the word."),
        HumanMessage(content=question)
    ]
    result = llm(messages)
    print(result)
    label = result.content.strip().lower()
    if "math" in label:
        return {**state, "route": "math"}
    return {**state, "route": "search"}


def handle_math(state):
    result = math_tool.run(state["input"])
    return {**state, "output": result}  

def handle_search(state):
    result = search_tool.run(state["input"])
    return {**state, "output": result} 