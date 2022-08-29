from random import randrange
import openai
import re
import os


openai.api_key_path = "model_access/key.txt"

professions = []

proftxt_path = 'data/text/professions.txt'
exgen_path = 'data/text/examplegen.txt'
exgendr_path = 'data/text/examplegen_dirty.txt'


with open(proftxt_path, "r") as f:
    professions = f.read().split(',')

# open for read and write
e = open(exgendr_path, "r+")

# #break da bank
for i in range(0,10):
    response = openai.Completion.create(
            model="text-davinci-002",
            max_tokens = 2000,
            #randomizing professions to get varied responses W
            prompt = "Generate a unique and lengthy conversation between a " + professions[randrange(len(professions))] +  " client and a therapist that follows the flow CLIENT: THERAPIST: . When putting words in quotations use single quotes, and do not deviate from the alternating flow of client to therapist.",
            temperature = 1,
            presence_penalty = 1,
            frequency_penalty = 1,
        )
    e.write(response.choices[0].text)


# opening clean file

a = open(exgen_path, "w")

data = e.read()

# data clean

to_replace = {"LAWYER:": "CLIENT:",
              "DOCTOR:": "CLIENT:",
              "BARTENDER:": "THERAPIST:",
              "PHYSICIAN ASSISTANT:": "THERAPIST:",
              "\n\n": "\n",
              ":\n\n": ":"}

for k, v in to_replace.items():
    repl = re.compile(k, re.IGNORECASE)
    data = repl.sub(v, data)

a.write(data)

# closing files

e.close()
f.close()
a.close()


exec(open('data\JSONLprep.py').read())
