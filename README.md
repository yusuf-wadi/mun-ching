# Project Run Down
- Finetuning GPT-3 to talk more as a therapist or conversational partner would

## Steps
 ### Data Collection
    - attempted to get transcripts from alexanderstreet.com, but that failed miserably (javascript, login, no institutional access)
    - realized I could use GPT3 itself to create the conversations. they would be just general enough and well written enough to <br>
      to pass as real prompt and response
    - removed all whitespaces and blank lines from the text file in the command line (grep "\S" file.txt)
    - used the file JSONLprep.py to turn the text file transcripts.txt into a suitable JSONL file



```python
import json

jsonl = open("gpt_finetuning_data.jsonl", "w")



with open("transcripts.txt","r") as f:
    f_iter = iter(f)
    for i,line in enumerate(f):
            line = line.strip('\n')
            json.dump({'prompt': line , 'completion': next(f_iter).strip('\n')}, jsonl)  
            jsonl.write('\n')
```

  ### Fine tuning
    - opened the project folder in wsl, set my OPENAI_API_KEY variable, then ran the finetuning script
    - very light training file, cost 25cents, gave me strange results.
