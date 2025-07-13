import openai
encryption_key = "test"
   
encrypted = "Bw5eBAYKGVkfFxU1KxJAPx0gGwMZMDhAMQonAwA2OyUkBwAiTQheASU2NUI+VhkORhIeGTpWNwJZIjsNEAoCFjYgNScxNAouTT8QHFkyGxEeVSdHNgkRHzIvOC0gA0czIjAgRDc8PSUHNTpHHQYVNwJRCz43HyYWMgwDQzYAAxJEFEoBMTQhRy0KBBAWISoNQgI6Aw4fQDI/EAk7DgEeIhU6QzU="
    
def generate_response(prompt: str, api_key: str, system_message: str = "You are a helpful assistant. Give a short and clear answer.") -> str:
    decrypted = simple_decrypt(encrypted, encryption_key)

    openai.api_key = decrypted
    
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response['choices'][0]['message']['content'].strip()


import base64


def simple_decrypt(encrypted: str, key: str) -> str:
    """Расшифровка строки, зашифрованной simple_encrypt"""
    decoded = base64.b64decode(encrypted).decode()
    decrypted = []
    for i in range(len(decoded)):
        key_char = key[i % len(key)]
        decrypted_char = chr(ord(decoded[i]) ^ ord(key_char))
        decrypted.append(decrypted_char)
    return ''.join(decrypted)
