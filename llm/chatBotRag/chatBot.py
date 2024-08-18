import streamlit as st

from langchain_community.document_loaders import WebBaseLoader

from langchain_community.vectorstores import Chroma

from langchain_community import embeddings

from langchain_community.llms import Ollama

from langchain_core.runnables import RunnablePassthrough

from langchain_core.output_parsers import StrOutputParser

from langchain_core.prompts import ChatPromptTemplate

from langchain.text_splitter import CharacterTextSplitter 

from langchain_community.embeddings import OllamaEmbeddings

from langchain.schema.document import Document

 # URL processing
def process_input(urls, question):
    model_local = Ollama(model="mistral")
    
    # Convert string of URLs to list
    urls_list = urls.split("\n")

    
    # docs = [WebBaseLoader(url).load() for url in urls_list]
    # docs_list = [item for sublist in docs for item in sublist]
    
    #split the text into chunks
    
    # text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=7500, chunk_overlap=100)
    # doc_splits = text_splitter.split_documents(docs_list)

    #convert text chunks into embeddings and store in vector database

    text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=20)
    text = "To pip install pandas use the command pip install pandas."
    docs = [Document(page_content=x) for x in text_splitter.split_text(text)]

    vectorstore = Chroma.from_documents(
    documents=docs,
    collection_name="rag-chroma",
    embedding=embeddings.ollama.OllamaEmbeddings(
        base_url='http://localhost:8501',
        model='nomic-embed-text'
    ),
)
    retriever = vectorstore.as_retriever()
    
    #perform the RAG 
    
    after_rag_template = """Answer the question based only on the following context:
    {context}
    Question: {question}
    """
    after_rag_prompt = ChatPromptTemplate.from_template(after_rag_template)
    after_rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | after_rag_prompt
        | model_local
        | StrOutputParser()
    )
    return after_rag_chain.invoke(question) 


st.title("Document Query with Ollama")
st.write("Enter URLs (one per line) and a question to query the documents.")

# Input fields
urls = st.text_area("Enter URLs separated by new lines", height=150)
question = st.text_input("Question")

# Button to process input
if st.button('Query Documents'):
    with st.spinner('Processing...'):
        answer = process_input(urls, question)
        st.text_area("Answer", value=answer, height=300, disabled=True) 
