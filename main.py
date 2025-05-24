from langgraph.graph import StateGraph, END
from langgraph_init import classify_message, handle_math, handle_search
from typing import TypedDict

class GraphState(TypedDict):
    input: str
    route: str
    output: str

builder = StateGraph(GraphState)
builder.add_node("classify", classify_message)
builder.add_node("math", handle_math)
builder.add_node("search", handle_search)

builder.set_entry_point("classify")
builder.add_conditional_edges("classify", lambda state: state["route"], {
    "math": "math",
    "search": "search"
})

builder.add_edge("math", END)
builder.add_edge("search", END)

graph = builder.compile()

# print(graph.invoke({"input": "What is the square root of 144 plus 6?"}))
print(graph.invoke({"input": "What is the capital of india?"}))