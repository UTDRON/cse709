import subprocess
from codecarbon import EmissionsTracker
import os
import pandas as pd
import time

# Define the root directory
root_dir = os.getcwd()

arguments = ["1"]
models                      = ['/Codex','/Copilot']
difficulties                = ['/easy','/medium','/hard']
directory                   = root_dir + "/Codex/easy/"
problems                    = []
llm_used                    = []
diff                        = []
run_times                   = []
for model in models:
    for difficulty in difficulties:
        directory = root_dir + model + difficulty
        # print(directory)
        for file in os.listdir(directory):
            files_to_run = [
                root_dir + "/Codex" + difficulty + "/" + file,
                root_dir + "/Copilot" + difficulty + "/" + file,
            ]
            llm_used.append("Codex")
            llm_used.append("Copilot")
            problems.append(file)
            problems.append(file)
            for item in files_to_run:
                print(item)
                start_time = time.time()
                subprocess.run(["python", item] + arguments)
                end_time = time.time()
                elapsed_time = end_time - start_time    
                run_times.append(elapsed_time)            


    break

for problem in problems:
    if "_easy.py" in problem:
        diff.append("easy")
    elif "_medium.py" in problem:
        diff.append("medium")
    else:
        diff.append("hard")

time_df = pd.DataFrame(problems, columns=['problems'])
time_df['llm_used'] = llm_used
time_df['difficulty'] = diff
time_df['run_times'] = run_times
time_df.to_csv("single_cycle_sim3.csv", index=False)

