import openai

# set api key
openai.api_key_path = "model/text/key.txt"
cur_model = "text-davinci-002"
done = False

curcon_path = 'model/text/mem/cur_convo.txt'
res_path = 'model/text/response.txt'
ctx_path = 'model/text/mem/cntx_prompt.txt'
baseCTX_path = "model/text/mem/baseCTX.txt"

while not done:

    YOUR_PROMPT = input("Enter prompt: ")
    if YOUR_PROMPT == "exit session":
        done = True
        break

    # hintGen = "Paraphrase the therapy clients intents based on the following string: " + '"' + YOUR_PROMPT + '"'

    # HINT = openai.Completion.create(
    #     model=cur_model,
    #     prompt=hintGen,
    #     temperature=0.3,
    #     presence_penalty=0.5,
    #     frequency_penalty=0.5,
    #     max_tokens=100,

    # )

    #update convo and read in hint
    with open(curcon_path,"a+") as cc:
        cc.write(" CLIENT: " + YOUR_PROMPT)
        cc.close()
    with open(curcon_path,"r") as cc:
        HINT = cc.read()
        cc.close()
    #####

    with open(ctx_path, "r") as ctx:
        ctxPrompt = ctx.read()
        ctx.close()

    ctxPrompt = ctxPrompt.format(YOUR_PROMPT, HINT)


    completion = openai.Completion.create(
        model=cur_model,
        prompt=ctxPrompt,
        temperature=0.3,
        presence_penalty=0.5,
        frequency_penalty=0.5,
        max_tokens=100,

    )
    print(completion.choices[0].text)

    #update convo 
    with open(curcon_path,"a+") as cc:
        cc.write("\n THERAPIST: " + completion.choices[0].text.strip('\n') + '\n')
        cc.close()



# erase convo file
cur_convo = open(curcon_path, "w")
cur_convo.close()
####


