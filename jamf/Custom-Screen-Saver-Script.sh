#!/bin/bash
# Custom Screen Saver Script
# This script sets a custom screen saver with a user-defined message

# Variables
customMessage="Welcome to our company!"
plistPath="/Users/$USER/Library/Preferences/ByHost/com.apple.screensaver.$(scutil --get LocalHostName).plist"

# Set custom screen saver
setCustomScreenSaver() {
    # Update message in the plist file
    defaults write "$plistPath" MESSAGE "$customMessage"

    echo "Custom screen saver set with the message: '$customMessage'."
}

# Main
echo "Setting custom screen saver..."
setCustomScreenSaver
echo "Custom screen saver configuration completed."
