import random


def create_word():
    length = random.randrange(3, 9)
    word = ""

    for _ in range(length):
        letter = random.randrange(start=97, stop=123)
        word += chr(letter)

    return word


def create_words(quantity):
    words = set()

    while len(words) < quantity:
        word = create_word()
        words.add(word)

    return list(words)


def create_description(words):
    quantity_of_words = random.randrange(15, 500)
    description_words = random.choices(words, k=quantity_of_words)
    description = " ".join(description_words)

    return description


def create_line(words):
    name = random.choice(words)
    description = create_description(words)
    line = f"{name},{description}\n"

    return line


with open("utils/trash.csv", "w") as file:
    lines = 100_000
    words = create_words(quantity=200_000)

    for _ in range(lines):
        line = create_line(words)
        file.write(line)
