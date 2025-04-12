import os
from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0, 
                 model="gpt-3.5-turbo", 
                 openai_api_key=os.getenv("OPENAI_API_KEY"))

def classifier_node(state):
    message = state["input"]
    prompt = f"Klasifikasikan kategori input berikut:\n\n\"{message}\"\n\nJawab hanya salah satu dari: account_issues, product_info, pricing."
    
    response = llm.invoke(prompt)
    label = response.content.strip().lower()
    return {"category": label}

def response_node(state):
    label = state["category"]
    if label == "account_issues":
        return {"output": "Silakan klik 'Lupa Password' di halaman login."}
    elif label == "product_info":
        return {"output": "LangGraph adalah framework untuk membangun LLM workflows."}
    elif label == "pricing":
        return {"output": "Kami sedang ada promo, cek website kami untuk info lengkap!"}
    else:
        return {"output": "Maaf, saya tidak mengerti pertanyaan Anda."}

# Build the graph
graph_builder = StateGraph()
graph_builder.add_node("classifier", RunnableLambda(classifier_node))
graph_builder.add_node("responder", RunnableLambda(response_node))

graph_builder.set_entry_point("classifier")
graph_builder.add_edge("classifier", "responder")
graph_builder.set_finish_point("responder")

app = graph_builder.compile()

def run_graph(input_text: str):
    result = app.invoke({"input": input_text})
    return result["output"]
