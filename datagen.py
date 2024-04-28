import subprocess
from codecarbon import EmissionsTracker

filepath1 = "/Users/pratik/Documents/UB Spring 2024/Courses/CSE709/cse709_project/Codex/easy/happyNumber_easy.py"
filepath2 = "/Users/pratik/Documents/UB Spring 2024/Courses/CSE709/cse709_project/Copilot/easy/happyNumber_easy.py"
filepaths = [filepath1, filepath2]
# filepaths = [filepath1]

for filepath in filepaths:
    tracker = EmissionsTracker()
    tracker.start()
    for i in range(10000):
        subprocess.run(["python", filepath])
        if i % 1000 == 0:
            print(i," CYCLES DONE")
    tracker.stop()