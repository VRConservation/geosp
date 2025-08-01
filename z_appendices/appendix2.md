# Visual Studio Code

Get your integrated development environment set up to code.

## Installation

[Visual Studio Code](https://code.visualstudio.com/) is a powerful open-source code editor. There are other integrated development environments (IDEs) such as Pycharm or Spyder (comes with Anaconda), so choose the one that's best for you. Note that if you only use R, RStudio comes with an integrated terminal and IDE so you can solely work within RStudio. If you use multiple languages, however, VS Code is fantastic, used by many (so it makes tutorials and learning new packages or languages easier), and it has many plugins to make it easy to use.

Visual Studio Code has great documentation and setup tutorials so that we won't explore those here. Download VS Code for your OS and open it. On the left-hand pane, there is an icon with 4 squares for extensions. Click on that to open it and install and activate the following extensions (use the search box at the top of the extension pane to find each extension):

1. Bracket Pair Color DLW
2. autoDocstring
3. Code Spell Checker
4. CodeSnap
5. GitHub Actions, GitHub Pull Requests, and GitHub Repositories
6. GitLens
7. Highlight Matching Tag
8. indent-rainbows
9. Jupyter
10. Prettier
11. Python

Optional extensions include github copilot (requires a subscription) and chatgpt (requires a subscription for some versions). I highly recommend considering copilot as the chat and autocomplete, for it often suggests code that works or can help you resolve errors in your code when searches or your own editing don't work. It will also greatly speed up the process of producing code and seems to be improving rapidly. Copilot is free to students and possibly free through select nonprofit organizations.

```{tip}
Run jupyter notebooks in your browser by navigating to the file where you want to run the notebooks or have existing notebooks. Right click on a blank space in the file navigator then select Open in Terminal. Enter `conda activate yourenv` substituting yourenv for your virtual environment name. Then run `jupyter lab`. This will open a locahost window in your default web browser where you can edit existing or open new notebooks.
```

## Environment Variables Setup

In many cases VS Code isn't properly set up with the terminal, usually in Windows. Open the terminal by clicking the Terminal Window in the top bar of VS Code and select 'New Terminal'. In the command line, enter `conda`. If you get a red error message, follow these steps:

1. Click the windows button on your computer, type 'env,' and select 'Edit the System Environment Variables'.
2. In the system properties window, select 'Environment Variables'
3. In the Environment Variables window under 'System variables', double click 'Path'
4. In the Edit environment variable window, you should have a variable called 'C:\Users\yourusername\anaconda3\Scripts\conda.exe'. anaconda3 may be replaced by miniconda if you installed miniconda.
5. If that doesn't exist, open internet explorer and go to the Scripts file:
   1. Select 'This PC' in the left pane of explorer
   2. Open 'Users'
   3. Open your username file, likely your first name
   4. Scroll down and open miniconda or anaconda3 (don't open the files such as .anaconda; keep scrolling until you find the file)
   5. Open 'Scripts'
   6. Find the conda.exe file. It could appear solely as 'conda'. Right-click on the file and select 'Copy as path'.
   7. Go back to the Edit environment variable, double-click at the bottom, and then type control V on your keyboard to paste the conda file path into the variables. Ok, your way out of each of the open windows.
   8. Close Visual Studio Code
6. Open the VS Code and type the conda into the terminal. You should no longer get an error.
7. What a pain in the butt! To watch how to do this, go to ~ minute 34:20 of the [Introducing Visual Studio Code](https://www.youtube.com/watch?v=MDtlHMQi7uk&t=2264s) video from Open Geospatial Solutions. The fix might convince you to switch to a linux OS where none of this configuration faffing is necessary!
