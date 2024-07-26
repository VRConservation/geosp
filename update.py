import os
import subprocess

# Save the original directory
orig_dir = os.getcwd()

# Define folder paths and create a list of the folders
bibtest = 'D:/OneDrive/1_Consulting/Spatial/geosp-bibtest'
chapters = 'D:/OneDrive/1_Consulting/Spatial/geosp-bibtest/chapters'
appendices = 'D:/OneDrive/1_Consulting/Spatial/geosp-bibtest/z_appendices'

folders = [bibtest, chapters, appendices]

# Loop through the folders and run the command 'jupytext --sync *.ipynb'
for folder in folders:
    os.chdir(folder)
    subprocess.run(["jupytext", "--sync", "*.ipynb"], check=True)
    os.chdir(orig_dir)  # go back to the bibtest folder

# Run the command jb build --all . after the loop
subprocess.run(["jb", "build", "--all", "."], check=True)

# run the ghp-import -n -p -f _build/html
subprocess.run(["ghp-import", "-n", "-p", "-f", "_build/html"], check=True)

# Push and sync the repository to GitHub
subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", "sql ucb db file updates"], check=True)
subprocess.run(["git", "push"], check=True)

# run the script in the terminal with the command python update.py