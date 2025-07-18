import os
from dotenv import load_dotenv

from openai import OpenAI
import base64
encryption_key = "test"
encrypted = "Bw5eBAYKGVlECiQ/OC08M0UoJjkYJhYgHwgcHDgrPAcgVTRNJzxeQhhTNgENMAI/AxA+AEcSSzVBCQsjAw43PAxXETkkHAYcMycwQTMiGh4SIydHNgkRHzIvBUY5FBExQDYeNxZVEhA3Jjo3WVcfWT4nQC0xPAAkGRMkJCxcHQMZLjhENUg7IR0KBi1FIDE9MRQjDgxdQQMDLxUYJjQrJQ5TGDU="

def decr() -> str:
    key = encryption_key
    """Расшифровка строки, зашифрованной simple_encrypt"""
    decoded = base64.b64decode(encrypted).decode()
    decrypted = []
    for i in range(len(decoded)):
        key_char = key[i % len(key)]
        decrypted_char = chr(ord(decoded[i]) ^ ord(key_char))
        decrypted.append(decrypted_char)
    #print(decrypted)    
    return ''.join(decrypted)

#decrypted = decr(encrypted, encryption_key)


def gen(prompt: str, key: str, system_message: str = "You are a helpful assistant. Give a short and clear answer.") -> str:
    client = OpenAI(
    # This is the default and can be omitted
    api_key=key,) 
    response = client.responses.create(
    model="gpt-4o",
    instructions=system_message,
    input=prompt,
    )
    print(response.output_text)
    
    return response.output_text
