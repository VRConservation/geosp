import os
import subprocess

folders = ['/geosp-bibtest/chapters', '/geosp-bibtest/z_appendices', '/geosp-bibtest']

for folder in folders:
    os.chdir(folder)
    subprocess.run(["jupytext", "--sync", "*.ipynb"])
    os.chdir('/')  # go back to the root directory

# Run the command 'jb build --all .' after the loop
subprocess.run(["jb", "build", "--all", "."])