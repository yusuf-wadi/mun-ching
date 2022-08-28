# Project Run Down
 Finetuning GPT-3 to talk more as a therapist or conversational partner would

## Steps
 ### Data Collection
  - attempted to get transcripts from alexanderstreet.com,<br>
  but that failed miserably (javascript, login, no institutional access)
  - realized I could use GPT3 itself to create the conversations. they would be just general enough and well written enough to <br>
      to pass as real prompt and response
  - removed all whitespaces and blank lines from the text file in the command line (grep "\S" file.txt)
  - used the file JSONLprep.py to turn the text file transcripts.txt into a suitable JSONL file
  - created a script to generate therapist sessions with gpt3 itself


```python

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

```

  ### Fine tuning
  - opened the project folder in wsl, set my OPENAI_API_KEY variable, then ran the finetuning script
  - trained once in the beginning, trained again with many more examples

