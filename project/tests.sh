#!/bin/bash

# Set the script to exit
set -e

# Change the directory to project
cd "$(dirname "$0")/project"

# Run the test script
py project/test.py


echo "All tests ran successfully!"