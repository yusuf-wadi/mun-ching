

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
