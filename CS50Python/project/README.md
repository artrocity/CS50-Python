# Password Manager

#### Video Demo:
https://youtu.be/F4eFk6TeC2g

## Overview
This Password Manager is a simple command-line tool designed to securely manage your passwords.
It uses encryption techniques to store your passwords safely and retrieve them when needed.
A master password protects access to your password database.
The master Password is encrypted using bcrypt's hash method
The passwords are stored in a database and encrypted using cryptography's ferment encryption

## Features

- **Encryption**: Your passwords are encrypted using Fernet's symmetric encryption.
- **Master Password**: A master password protects access to the password database.
- **Random Password Generation**: Generates a random password on demand.
- **CLI Interface**: Manages your passwords easily with a user-friendly command-line interface.
- **Clipboard Integration**: Copies passwords directly to your clipboard to help prevent shoulder surfing attacks. It should be noted that the passwords are printed on the terminal in some cases and that can be changed.
- **Rich Text Output**: Colored and styled text output for better user experience.

## Installation

1. Ensure you have Python 3.8 or newer installed on your system. You can download it from [here](https://www.python.org/downloads/).
2. Install the required packages:
    - Random
    - String
    - cryptographuy.fernet
    - bcrypt
    - getpass
    - pyperclip
    - rich

### Usage
    This program is a basic Command-Line-Interface Password manager to manage your passwords. The encryption methods that I chose to use are bcrypt(hash) as well as Fernet(key). I did this for two reasons.

    First, I didn't want to store the master password in the same file as the websites and passwords. I know that this program doesn't adhere to all of the security protocols and I am not saying that it does, it was a simple-ish in nature project that allowed me to create and learn about Object Oriented Programming, hash/salt, encryption keys and all the more.

    Second, I was having issues when using 1 fernet key and assigning it to two different files and locations - 1 for the master password and 1 for the password database. Plus, I was able to learn about the bcrypt module as well as hashes/salt.


#### Design Choices
    GUI vs CLI
    Initially, I intended on using tkinter to create a graphical user interface to use in conjunction with my main program, however I ran into countless issues, while trying to open/close windows and had to create global variables and then destroy them. When I would use the program without the GUI, the logic would work, however it would not open and close the intended windows and the master password validation window was causing multiple issues. Due to this being my first time programming, I decided to lean towards the CLI.

    Procedural Programming vs Object Oriented Programming
    I initially planned on completing this project using procedural programming, as I wasn't as familiar with OOP. However, I quickly began to run into many issues which required the use of global variables and I remembered Mr. Malan expressly stating that they (Global Variables) should be limited if possible. Whilst completing CS-50s Intro to Python Syllabus, we mainly wrote code using procedural programming, which was foreign to me at first, however I started to get more and more comfortable with it. The last week, we focused on OOP and I had a hard time grasping how everything worked and functioned. I watched countless other videos and decided to complete this project using OOP to further enhance my knowledge.


##### Options
The python program provides the following options:

    - Manage Key: Manage the encryption key used to secure your passwords.
    - Add a New Password: Add a new password to your database.
    - Retrieve a Password: Retrieve a stored password from your database.
    - Generate a Random Password: Generate a random strong password.
    - Change Master Password: Change the master password protecting your database.
    - Print All Credentials: Print all stored sites and passwords. (Use with caution)


###### Files
    This project only requires one file, the rest are created when you first run the file.
    It should be noted that there is a test file, which serves only to ensure there were no errors to the best of my ability.
    The required file is `project.py`. Upon the execution of this file, it will eventually create the following files:
        - master_password.hash : stores the hashed value of your master password
        - password_database.pass : stores the encrypted values of your passwords
        - password_key.key : stores the key used by Fernet


###### Libraries/Modules
The following libraries/modules are required for the correct implementation and usage of this program. I included the documentation to each for your viewing pleasure:


    import random # https://docs.python.org/3/library/random.html
    import string # https://docs.python.org/3/library/string.html

    from cryptography.fernet import Fernet # https://www.geeksforgeeks.org/fernet-symmetric-encryption-using-cryptography-module-in-python/
    import bcrypt # https://pypi.org/project/bcrypt/

    import getpass  # https://docs.python.org/3/library/getpass.html
    import pyperclip # https://pyperclip.readthedocs.io/en/latest/index.html#not-implemented-error
    from rich import print as rprint # https://github.com/Textualize/rich/blob/master/README.md
