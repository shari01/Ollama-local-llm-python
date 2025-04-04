# first download ollama 
# install the required model
# use ollama pull "model-name" or ollama run "model-name"  that's all :)


import ollama

# Initialize the Ollama client
client = ollama.Client()

# Define the model and the input prompt
model = "Mistral:latest"  # Replace with your model name

prompt = "enlist the genes involved in the cancer"

# Send the query to the model
response = client.generate(model=model, prompt=prompt)

# Print the response from the model
print("Response from Ollama:")
print(response.response)
