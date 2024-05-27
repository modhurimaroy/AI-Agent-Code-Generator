from llama_index.llms.ollama import Ollama

llm = Ollama( model = "mistral", request_timeout = 50.0)

result = llm.complete("Hello world")
print(result)