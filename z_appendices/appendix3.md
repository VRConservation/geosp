# Github
Install Git, Github, and connect your local computer to remote repos.

## Create a new repository on GitHub

1. Go to GitHub and log in to your account.
2. Click on the '+' icon in the upper right corner and select 'New repository'.
3. Name your repository, add a description (optional), and choose to make the repository either public or private.
4. You can initialize the repository with a README, .gitignore, or license if you want.
5. Click 'Create repository'.

## Connect the repository to a local directory

1. Open the terminal on your computer.
2. Use the' cd' command to navigate to the directory where you want to clone the repository. For example, if you want to clone the repository to a directory named 'my_directory' on your C drive, you would use the command `cd C:/my_directory`. You can also navigate to the file location, right-click in a blank space, and select 'open in terminal'. Make sure to activate the correct environment for the project.
3. Clone the repository by running the command `git clone https://github.com/username/repository.git`, replacing 'username' with your GitHub username and 'repository' with the name of your repository. This will create a new directory in 'my_directory' with the same name as your repository, and this new directory will be linked to the repository on GitHub.
4. Navigate into the new directory with the command `cd repository`, replacing 'repository' with the name of your repository.

## Push changes to GitHub

1. Make any changes you want in the new directory.
2. Once done, you can add these changes to the staging area with the command `git add .`.
3. Commit the changes with the command `git commit -m "Your commit message"`, replacing 'Your commit message' with a brief description of your changes.
4. Push the changes to GitHub with the command `git push origin master`.
Please note that you need to have Git installed on your computer to use the git command. If you don't have Git installed, you can download it from the Git website.

## Clone an existing repo
1. Find the repository on GitHub
    1. Go to GitHub and log in to your account.
    2. Navigate to the repository you want to clone.

2. Copy the github URL
    1. In the repo, click the 'green `<> Code` button near the top of the repository's page.
    2. In the dropdown that appears, click copy the repository's URL to your clipboard.

3. Open the terminal on your computer.
    1. In a terminal, navigate to the directory where you want to clone the repository using the `cd` command. For example, if you want to clone the repository to a directory named 'my_directory' on your C drive, you would use the command `cd C:/my_directory`.
    2. An easier way to the correct directory is to open the directory in your file explorer, right-click on a space in the directory, and select open in terminal.  
    3. Clone the repository by running the command `git clone https://github.com/username/repository.git`, replacing 'https://github.com/username/repository.git' with the URL you copied in step 1. This will create a new directory in 'my_directory' with the same name as your repository, and this new directory will be linked to the repository on GitHub.

## Clone a repo in VS Code
1. Open VS Code
2. Open the command palette by typing `Ctrl+Shift+P`
3. Type `Git: Clone` and select it from the dropdown list
4. Paste the repo URL you want to clone and click enter
5. Choose the directory where you want to store the repo on your computer
6. Click `Open` to open the repo in a new window or `Add to Workspace` to add it to the workspace you are working in.

## Git init
You need to initialize Git in each new project you want to control version. You do this by navigating to your project's directory in the terminal and running the command git init. This creates a new Git repository in the current directory.

For example, if you have a project in a directory named 'my_project' on your C drive, you would initialize Git in this project with the following commands:

```
cd C:/my_project
git init
```
After running these commands, you'll see the message "Initialized empty Git repository in C:/my_project/.git/". This means that Git has been initialized in the 'my_project' directory, and you can now use Git commands to track changes to your project.

## Push changes in VS Code
To save your local changes in VS Code and 'push' them to your remote repo, follow these steps:
1. Edit your files and save the changes.
2. Click on the Source Control icon in the Activity Bar on the side or press `Ctrl + Shift + G` to open the Source Control panel.
3. Click the '+' icon next to each file you want to stage, or click the '+' icon at the top to stage all changes.
4. In the text box at the top of the Source Control panel, enter a commit message and press `Ctrl + Enter` to commit the changes.
5. Click on the '...' icon at the top of the Source Control panel and select 'Push' from the dropdown menu.
6. Select sync from the blue button.

## Push changes using Git
Or you can push changes in the terminal using Git:
1. Make sure you're in the correct repo and env in your terminal. Use the `cd` command to change directories, e.g., `cd C:\my_project`
2. Stage changes using the command `git add .` to stage all the repo changes.
3. Commit changes using the command `git commit -m 'your commmit message'. Make sure to change the commit message in quotes to reflect what changes you made.
4. Push the changes using `git push origin master, ' sending them to the master branch of the remote repo.

This will look like the following, where you enter each line and hit enter separately:

```
cd C:/my_project
git add .
git commit -m "Your commit message"
git push origin master
```
