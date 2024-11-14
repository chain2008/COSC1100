"""
Assignment2: Secret Codes (Arrays & Functions) 
Author: Cheng He
Date: 2024-11-1
Version: 1
"""
import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util
import Assignment2.cipher as cipher

if __name__ == "__main__":
    if len(sys.argv) > 1:
        text = sys.argv[1]
    else:
        text = util.get_input("Input plain Text: ")
txt_length = len(text)
key = cipher.gen_key(txt_length)
cipher_text = ""
for index in range(0, txt_length):
    cipher_text += cipher.base3_cipher(text[index],key[index])
print(f"cipher: {cipher_text}")

plain_text = ""
for index in range(0, txt_length):
    plain_text += cipher.base3_cipher(cipher_text[index],key[index])
print(f"plain: {plain_text}")
