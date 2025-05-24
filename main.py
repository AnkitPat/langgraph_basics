from langgraph.graph import StateGraph, END
from langgraph_init import classify_message, handle_math, handle_search, handle_math_verifier
from typing import TypedDict
from IPython.display import Image, display
from pathlib import Path

class GraphState(TypedDict):
    input: str
    route: str
    output: str
    verified_output: str

builder = StateGraph(GraphState)
builder.add_node("classify", classify_message)
builder.add_node("math", handle_math)
builder.add_node("search", handle_search)
builder.add_node("math_verifier", handle_math_verifier)

builder.set_entry_point("classify")
builder.add_conditional_edges("classify", lambda state: state["route"], {
    "math": "math",
    "search": "search"
})

# builder.add_edge("math", END)
# builder.add_conditional_edges("classify", lambda state: state["route"], {
#     "math_result": "math_result",
#     "math_verifier": "math_verifier"
# })
builder.add_edge("math", "math_verifier")
builder.add_edge("math_verifier", END)
builder.add_edge("search", END)

graph = builder.compile()


# Get the image object
img_data = graph.get_graph().draw_mermaid_png()

Path("langgraph_diagram.png").write_bytes(img_data)

# for display
Image(data=img_data)


print(graph.invoke({"input": "What is the square root of 144 plus 6?"}))
# print(graph.invoke({"input": "What is the capital of india?"}))