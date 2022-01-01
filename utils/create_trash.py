import random

def random_text(length):
    text = ""

    for _ in range(length):
        letter = random.randrange(start=97, stop=123)
        text += chr(letter)

    return text

def random_texts(length, words):
    description = ""

    for _ in range(words):
        text = random_text(length)
        description += " " + text
    
    return description

def random_line():

    name_length = random.randrange(4, 8)
    words_length = random.randrange(3, 7)
    words_quantity = random.randrange(15, 500)

    random_name = random_text(name_length)
    random_description = random_texts(words_length, words_quantity)
    line = f"{random_name},{random_description}\n"

    return line

with open('trash.csv', 'a') as file:
    file.write('name, description\n')

    for i in range(1500000):
        file.write(random_line())
