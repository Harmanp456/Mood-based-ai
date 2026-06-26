from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")


response = model.invoke("Hello, how are you?")
print(response.content)