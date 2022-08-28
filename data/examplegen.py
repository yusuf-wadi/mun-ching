from random import randint, randrange
import openai


openai.api_key_path = "model_access/key.txt"

professions = []

with open('data/professions.txt', "r") as f:
    professions = f.read().split(',')


e = open("data/examplegen.txt","a")
    

for i in range(0,30):
    response = openai.Completion.create(
            model="text-davinci-002",
            max_tokens = 2000,
            prompt = "Generate a unique and lengthy conversation between a " + professions[randrange(23)] +  " client and a therapist that follows the flow ""CLIENT:'' , THERAPIST:'' """,
            temperature = 0.85,
            presence_penalty = 0.67,
            frequency_penalty = 0.7,    
        )
    e.write(response.choices[0].text)

e.close()
f.close()

