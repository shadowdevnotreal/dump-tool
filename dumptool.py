#!/bin/bash

# Check for necessary commands (Zenity and aha) and install or prompt for installation if missing
if ! command -v zenity &> /dev/null; then
    echo "Zenity is not installed. Please install Zenity and try again."
    exit 1
fi

if ! command -v aha &> /dev/null; then
    echo "aha is not installed. Installing..."
    if command -v pip3 &> /dev/null; then
        pip3 install aha
    else
        echo "pip3 is not available. Please install Python3 pip and try again."
        exit 1
    fi
fi

# Function to search for a term in files, using find for recursive search
search_term() {
    local term=$1
    local directory=$2

    echo "Searching in $directory..."
    find "$directory" -type f -exec grep -Hn --color=always "$term" {} \; | GREP_COLORS='mt=01;31' grep --color=always -E "$term|$"
}

# Function to print the banner
print_banner() {
    local banner_text="Dump Search Tool"
    if command -v tput &> /dev/null; then
        local cols=$(tput cols)
    else
        local cols=80 # default width if tput is not available
    fi
    local banner_length=${#banner_text}
    local padding=$(( (cols - banner_length) / 2 ))
    local line=$(printf "%*s" "$cols" | tr ' ' '=')

    echo
    echo "$line"
    printf "%*s\n" $((padding + banner_length)) "$banner_text"
    echo "$line"
    echo
}

# Print welcome message
echo "Welcome to the search tool"

# Select file or folder using Zenity
selection=$(zenity --file-selection --filename="/path/to/folder" --title="Select File or Folder" --multiple --separator='|' --directory)

# Input search term using Zenity
search_term_input=$(zenity --entry --title="Enter Search Term" --text="Enter the search term:")

# Choose whether or not to have colored output
color_output=$(zenity --list --title="Choose Output Color Option" --radiolist --column="Select" --column="Option" TRUE "Colored" FALSE "Plain")

# Input output filename using Zenity
output_filename=$(zenity --file-selection --save --title="Save Output As" --confirm-overwrite)

# Main script
# Print banner
print_banner

# Determine coloring option
color_cmd="cat" # Default to plain text if color is not selected
if [ "$color_output" == "Colored" ]; then
    color_cmd="aha --black"
fi

# Iterate over selected files/folders
IFS='|' read -ra files <<< "$selection"
for item in "${files[@]}"; do
    if [ -f "$item" ]; then
        search_term "$search_term_input" "$(dirname "$item")"
        echo "=============================="
    elif [ -d "$item" ]; then
        search_term "$search_term_input" "$item"
        echo "=============================="
    fi
done | $color_cmd > "$output_filename"

# Option to open the output file in the default web browser
if zenity --question --title="Open Output" --text="Do you want to open the output file now?"; then
    xdg-open "$output_filename"
fi
