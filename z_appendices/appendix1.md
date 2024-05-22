# Appendix 1: venv
Getting your virtual environment set up

## Installation
Installation instructions are for a PC, but Mac and Linux are similar but probably much easier than windows.

1. [Install](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) conda by downloading miniconda or anaconda for your os. The documentation provides an overview of which package will work for you. I installed anaconda but almost never use the navigator that comes with the larger package, using the conda command interface to install everything. This would imply I need to install miniconda, the minimal installer, but I was never able to make it work on my machine.
2. Open the conda command prompt by clicking the windows button and typing anaconda or miniconda then selecting the prompt. You should see the following

```
(base) C:\Users\yourusername>
```

If you don't see this in the command prompt (also known as command line interface or CLI), try going to your Users\username file right clicking in the file and selecting 'open in terminal' and follow the instructions below. If the windows powershell gives you an error or conda won't work see [this](http://gg.gg/1av2oy) video to fix the issue.

Note that you hit enter after typing or pasting every command into the terminal.

3. Create a conda environment. It's preferable to create a new environment for each project or set of tasks you complete to avoid conflicts between packages. We'll call this one 'geo' but name it whatever you like, making sure to use a short 3-4 letter abbreviation or name. 

When the terminal says ```Proceed ([y]/n)?``` hit enter or type y and enter to create the environment. When finished you'll get a message about activate or deactivate the env using the command line.

```
conda create -n geo python
```

Note this will install the latest version of Python on your computer. Sometimes that can create incompatibilities with the software packages you install since they may not be synced with this version of Python. It's safer to specific the previous version of Python. In other words if the latest release is 3.13, install 3.12. to do this alter your environment creation commands to the latest version minus 0.01, in this case 3.12 if the latest is 3.13.

```
conda create -n geo python=3.12
```

4. Activate the new environment. 

```
conda activate geo
```

The command line will change to

```
(geo) C:\Users\yourusername>
```
You can also check the environment is active by entering ```conda env list```. You should see an asterisk next to the environment you installed and a pathway on the drive to that environment. If you activate base the asterisk will go to the base environment.

The command `conda list` will show the packages installed in the active environment. You should see python and the version installed. Use the command `cls` to clear the screen.

6. Install geemap. You can do this directly in conda, but it can be slow. Installing mamba speeds up this process. Mamba is a drop-in replacement for conda that is faster and better at resolving package dependencies:

```
conda install -c conda-forge mamba
```
This will take a while but hit enter once it asks you to proceed. Once installed you can install geemap:

```
mamba install -c conda-forge geemap
```

Alternatively you can install a suite of commonly used packages for geospatial analysis using [geospatial](https://geospatial.gishub.org/)

## Github

## Anaconda
