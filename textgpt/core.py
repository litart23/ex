import openai

def generate_response(prompt: str, api_key: str, system_message: str = "You are a helpful assistant. Give a short and clear answer.") -> str:
    
    openai.api_key = "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"

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response['choices'][0]['message']['content'].strip()
