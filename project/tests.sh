#!/bin/bash

# Set the script to exit
set -e

# Change the directory to project
cd "$(dirname "$0")"

# Run the test script
py test.py


echo "All tests passed (Final test)"