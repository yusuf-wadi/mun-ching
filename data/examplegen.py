from random import randint, randrange
import openai
import os



openai.api_key_path = "model_access/key.txt"

professions = []

with open('data/professions.txt', "r") as f:
    professions = f.read().split(',')


e = open("data/examplegen_dirty.txt","r+")
    

for i in range(0,15):
    response = openai.Completion.create(
            model="text-davinci-002",
            max_tokens = 2000,
            prompt = "Generate a unique and lengthy conversation between a " + professions[randrange(len(professions))] +  " client and a therapist that follows the flow ""CLIENT:'' , THERAPIST:'' """,
            temperature = 0.85,
            presence_penalty = 0.67,
            frequency_penalty = 0.7,    
        )
    e.write(response.choices[0].text)





#opening clean file

a = open("data/examplegen.txt","a+")

data = e.read()

#data clean

to_replace = {"CLIENT:" : '',
              "THERAPIST:" : '',
              "LAWYER:" : '',
              "\n\n" : "\n",}

for k,v in to_replace.items():
    data = data.replace(k,v)

a.write(data)

#closing files

e.close()
f.close()
a.close()



