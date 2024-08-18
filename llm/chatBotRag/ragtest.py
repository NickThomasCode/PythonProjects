# from langchain.text_splitter import CharacterTextSplitter
# from langchain.schema.document import Document
# from langchain_community.embeddings import OllamaEmbeddings

# text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=20)
# text = "I am going to tell you a story about Tintin."
# docs = [Document(page_content=x) for x in text_splitter.split_text(text)]


# from langchain_community.vectorstores import Chroma
# from langchain_community.llms import Ollama
# from langchain_community import embeddings
# persist_directory = "/tmp/chromadb"
# # vectorstore = Chroma.from_documents(
# #     documents=docs,
# #     collection_name="test",
# #     embedding=embeddings.ollama.OllamaEmbeddings(model='nomic-embed-text')
# # )

# vectorstore = Chroma.from_documents(
#     documents=docs,
#     collection_name="test",
#     embedding=embeddings.ollama.OllamaEmbeddings(
#         base_url='http://192.168.0.200:11434',
#         model='nomic-embed-text'
#     ),
# )
# retriever = vectorstore.as_retriever()


# from langchain_community.llms import Ollama
# llm = Ollama(model="mistral")


# from langchain_core.runnables import RunnablePassthrough
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import ChatPromptTemplate
# template = """Answer the question based only on the following context:
# {context}
# Question: {question}
# """
# prompt = ChatPromptTemplate.from_template(template)
# rag_chain = (
#     {"context": retriever, "question": RunnablePassthrough()}
#     | prompt
#     | llm
#     | StrOutputParser()
# )
# print(rag_chain.invoke("tell me a story"))


from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema.document import Document
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=20)
text = "I am going to tell you a story about Tintin."
docs = [Document(page_content=x) for x in text_splitter.split_text(text)]


from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain_community import embeddings
persist_directory = "/tmp/chromadb"
vectorstore = Chroma.from_documents(
    documents=docs,
    collection_name="test",
    embedding=embeddings.ollama.OllamaEmbeddings(
        base_url='http://localhost:8501',
        model='nomic-embed-text'
    ),
)
retriever = vectorstore.as_retriever()


from langchain_community.llms import Ollama
llm = Ollama(model="mistral")


from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
template = """Answer the question based only on the following context:
{context}
Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
print("DONE WITH PROMPT")
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)
print(rag_chain.invoke("tell me a story"))