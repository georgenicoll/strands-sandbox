# This requires ollama to be running.
# Install the llama3.1 model:  ollama pull llama3.1
# Start the ollama server:  ollama serve

from strands import Agent
from strands.models.ollama import OllamaModel

# create the agent
agent = Agent()

agent("Tell me about agentic AI")
