import random


def jig(letter):
    second_choice = ""

    if letter.lower() == "f":
        second_choice = "v"
    elif letter.lower() == "k":
        second_choice = "ck"
    elif letter.lower() == "o":
        second_choice = "oa"
    elif letter.lower() == "r":
        second_choice = "l"
    elif letter.lower() == "l":
        second_choice = "r"
    elif letter.lower() == "s":
        second_choice = random.choice(["sd", "ss", "as"])
    elif letter.lower() == "y":
        second_choice = "u"
    elif letter.lower() == "u":
        second_choice = "y"
    elif letter.lower() == "z":
        second_choice = "x"
    elif letter.lower() == "x":
        second_choice = "z"

    if second_choice == "":
        return random.choice([letter.lower(), letter.lower(), letter.lower(), letter.lower(), "{}{}".format(letter.lower(), letter.lower())])
    else:
        return random.choice([letter.lower(), letter.lower(), letter.lower(), letter.lower(), second_choice])