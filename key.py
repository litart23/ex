import base64

def simple_encrypt(secret: str, key: str) -> str:
    """Простая шифровка строки с помощью XOR и ключа"""
    encrypted = []
    for i in range(len(secret)):
        key_char = key[i % len(key)]
        encrypted_char = chr(ord(secret[i]) ^ ord(key_char))
        encrypted.append(encrypted_char)
    return base64.b64encode(''.join(encrypted).encode()).decode()

def simple_decrypt(encrypted: str, key: str) -> str:
    """Расшифровка строки, зашифрованной simple_encrypt"""
    decoded = base64.b64decode(encrypted).decode()
    decrypted = []
    for i in range(len(decoded)):
        key_char = key[i % len(key)]
        decrypted_char = chr(ord(decoded[i]) ^ ord(key_char))
        decrypted.append(decrypted_char)
    return ''.join(decrypted)

# Пример использования:
if __name__ == "__main__":
    # Твой секретный ключ, который нельзя публиковать
    original_secret = "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"
    
    # Ключ для шифрования (должен быть достаточно длинным и сложным)
    # НИКОГДА не публикуй этот ключ!
    encryption_key = "test"
    
    print("Original:", original_secret)
    
    encrypted = simple_encrypt(original_secret, encryption_key)
    print("Encrypted:", encrypted)
    
    decrypted = simple_decrypt(encrypted, encryption_key)
    print("Decrypted:", decrypted)