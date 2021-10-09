from pynput.keyboard import Key, Controller
import time
import random
import datetime
import os
import json
import sys
from alfabet_jig import jig

keyboard = Controller()
random_sentences = []
config_format = {
    "delay": 60
}

if not os.path.exists("sentences.txt"):
    open("sentences.txt", "x")
    print("Created sentences.txt file")

if not os.path.exists("config.json"):
    with open("config.json", "w") as outfile:
        json.dump(config_format, indent=4, fp=outfile)
        print("Created config.json file")

text_file = open("sentences.txt", "r")
for sentence in text_file.read().split("\n"):
    if len(sentence) > 0:
        random_sentences.append(sentence)

with open("config.json") as json_file:
    config = json.load(json_file)

time.sleep(3)
if len(random_sentences) > 0:
    while True:
        random_sentence = random.choice(random_sentences)
        print("[{}] {}".format(datetime.datetime.now(), random_sentence))

        prev_ch = ""
        for i in random_sentence:

            if prev_ch == " " or prev_ch == "":
                jigged_i = jig(i)
                keyboard.type(jigged_i)
            else:
                keyboard.type(i)

            prev_ch = i
            time.sleep(0.1)

        keyboard.press(Key.enter)

        time.sleep(config["delay"])
else:
    print("No sentences found.")
    os.system('pause')
    sys.exit()