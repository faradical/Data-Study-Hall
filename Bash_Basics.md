# Bash:
## Unix Essentials
On a unix or Linux system, everything is either a file, which exists on the hard drive, or a process, which is executed on the processor. Bash, the Boure Again SHell, is the "language" we use to communicate with the OS on a Unix sytem. While Mac, which is inherently a Unix system, has the Terminal application to run Bash in, Windows requires an application that can replicate a Unix style system for us to use. This course uses GitBash to fulfill that role.

## Bash Commands:
`mkdir <directory name>` Creates a new directory.

`cd <path/to/directory>` CD (Change Directory) moves the prompt to the target directory.

`touch <file name>` Creates a new file.

`ls` and `ls -al` Lists files in a directory. The `-al` flag shows all hidden files (the 'a' flag) and in the long form (the 'l' flag).

`cp [option] <path/to/source> <path/to/destination>` The copy command.

`mv [option] <path/to/source> <path/to/destination>` The move command. Can also be used to rename files by moving them within the smae directoy under a new name.

`cat <file name>` Cat, or Concatenate, has a deceptively extensive use. It's primary purpose is to display file contents, but can be combined with the redirect or pipe to combine, or concatenate, files.

`pbcopy` On Mac, allows content to be copied to the clipboard.

`clip` On Windows, allows content to be copied to the clipboard.

`code <file name>` Opens a new file in Visual Studio Code.

`open <file name>` and `open -a <Application name> <file name>` On Mac, allows you to open a folder or file from the terminal.

`explorer <file name>` On Windows, allows a Windows File Explorer window to be opened in the specified directory.

## Sudo vs. Admin
`sudo` (mac) vs. open as admin (windows).

## Scripting (write file, chmod +x or chmod 777, ./file.sh)