#!/bin/bash

# Check if the directory path argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <log_directory>"
    exit 1
fi

# Assign the directory path argument to a variable
log_dir="~/nfs/timing/$1"

# Create the directory if it does not exist on the local machine
mkdir -p "$log_dir"

# Loop over the range of nodes
for n in {0..29}; do
    ssh scc124-cpu$n "mkdir -p ~/nfs/timing/$1 && fping -f /home/rocky/nfs/timing/hosts.txt -c 1 -p 10 -q > ~/nfs/timing/$1/\$(hostname).log 2>&1" &
done

# Wait for all background SSH commands to complete
wait

echo "All fping commands completed in parallel. Logs saved to ~/nfs/timing/$1."

