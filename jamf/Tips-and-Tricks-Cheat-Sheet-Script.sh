#!/bin/bash
# Tips and Tricks Cheat Sheet Script
# This script displays a cheat sheet with helpful tips for macOS users

# Variables
cheatSheetPath="/path/to/cheat-sheet.txt"

# Display cheat sheet
displayCheatSheet() {
    # Check if the cheat sheet file exists
    if [[ -f "$cheatSheetPath" ]]; then
        # Use 'less' to display the cheat sheet file with pagination
        less "$cheatSheetPath"
    else
        echo "Cheat sheet file not found."
    fi
}

# Main
echo "Displaying tips and tricks cheat sheet..."
displayCheatSheet
echo "Cheat sheet display completed."
