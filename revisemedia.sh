#!/bin/bash

# Change to the 'media' directory
cd media

# Loop through all files in the directory
for file in *; do
    # Check if the file matches the pattern
    if [[ $file =~ ^(.*)\.[^.]{5,}$ ]]; then
        # Rename the file by removing the trailing characters
        mv "$file" "${BASH_REMATCH[1]}"
    fi
done
