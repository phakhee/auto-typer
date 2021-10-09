import faster as faster
from pynput.keyboard import Key, Controller
import time
import random
import datetime
import os
import json
import sys
from alfabet_jig import jig

IGNORE_JIG_WILDCARD = True

keyboard = Controller()
random_sentences = []
config_format = {
    "min_delay": 60,
    "max_delay": 90,
    "history_size": 10,
}

if not os.path.exists("sentences.txt"):
    open("sentences.txt", "x")
    print("Created sentences.txt file")

if not os.path.exists("config.json"):
    with open("config.json", "w") as outfile:
        json.dump(config_format, indent=4, fp=outfile)
        print("Created config.json file")


if not os.path.exists("history.json"):
    with open("history.json", "w") as outfile:
        json.dump([], indent=4, fp=outfile)
        print("Created history.json file")


text_file = open("sentences.txt", "r")
for sentence in text_file.read().split("\n"):
    if len(sentence) > 0:
        random_sentences.append(sentence)

with open("config.json") as json_file:
    config = json.load(json_file)

min_delay = config["min_delay"]
max_delay = config["max_delay"]
history_size = config["history_size"]

with open("history.json") as json_file:
    history = json.load(json_file)

time.sleep(3)
if len(random_sentences) > 0:
    while True:
        random_sentence = random.choice(random_sentences)

        if random_sentence in history:
            continue

        if len(history) >= history_size:
            history.pop(0)

        history.append(random_sentence)

        with open("history.json", "w") as outfile:
            json.dump(history, indent=4, fp=outfile)

        print("[{}] {}".format(datetime.datetime.now(), random_sentence))

        prev_ch = ""

        # If the sentence starts with a wildcard then we do not want to jig
        ignore_jig = random_sentence[0] != IGNORE_JIG_WILDCARD
        if not ignore_jig:
            # Jigging is disabled for this sentence, remove the * wildcard
            random_sentence = random_sentence[1:]

        for i in random_sentence:
            if prev_ch == " " or prev_ch == "" and not ignore_jig:
                jigged_i = jig(i)
                keyboard.type(jigged_i)
            else:
                keyboard.type(i)

            prev_ch = i
            time.sleep(0.1)

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        delay = random.randint(min_delay, max_delay)

        time.sleep(delay)
else:
    print("No sentences found.")
    os.system('pause')
    sys.exit()
