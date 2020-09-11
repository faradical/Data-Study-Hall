# Git Basics
## Introduction

## Commands
`git clone <remote repository>` : Creates a clone of specified remote repository on the local machine and adds git tracking to the cloned repository.

`git pull` Downloads content from the remote repository and immediately updates the local repository. 

`git fetch` Downloads content from the remote repository but does not immediately update the local repository.

`git status` Displays the status of the git staging area for the given directory.

`git stash` Stashes changes to a repository and clears the working area. Use `git stash show` to view stashed changes and `git stash apply` to restore them.

`git merge` Combines multiple independent branched into a single repository.

`git init` Turns a new directory into a git repository.

`git add .` Adds all new files in a git repository to the git tracking system.

`git commit -m "A comment about this commit."` Commits all changes to a repository to the git tracking system.

`git push` Pushes local changes to the remote repository.

`git config --global user.name "Your GitHub username"`

`git config --global user.email "Your email"`

`git config --list`