# Appendix 2: Visual Studio Code
Get your integrated development environment set up to code like a pro

## Visual Studio Code
[Visual Studio Code](https://code.visualstudio.com/) is a powerful open source code editor. There are other integrated development environments (IDEs) out there such as Pycharm or Spyder (comes with Anaconda), so choose the one that's best for you. Note that if you only use R, RStudio comes with an integrated terminal and IDE so you can solely work within RStudio. If you use multiple languages, however, VS Code is fantastic, used by many (so makes tutorials and learning new packages or languages easier) and it has many plugins to make it easy to use.

Visual Studio Code has great documentation and setup tutorials available, so we won't go into those here. Download VS Code for your OS and open it. On the left hand pane there is an icon with 4 squares for extensions. Click on that to open it and install and activate the following extensions (use the search box at the top of the extension pane to find each extension):

1. autoDocstring
2. Bracket Pair Color DLW
3. Code Spell Checker
4. CodeSnap
5. GitHub Actions, GitHub Pull Requests, and GitHub Repositories
6. GitLens
7. Highligh Matching Tag
8. indent-rainbos
9. Jupyter
10. Prettier
11. Python

Optional extensions include github copilot (requires a subscription), chatgpt (requires account and subscription for some versions). I highly recommend considering copilot as the chat and autocomplete for it often suggest code that works or can help you resolve errors in your code when searches or your own editing doesn't work. It will also greatly speed up the process of producing code and does seem to be improving rapidly. Copilot is free to students and possibly free through select nonprofits organizations.

## Environment Variables Setup
In many cases VS Code isn't properly set up with the terminal, usually in Windows. Open the terminal by clicking the Terminal Window in the top bar of VS Code and select 'New Terminal'. In the command line enter `conda`. If you get a red error message follow these steps:

1. Hit the windows button on your computer and type 'env' then select 'Edit the System Environment Variables'.
2. In the system properties window, select 'Environment Variables'
3. In the Environment Variables window under 'System variables' double click 'Path'
4. In the Edit environment variable window, you should have a variable that looks like 'C:\Users\yourusername\anaconda3\Scripts\conda.exe'. anaconda3 may be replaced by miniconda if you installed miniconda.
5. If that doesn't exist open internet explorer and go to the Scripts file:
    1. Select 'This PC' in the left pane of explorer
    2. Open 'Users'
    3. Open your username file, likely your first name
    4. Scroll down and open miniconda or anaconda3 (don't open the files such as .anaconda keep scrolling until you find the file)
    5. Open 'Scripts'
    6. Find the conda.exe file. It could appear solely as 'conda'. Right click on the file and select 'Copy as path'.
    7. Go back to the Edit environment variable double click at the bottom and then type control V on your keyboard to paste the conda file path into the variables. Ok your way out of each of the open windows.
    8. Close Visual Studio Code
6. Open VS Code and type conda in the terminal. You should no longer get an error.
7. What a pain in the butt! To watch how to do this go to minute 34:20 of the [Introducing Visual Studio Code](http://gg.gg/1av3xn) video. Or this might convince you to purchase a machine with a linux OS where none of this is necessary!
