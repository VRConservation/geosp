import os
import subprocess

# Save the original directory - use the script's directory as the base
script_dir = os.path.dirname(os.path.abspath(__file__))
orig_dir = script_dir

# Define folder paths and create a list of the folders
bibtest = r'D:\OneDrive\1_Consulting\Spatial\geosp'
chapters = r'D:\OneDrive\1_Consulting\Spatial\geosp\chapters'
appendices = r'D:\OneDrive\1_Consulting\Spatial\geosp\z_appendices'

folders = [bibtest, chapters, appendices]

# Loop through the folders and run the command 'jupytext --sync *.ipynb'
for folder in folders:
    print(f"Processing folder: {folder}")
    try:
        # Run jupytext with the folder as working directory without changing the script's cwd
        result = subprocess.run("jupytext --sync *.ipynb", shell=True,
                                check=True, capture_output=True, text=True, cwd=folder)
        print(f"Success in {folder}")
        if result.stdout:
            print(f"Output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error in {folder}: {e}")
        if e.stdout:
            print(f"Stdout: {e.stdout}")
        if e.stderr:
            print(f"Stderr: {e.stderr}")

# Run the command jb build --all . after the loop
subprocess.run(["jb", "build", "--all", "."], check=True)

# run the ghp-import -n -p -f _build/html
subprocess.run(["ghp-import", "-n", "-p", "-f", "_build/html"], check=True)

# Push and sync the repository to GitHub
subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", "Intro chapter first para error sync"], check=True)
subprocess.run(["git", "push"], check=True)

# Define the path to the intro.html file
file_path = r'D:\OneDrive\1_Consulting\Spatial\geosp\_build\html\index.html'

# Define the command to open the file in Brave or Chrome
# For Brave
command_brave = f'start brave "{file_path}"'

# For Chrome
# command_chrome = f'start chrome "{file_path}"'

# Execute the command in Brave. Use command_chrome for Chrome
subprocess.run(command_brave, shell=True)  # Use command_chrome for Chrome

# run the script in the terminal with the command python update.py
