# Art Intel Computers

### Fairplay
We have three computers for machine learning use. We need to share these three amongst all of us. So here are a few community rules:
- Only use these computers for dedicated machine learning tasks.
- Don't leave finished tasks still running on tmux.
- Move any output files you want to save to your computer and **delete all other generated files** as soon as a task is done.
- Each person will have one computer they are assigned to to use. Please only use the computer you've been assigned to. If that computer is tied up for long periods, but another is free, let me know and we can talk about using a different computer.
- **Only add or change dependencies on your own environment**.
- Check to see if anyone is currently using the computer by checking the tmux sessions (more below).
- Run ALL of your processes in tmux.

### Setup
We'll be using Anaconda to manage our dependencies. I've set up CUDA and Tensorflow already and made a base conda environment for you to build off of. You need to clone this environment into your own personal environment:
- `conda create --name <YOURNAME> --clone tensorflow`

ANy changes to Python version, python libraries, etc. you want to make will happen in your own environment.

### SSH
You can log into your computer remotely via SSH:
- `ssh nyuad@<IPADDRESS>`

### TMUX
We will use tmux for a detachable command line window. tmux commands:
- Check if there is another session running (list sessions): `tmux ls`
- Start a new session: `tmux new -s <YOURNAME>`
- Detach window (while in a session): `ctrl+b` then `d` 
- Reattach to a session: `tmux a -t <NAMEOFSESSION>`
- Kill a session: `tmux kill-session -t <NAMEOFSESSION>`

### SFTP
We'll use SFTP to move files between our computers and the class computers.
- If logged into the class computer, SFTP into your own computer:
  - `sftp <yourusername>@<yourIPADDRESS>`
