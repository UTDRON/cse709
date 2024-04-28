# #!/bin/bash

# directories=("codex" "copilot")

# for directory in "${directories[@]}"; do
#     echo "Executing Python files in directory: $directory"
    
#     for file in "$directory"/*.py; do
#         echo "Running: $file"
        
#         start=$(date +%s.%N)
        
#         python "$file"
        
#         end=$(date +%s.%N)
#         duration=$(echo "$end - $start" | bc)
#         echo "Execution time: $duration seconds"
#         echo
#     done
# done
#---------------------------------------------------------------------------------
# #!/bin/bash

# # Function to execute Python files and measure execution time
# execute_python_files() {
#     local folder="$1"
#     local output_file="$2"

#     # Loop through each Python file in the specified folder
#     for file in "$folder"/*.py; do
#         # Get the name of the Python file
#         filename=$(basename "$file")

#         # Measure execution time
#         execution_time=$( { time python3 "$file"; } 2>&1 | grep real | awk '{print $2}')

#         # Print execution time
#         echo "$filename: $execution_time" >> "$output_file"
#     done
# }

# # Main script
# output_file="execution_times.txt"

# # Execute Python files in the 'codex' folder
# echo "Executing Python files in the 'codex' folder..."
# execute_python_files "codex" "$output_file"

# # Execute Python files in the 'copilot' folder
# echo "Executing Python files in the 'copilot' folder..."
# execute_python_files "copilot" "$output_file"

# echo "Execution times saved to '$output_file'"

#---------------------------------------------------------------------------------
#!/bin/bash

# Function to execute Python files and measure energy consumption
execute_python_files() {
    local folder="$1"

    # Loop through each Python file in the specified folder
    for file in "$folder"/*.py; do
        # Get the name of the Python file
        filename=$(basename "$file")

        # Measure energy consumption
        energy=$(perf stat -e power/energy-pkg/ python3 "$file" 2>&1 | grep "Joules" | awk '{print $1}')

        # Print energy consumption
        echo "$filename: $energy Joules"
    done
}

# Main script
echo "Energy consumption for Python files in the 'codex' folder:"
execute_python_files "codex"

echo "Energy consumption for Python files in the 'copilot' folder:"
execute_python_files "copilot"


sudo powermetrics --samplers cpu_power
python3 Copilot/editDistance.py
sudo powermetrics --samplers cpu_power

