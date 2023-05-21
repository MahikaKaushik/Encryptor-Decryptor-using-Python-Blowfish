from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad

def encrypt_message(message, key):
    cipher = Blowfish.new(key.encode(), Blowfish.MODE_ECB)
    padded_message = pad(message.encode(), Blowfish.block_size)
    ciphertext = cipher.encrypt(padded_message)
    return ciphertext.hex()

def decrypt_message(ciphertext, key):
    cipher = Blowfish.new(key.encode(), Blowfish.MODE_ECB)
    decrypted_message = cipher.decrypt(bytes.fromhex(ciphertext))
    message = unpad(decrypted_message, Blowfish.block_size).decode()
    return message

# Example usage:
message = input("Enter a message to encrypt: ")
key = input("Enter an encryption key: ")

encrypted_message = encrypt_message(message, key)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt_message(encrypted_message, key)
print("Decrypted message:", decrypted_message)
