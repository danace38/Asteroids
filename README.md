# Asteroids
This is a Python implementation of a simple Asteroids game, inspired by a version of the original concept: [Asteroids by eChalk](https://www.echalk.co.uk/amusements/Games/asteroidsClassic/ateroids.html)

# Video Walkthrough
Here's a walkthrough of the Asteroids game:
![Asteroids_BootDev](https://github.com/user-attachments/assets/b3cc89fc-cb27-4ce8-aeb7-df49395d4f80)

# Features 
* A player-contolled ship
* Asteroids that need to be avoided or destroyed
* Shooting mechanism
* Movement mechanism for the player (e.g., W-up, S-down, A-left, D-right)
* Award points for destroying asteroids (5 points for big asteroids, 3 points for medium asteroids and 1 point for small asteroids)
* Tracking system for total of destroyed asteroids

# Prerequisites

In order to run the game on your local machine, you will need the following:

* Python 3.10+ installed
* [Pygame](https://www.pygame.org/news) module
* Virtual Environment (venv)
* (Optional) Install [The Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install) in order to access a unix-like shell (e.g. zsh or bash)

**Note**: As a best practice, each Python project on your machine should have its own virtual environment to keep them isolated from each other.

# Instructions

* Copy the project repository to your local machine using CLI (I recommend using [VS Code](https://code.visualstudio.com/))
```
git clone https://github.com/danace38/Asteroids.git
```
* Create a virtual environment at the top level of the project directory
```
python3 -m venv venv
```
* Activate the virtual environment
```
source venv/bin/activate
```
**Note**:

You should see **(venv)** at the beginning of your terminal prompt, for example, mine is:
```
(venv) danace38@MyPC:~/workspace/asteroids$
```

* Install the requirements that are specified in **requirements.txt** file by running this command
```
pip install -r requirements.txt
```
* Make sure pygame is installed
```
python3 -m pygame
```
**Keep in mind:**

If you decided to install WSL, you will probably need to install [VcXsrv](https://vcxsrv.com/) to run pygame.

# Executing the program
* Run **main.py** inside the projects repository
```
python3 main.py
```
# Contributing
Found a typo in the documentation or interested in contributing to this project? Then by all means [submit an issue](https://github.com/danace38/Asteroids/issues) or [pull request](https://help.github.com/articles/using-pull-requests/). 

# Acknowledgments

The project has been completed as part of [Boot.dev](https://boot.dev)
curriculum.

# License
 This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
