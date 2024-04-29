import subprocess
from codecarbon import EmissionsTracker
import os
import pandas as pd

# Define the root directory
root_dir = os.getcwd()

arguments = ["1"]
models                      = ['/Codex','/Copilot']
difficulties                = ['/easy','/medium','/hard']
directory                   = root_dir + "/Codex/easy/"
problems                    = []
llm_used                    = []
diff                        = []
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
                tracker = EmissionsTracker()
                tracker.start()
                # subprocess.run(["python", item])
                subprocess.run(["python", item] + arguments)
                tracker.stop()

    break

for problem in problems:
    if "_easy.py" in problem:
        diff.append("easy")
    elif "_medium.py" in problem:
        diff.append("medium")
    else:
        diff.append("hard")

emissions_df = pd.read_csv("emissions.csv")
selected_columns = ['timestamp','duration','emissions','emissions_rate','cpu_power','gpu_power','ram_power','cpu_energy','gpu_energy','ram_energy','energy_consumed']
selected_df = emissions_df[selected_columns]
selected_df['problems'] = problems
selected_df['llm_used'] = llm_used
selected_df['difficulty'] = diff
selected_df.to_csv("selected_emissions.csv", index=False)

