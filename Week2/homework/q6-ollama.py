from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',
)

def llm(prompt):
    response = client.chat.completions.create(
        model='gemma:2b',
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0
    )
    
    return response

prompt = "What's the formula for energy?"
response = llm(prompt)
print(response.choices[0].message.content)
print(f"Length of the prompt: {len(response.choices[0].message.content)}")
print(f"Number of tokens: {response.usage.completion_tokens}")