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

    password=''.join(random.choice(characters) for i in range(min_lenght))
    return password