import os
import subprocess

# Save the original directory
orig_dir = os.getcwd()

# Define folder paths and create a list of the folders
bibtest = 'C:/Users/vance/Downloads/geosp-bibtest'
chapters = 'C:/Users/vance/Downloads/geosp-bibtest/chapters'
appendices = 'C:/Users/vance/Downloads/geosp-bibtest/z_appendices'

folders = [bibtest, chapters, appendices]

# Loop through the folders and run the command 'jupytext --sync *.ipynb'
for folder in folders:
    os.chdir(folder)
    subprocess.run(["jupytext", "--sync", "*.ipynb"], check=True)
    os.chdir(orig_dir)  # go back to the bibtest folder

# Run the command jb build --all . after the loop
subprocess.run(["jb", "build", "--all", "."], check=True)

# # run the ghp-import -n -p -f _build/html
# subprocess.run(["ghp-import", "-n", "-p", "-f", "_build/html"], check=True)

# # Push and sync the repository to GitHub
# subprocess.run(["git", "add", "."])
# subprocess.run(["git", "commit", "-m", "Update the repository"])
# subprocess.run(["git", "push"])


# run the script in the terminal by with the command python update.py