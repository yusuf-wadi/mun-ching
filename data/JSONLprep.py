

jsonl = open("data/gpt_finetuning_data.jsonl", "a")



with open("data/examplegen.txt","r") as f:
    f_iter = iter(f)
    for i,line in enumerate(f):
        if i%2==0:           # every even (0, 2, 4...) row
            jsonl.write('{"prompt":' + '"' + line.strip('\n') + '"' + ',')
        else:                # every odd (1, 3...) row
           jsonl.write('"completion":' + '"' + line.strip('\n') + '"' +'}' + '\n')
          
    
jsonl.close()
f.close()




    
