# Define the available resources
available = [3, 3, 2]

# Define the maximum demand for each process
maximum = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]

# Define the allocation for each process
allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]

# Define the need for each process
need = [[7, 4, 3], [1, 2, 2], [6, 0, 0], [0, 1, 1], [4, 3, 1]]

# Define the list of processes
processes = [0, 1, 2, 3, 4]

# Define a list to keep track of finished processes
finished = [False] * len(processes)

# Define a list to keep track of the safe sequence
safe_sequence = []

# Loop until all processes have finished or a deadlock is detected
while False in finished:
    # Assume deadlock
    deadlock = True
    
    # Loop through each process
    for i in processes:
        # Check if the process is not finished and its need can be satisfied
        if not finished[i] and all(j <= available[idx] for idx, j in enumerate(need[i])):
            # Mark the process as finished
            finished[i] = True
            
            # Add the allocated resources back to the available resources
            available = [sum(x) for x in zip(available, allocation[i])]
            
            # Add the process to the safe sequence
            safe_sequence.append(i)
            
            # Reset the deadlock flag
            deadlock = False
            
    # If deadlock is detected, break out of the loop
    if deadlock:
        break

# If all processes have finished, print the safe sequence
if len(safe_sequence) == len(processes):
    print("Safe sequence:", safe_sequence)
# If a deadlock was detected, print an error message
else:
    print("Deadlock detected")
