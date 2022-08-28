# Project Run Down
 Finetuning GPT-3 to talk more as a therapist or conversational partner would

## Steps
 ### Data Collection
 -  _8.26.22_ attempted to get transcripts from alexanderstreet.com,<br>
             but that failed miserably (javascript, login, no institutional access)
 -  _8.26.22_ realized I could use GPT3 itself to create the conversations. they would be just general enough and well written enough to <br>
      to pass as real prompt and response
   - _8.26.22_ used the file JSONLprep.py to turn the text file transcripts.txt into a suitable JSONL file
  -  _8.27.22_ created a script to generate therapist sessions with gpt3 itself
  -  _8.27.22_ data is saved and parsed with new methods to comply with jsonl


```python


jsonl = open("data/gpt_finetuning_data.jsonl", "a")


with open("data/examplegen.txt", "r") as f:

    for line in f:

        if "CLIENT:" in line:  # client is prompt

            line = line.strip("CLIENT:")
            jsonl.write('{"prompt" : ' + '"' + line.strip('\n') + '"' + ' , ')

        elif "THERAPIST:" in line:  # therapist is completion

            line = line.replace("THERAPIST:", "")
            jsonl.write('"completion" : ' + '"' +
                        line.strip('\n') + '"' + '}' + '\n')


jsonl.close()
f.close()


```

  ### Fine tuning
  - _8.27.22_ opened the project folder in wsl, set my OPENAI_API_KEY variable, then ran the finetuning script
  - _8.28.22_ trained once in the beginning, trained again with many more examples

### Model Access 
- _8.28.22_ Currently, the model is accessed through a rudimentary script

