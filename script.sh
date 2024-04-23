#!/bin/bash

directories=("codex" "copilot")

for directory in "${directories[@]}"; do
    echo "Executing Python files in directory: $directory"
    
    for file in "$directory"/*.py; do
        echo "Running: $file"
        
        start=$(date +%s.%N)
        
        python "$file"
        
        end=$(date +%s.%N)
        duration=$(echo "$end - $start" | bc)
        echo "Execution time: $duration seconds"
        echo
    done
done
