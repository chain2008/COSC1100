"""
Assignment2: Secret Codes (Arrays & Functions) 
Author: Cheng He
Date: 2024-11-1
Version: 1
"""
import base3cipher

text = "This is a plain Text"
txt_length = len(text)
key = base3cipher.gen_key(txt_length)
cipher_text = ""
for index in range(0, txt_length):
    cipher_text += base3cipher.base3_cipher(text[index],key[index])
print(cipher_text)

plain_text = ""
for index in range(0, txt_length):
    plain_text += base3cipher.base3_cipher(cipher_text[index],key[index])
print(plain_text)
