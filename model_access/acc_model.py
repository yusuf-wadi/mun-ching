import openai

openai.api_key_path = "model_access/key.txt"
YOUR_PROMPT = input("Enter prompt: ")
cur_model = "davinci:ft-valley-2022-08-28-00-10-42"

with open("response.txt", "w") as f:
    completion = openai.Completion.create(
        model= cur_model,
        prompt= YOUR_PROMPT,
        temperature = 0.5,
        presence_penalty = 0.67,
        frequency_penalty = 0.7,
        max_tokens = 30    
        )
    f.write(completion.choices[0].text)

print(completion)
        
f.close()
