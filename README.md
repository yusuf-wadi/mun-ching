# Project Run Down

Finetuning GPT-3 to talk more as a therapist or conversational partner would

## Steps

### Data Collection

- _8.26.22_ Attempted a webscrape to get valuable data  
  Failed miserably
- _8.26.22_ realized I could use GPT3 itself to create the conversations. they would be just general enough and well written enough to <br>
  to pass as real prompt and response
- _8.26.22_ used the file JSONLprep.py to turn the text file transcripts.txt into a suitable JSONL file
- _8.27.22_ created a script to generate therapist sessions with gpt3 itself
- _8.27.22_ data is saved and parsed with new methods to comply with jsonl
- _3:14 AM 9/5/2022_ The big data has been caught. Alhamdulilah. 
### Fine tuning

- _8.27.22_ opened the project folder in wsl, set my OPENAI_API_KEY variable, then ran the finetuning script
- _8.28.22_ trained once in the beginning, trained again with many more examples
- _3:14 AM 9/5/2022_ Now that the BEEG data has been caught, new finetuning is in order. But the question is, is finetuning really 
                      the way to go about this? prompt engineering is already such a powerful tool. Further inquiry and research is required.
### Model Access

- _8.28.22_ Currently, the model is accessed through a rudimentary script
- _8.29.22_ The model is now accessible through a bare tkinter GUI in the tkGUI branch

### Adding model memory
- _2:53 PM 8/30/2022_ As when you talk to most people, they tend to remember the last thing you said. <br>
  As such, I am adding memory to this model through way of contextual prompting. 
- _3:14 AM 9/5/2022_ Memory has been added by way of prompt engineering and human ingenuity. 
- _12:01 PM 9/8/2022_ Memory and prompt have been optimized. Time for webapp

### Future Ideas
from _12:01 PM 9/8/2022_
- [X] Make webapp
- [ ] Figure out a way to finetune and move past full prompt engineering
from _2:29 AM 9/10/2022_
- [ ] Create search conversation function to optimize memory and return only relevant lines of conversation for summary and context.
