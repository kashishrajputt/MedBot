from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os

app = Flask(__name__)

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
GROQ_API_KEY  = os.environ.get('GROQ_API_KEY')

load_dotenv()



embeddings = download_hugging_face_embeddings()

index = "medbot"

docsearch = PineconeVectorStore.from_existing_index(
    index_name = "medbot",
    embedding = embeddings,
)

retriever = docsearch.as_retriever(search_type= 'similarity', search_kwargs={'k':3})

llm = ChatGroq(
    temperature = 0.4, 
    max_tokens  = 500,
    groq_api_key = GROQ_API_KEY,
    model_name = "llama3-70b-8192"
    )

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human","{input}"),
        
    ]
)

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET","POST"])
def chat():
    msg = request.form['msg']
    input = msg
    print(input)
    response = rag_chain.invoke({"input":msg})
    print("Response : ", response["answer"])
    return str(response["answer"])

if __name__ =='__main__':
    app.run(debug=True)