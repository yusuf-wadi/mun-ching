import openai

openai.api_key_path = "model_access/key.txt"
YOUR_PROMPT = input("Enter prompt: ")

with open("response.txt", "w") as f:
    completion = openai.Completion.create(
        model="davinci:ft-valley-2022-08-28-00-10-42",
        prompt= YOUR_PROMPT)
    f.write(completion.choices[0].text)

print(completion)
        
f.close()
