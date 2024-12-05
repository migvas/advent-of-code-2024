#!/bin/bash

# Check if an argument is passed
if [ -z "$1" ]; then
  echo "Usage: $0 <number>"
  exit 1
fi

# Get the input number
DAY_NUMBER=$1

# Create the folder with the name day + day number
FOLDER_NAME="day${DAY_NUMBER}"
mkdir -p "$FOLDER_NAME"

# Create the files inside the folder
touch "$FOLDER_NAME/test_data.txt" "$FOLDER_NAME/input.txt" "$FOLDER_NAME/$FOLDER_NAME.py"

echo "Day $DAY_NUMBER files created successfully."
