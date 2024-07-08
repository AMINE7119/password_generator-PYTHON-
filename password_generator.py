import random
import string

def generate_password(min_lenght, numbers=True,special_caracteres=True):

    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation

    characters=letters
    if numbers:
        characters+=digits
    if special_caracteres:
        characters+=special
    pwd=""
    meets_criteria=False
    has_numbers=False
    has_special=False

    while not meets_criteria or len(pwd)<min_lenght:
