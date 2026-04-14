# This requires ollama to be running.
# Install the model:  ollama pull <model>
# For a list of models:
# Start the ollama server:  ollama serve

from strands import Agent
from strands.models.ollama import OllamaModel

model_id = "tinyllama"

# ollama model instance
ollama_model = OllamaModel(
    host="http://localhost:11434",
    model_id=model_id,
)

# create the agent
agent = Agent(model=ollama_model)

# Use the agent
agent("When were you trained")
