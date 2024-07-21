# Homework : Open-Source LLMs

## Question 1. Running Ollama with Docker

```bash

# Launch docker for ollama
docker run -it \
    --rm \
    -v ollama:/root/.ollama \
    -p 11434:11434 \
    --name ollama \
    ollama/ollama

# Enter the container
docker exec -it ollama bash

# Command to know the version
ollama -v

```

*What's the version of ollama client?*

**Answer:** ollama version is 0.1.48

## Question 2. Downloading an LLM

```bash

# Inside the container
ollama pull gemma:2b
```

*What's the content of the file related to gemma?*

```bash

cd /root/.ollama/models/manifests/registry.ollama.ai/library/gemma
```

![alt text](manifest_gemma.png)

**Answer:**
{"schemaVersion":2,"mediaType":"application/vnd.docker.distribution.manifest.v2+json","config":{"mediaType":"application/vnd.docker.container.image.v1+json","digest":"sha256:887433b89a901c156f7e6944442f3c9e57f3c55d6ed52042cbb7303aea994290","size":483},"layers":[{"mediaType":"application/vnd.ollama.image.model","digest":"sha256:c1864a5eb19305c40519da12cc543519e48a0697ecd30e15d5ac228644957d12","size":1678447520},{"mediaType":"application/vnd.ollama.image.license","digest":"sha256:097a36493f718248845233af1d3fefe7a303f864fae13bc31a3a9704229378ca","size":8433},{"mediaType":"application/vnd.ollama.image.template","digest":"sha256:109037bec39c0becc8221222ae23557559bc594290945a2c4221ab4f303b8871","size":136},{"mediaType":"application/vnd.ollama.image.params","digest":"sha256:22a838ceb7fb22755a3b0ae9b4eadde629d19be1f651f73efb8c6b4e2cd0eea0","size":84}]}

## Question 3. Running the LLM

*Test the following prompt: "10 * 10". What's the answer?*

![alt text](prompt_ollama.png)

**Answer:** Sure. 10 * 10 is 100.

## Question 4. Downloading the weights

```bash
mkdir ollama_files

docker run -it \
    --rm \
    -v ./ollama_files:/root/.ollama \
    -p 11434:11434 \
    --name ollama \
    ollama/ollama

docker exec -it ollama ollama pull gemma:2b 

# in the folder where ollama_files is
du -h
```

*What's the size of the ollama_files/models folder?*

**Answer:** 1.6G

## Question 5. Adding the weights

*What's do you put after `COPY` ?*

**Answer:** ollama_files/ root/.ollama/

## Question 6. Serving it

![alt text](image.png)

*How many completion tokens did you get in response?*

**Answer:** 304


