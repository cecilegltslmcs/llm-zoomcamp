# Instal ollama
curl -fsSL https://ollama.com/install.sh | sh

# Download and run the model
ollama run phi3

# List the models on the machine
ollama list

# Docker command for ollama
docker run -it \
    -v ollama:/root/.ollama \
    -p 11434:11434 \
    --name ollama \
    ollama/ollama

docker exec -it ollama bash
ollama pull phi3