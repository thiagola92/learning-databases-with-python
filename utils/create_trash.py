import random

def random_text(length=5):
    text = ""

    for i in range(length):
        letter = random.randrange(start=97, stop=123)
        text = text + chr(letter)

    return text

def random_description(words=20):
    description = ""

    for i in range(words):
        length = random.randrange(start=3, stop=7)
        text = random_text(length)
        description = description + " " + text
    
    return description

def random_line():
    line = "\n"

    name_length = random.randrange(4, 8)
    description_length = random.randrange(15, 500)

    line = line + random_text(name_length) + ","
    line = line + random_description(description_length)

    return line

with open('big_file', 'a') as file:
    # file.write('name,description')

    for i in range(100000):
        file.write(random_line())
