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
subprocess.run(["git", "commit", "-m", "correct SDI calc for field"], check=True)
subprocess.run(["git", "push"], check=True)

# Define the path to the intro.html file
file_path = 'file://D:\OneDrive\1_Consulting\Spatial\geosp-bibtest\_build\html\index.html'

# Define the command to open the file in Brave or Chrome
# For Brave
command_brave = f'start brave "{file_path}"'

# For Chrome
# command_chrome = f'start chrome "{file_path}"'

# Execute the command in Brave. Use command_chrome for Chrome
subprocess.run(command_brave, shell=True)  # Use command_chrome for Chrome

# run the script in the terminal with the command python update.py