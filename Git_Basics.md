# Git Basics
![git logo](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.fullstackpython.com%2Fgit.html&psig=AOvVaw3ejs4xqBG5m27jqorOH7lb&ust=1602961909025000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCLDI1oDpuewCFQAAAAAdAAAAABAD)
## Introduction
Git is a VCS, or Version Control System. It allows us to to track changes to files, restore previous versions, collaborate with others, and create CI/CD pipelines for code deployment.

A presentation on Git can be accessed [here](https://docs.google.com/presentation/d/1T8kM0VriITsiH18DNoeZJCs2gCxvU-lHkgyFM3cTJis/edit?usp=sharing)

## Commands
`git clone <remote repository>` : Creates a clone of specified remote repository on the local machine and adds git tracking to the cloned repository.

`git pull` Downloads content from the remote repository and immediately updates the local repository. 

`git fetch` Downloads content from the remote repository but does not immediately update the local repository.

`git status` Displays the status of the git staging area for the given directory.

`git stash` Stashes changes to a repository and clears the working area. Use `git stash show` to view stashed changes and `git stash apply` to restore them.

`git merge` Combines multiple independent branches into a single repository.

`git init` Turns a new directory into a git repository.

`git add .` Adds all new files in a git repository to the git tracking system.

`git commit -m "A comment about this commit."` Commits all changes to a repository to the git tracking system.

`git push` Pushes local changes to the remote repository.

`git config --global user.name "Your GitHub username"`

`git config --global user.email "Your email"`

`git config --list`