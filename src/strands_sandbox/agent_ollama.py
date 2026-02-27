# This requires ollama to be running.
# Install the llama3.1 model:  ollama pull llama3.1
# Start the ollama server:  ollama serve

from strands import Agent
from strands.models.ollama import OllamaModel

# ollama model instance
ollama_model = OllamaModel(
    host="http://localhost:11434",
    model_id="tinyllama",
)

# create the agent
agent = Agent(model=ollama_model)

# Use the agent
agent("When were you trained")
