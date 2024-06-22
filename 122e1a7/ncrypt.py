import random
import string
import base64
import json

def random_number(A, I):
    # This function generates a random integer between A and I
    return random.randint(A, I)

def encrypt(str):
    # Define the alphabet
    alphabet = string.ascii_lowercase
    
    # Check if the input string is null
    if str is None:
        return None
    
    # Generate 13 random uppercase characters
    list_joined = ''.join(random.choices(string.ascii_uppercase, k=13))
    
    # Generate a random integer between 1 and 26
    rand = random_number(1, 26)
    
    # Reverse the string, split it into characters, and apply rotation
    a = ''.join([rotate_char(char, rand, alphabet) if char.isalpha() else char for char in reversed(str)])
    
    # Encode the string to Base64 and reverse it
    encoded_str = base64.b64encode(a.encode()).decode()[::-1]
    
    # Generate a random integer between 1 and the length of the encoded string - 1
    rand_2 = random_number(1, len(encoded_str) - 1)
    
    # Circularly shift the characters and reverse their case based on list_joined
    transformed_str = circular_shift(encoded_str, rand_2)
    transformed_str = reverse_case(transformed_str, list_joined)
    
    # Convert rand and rand_2 to hexadecimal strings
    rand_hex = hex(rand)[2:]
    rand_2_hex = hex(rand_2)[2:]
    
    return transformed_str, rand_hex, rand_2_hex, list_joined

def rotate_char(char, rotation, alphabet):
    # This function rotates a character by the specified rotation
    if char.isalpha():
        index = (alphabet.index(char.lower()) + rotation) % 26
        return alphabet[index].upper() if char.isupper() else alphabet[index]
    return char

def circular_shift(text, rand_2):
    # This function circularly shifts the characters of a text by rand_2 positions
    return text[rand_2:] + text[:rand_2]

def reverse_case(text, list_joined):
    # This function reverses the case of characters based on the characters in list_joined
    return ''.join([char.lower() if char in list_joined + list_joined.lower() else char.upper() for char in text])



