#!/bin/bash


# Import Functions & Variables
source "./00-Functions-resolve-installer.sh"

### general variables ###
#resolve_luts
#resolve_transitions
#fusion_scripting

# Getting Resolve and Fusion install packages
grab_blackmagic_packages

# Ask the user to select the app to install
selectedApps=$(zenity --list --checklist --column "Select" --column "Item" \
              TRUE "Fusion" \
              TRUE "Resolve" \
              --separator=":" --title "Installation" --text "Select app(s) to install")

              
# INSTALL libraries
#install_libs

# Install logic for the apps Resolve and/or Fusion
#install_apps

#test_code

pause_script_keyboard_feedback
