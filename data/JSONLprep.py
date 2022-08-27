import os

#{"prompt":"","completion":""}

import json

jsonl = open("gpt_finetuning_data.jsonl", "w")



with open("transcripts.txt","r") as f:
    f_iter = iter(f)
    for i,line in enumerate(f):
            line = line.strip('\n')
            json.dump({'prompt': line , 'completion': next(f_iter).strip('\n')}, jsonl)  
            jsonl.write('\n')
        
    
jsonl.close()
f.close()




    

# with open('gpt_finetuning_data.jsonl', 'w') as outfile:
#     for i in range(1000):
#         json.dump({'prompt': , 'completion' : }, outfile)
#         outfile.write('\n')