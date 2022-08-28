from random import randrange
import openai
import re
import os


openai.api_key_path = "model_access/key.txt"

professions = []

with open('data/professions.txt', "r") as f:
    professions = f.read().split(',')

# open for read and write
e = open("data/examplegen_dirty.txt", "r+")

# #break da bank
# for i in range(0,30):
#     response = openai.Completion.create(
#             model="text-davinci-002",
#             max_tokens = 2000,
#             #randomizing professions to get varied responses W
#             prompt = "Generate a unique and lengthy conversation between a " + professions[randrange(len(professions))] +  " client and a therapist that follows the flow CLIENT: THERAPIST: . When putting words in quotations use single quotes, and do not deviate from the alternating flow of client to therapist.",
#             temperature = 0.80,
#             presence_penalty = 0.7,
#             frequency_penalty = 0.8,
#         )
#     e.write(response.choices[0].text)


# opening clean file

a = open("data/examplegen.txt", "w")

data = e.read()

# data clean

to_replace = {"LAWYER:": "CLIENT:",
              "DOCTOR:": "CLIENT:",
              "BARTENDER:": "THERAPIST:",
              "PHYSICIAN ASSISTANT:": "THERAPIST:",
              "\n\n": "\n",
              ":\n": ":"}

for k, v in to_replace.items():
    repl = re.compile(k, re.IGNORECASE)
    data = repl.sub(v, data)

a.write(data)

# closing files

e.close()
f.close()
a.close()


exec(open('data\JSONLprep.py').read())
