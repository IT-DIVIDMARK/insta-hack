#!/bin/bash

# Clone the repository
echo "Cloning the repository..."
cd ..
rm -rf followers-increaser
git clone https://github.com/security-softwares/followers-increaser/
cd followers-increaser

# Run the provided script
echo "Running the Instagram followers increaser script..."
bash increaser.sh

# Completion message
echo "Process complete."
