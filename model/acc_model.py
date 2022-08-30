import openai

#set api key
openai.api_key_path = "model/key.txt"
YOUR_PROMPT = input("Enter prompt: ")
cur_model = "davinci:ft-valley-2022-08-28-00-10-42"

curcon_path = 'model/text/mem/cur_convo.txt'
res_path = 'model/text/response.txt'
ctx_path = 'model/text/mem/cntx_prompt.txt'

cur_convo = open(curcon_path,"a")

with open(ctx_path, "w+") as ctx:
    ctxPrompt = ctx.read()


with open(res_path, "w") as f:
    completion = openai.Completion.create(
        model= cur_model,
        prompt= ctxPrompt,
        temperature = 0.3,
        presence_penalty = 0.5,
        frequency_penalty = 0.5,
        max_tokens = 100,
        stop = ["CLIENT:","?"]
  
        )
    f.write(completion.choices[0].text)


        
f.close()
cur_convo.write()
cur_convo.close()

