
import re

jsonl = open("data/gpt_finetuning_data_v2_1.jsonl", "w")


with open("crawlers/transcripts_v2_1.txt", "r") as f:

    for line in f:

        line.replace('-','')

        if bool(re.match("^CLIENT:",line)):  # client is prompt
            line.replace('"',"'")
            line = line.replace("CLIENT:","")
            line = line.replace("THERAPIST:", "")
            jsonl.write('{"prompt" : ' + '"' + line.strip('\n') + '"' + ' , ')

        elif bool(re.match("^THERAPIST:",line)):  # therapist is completion
            line.replace('"',"'")
            line = line.replace("CLIENT:","")
            line = line.replace("THERAPIST:", "")
            jsonl.write('"completion" : ' + '"' +
                        line.strip('\n') + '"' + '}' + '\n')


jsonl.close()
f.close()
