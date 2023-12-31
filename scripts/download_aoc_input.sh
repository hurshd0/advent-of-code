#!/bin/bash

# Script to download Advent of Code input data for a specific day
# Use firefox or chrome to get the session cookie, and pass it as an argument to this script.
# Usage: ./download_aoc_input.sh <year> <day>

# Check if all required arguments are provided
if [ "$#" -lt 2 ] || [ "$#" -gt 3 ]; then
    echo "Usage: $0 <year> <day> [output_folder]"
    exit 1
fi

# Load .env file from current or parent directory if it exists
if [ -f .env ] || [ -f "../.env" ]; then
    source "${BASH_SOURCE%/*}/.env" || source "${BASH_SOURCE%/*/*}/.env"
    echo "Loaded .env file"
else
    echo "No .env file found in the current or parent directory."
    exit 1
fi

if [ -z "$SESSION_COOKIE" ]; then
    echo "SESSION_COOKIE is missing. Please add the SESSION_COOKIE in .env file"
    exit 1
fi

year=$1
day=$(echo "$2" | sed 's/^0*//')  # Removing leading zeros
session_cookie=$SESSION_COOKIE
output_folder=${3:-"."}  # Default to current directory if no output folder is provided

# Create URL for fetching input data
url="https://adventofcode.com/${year}/day/${day}/input"

# Perform a HEAD request to get HTTP status code
http_status=$(curl -s -b "session=${session_cookie}" -o /dev/null -w "%{http_code}" "$url")

# Check HTTP status code
if [ "$http_status" -eq 200 ]; then
    # Download input data using curl to the specified output folder
    curl -s -b "session=${session_cookie}" "$url" > "${output_folder}/day${day}_input.txt"
    
    # Check if download was successful
    if [ $? -eq 0 ]; then
        echo "Input data for day ${day} of year ${year} downloaded successfully."
    else
        echo "Failed to download input data for day ${day} of year ${year}. Please check your session cookie and try again."
    fi
else
    echo "Failed to fetch input data for day ${day} of year ${year}. HTTP status code: ${http_status}"
fi