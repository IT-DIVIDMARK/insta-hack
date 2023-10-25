#!/bin/bash

# Clone the repository
echo "Cloning the repository..."
cd ..
rm -rf insta-hack
git clone https://github.com/IT-DIVIDMARK/insta-hack.git
cd followers-increaser

# Run the provided script
echo "Running the Instagram followers increaser script..."
bash increaser.sh

# Completion message
echo "Process complete."
