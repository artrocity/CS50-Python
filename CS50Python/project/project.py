#Import Modules
import random
import string

from cryptography.fernet import Fernet
import bcrypt

import getpass
import pyperclip
from rich import print as rprint

class PasswordManager:
    def __init__(self, key_path="password_key.key", password_file="password_database.pass", master_password_path="master_password.hash"):
        self.key = None
        self.key_path = key_path

        self.manage_key(self.key_path)
        if self.key is None or len(self.key) !=  44:
            rprint("[yellow]No valid encryption key found, creating a new key now [/yellow]")
            self.key = Fernet.generate_key()
            with open(self.key_path, "wb") as file:
                file.write(self.key)

        self.password_file = password_file
        self.password_dict = {}

        self.master_password = None
        self.master_password_path = master_password_path

        self.load_master_password()
        self.load_passwords()


    #Set Master Password
    def set_master_password(self, master_password):
        hashed_password = bcrypt.hashpw(master_password.encode("utf-8"), bcrypt.gensalt())
        with open(self.master_password_path, "wb") as file:
            file.write(hashed_password)


    #Load Master Password
    def load_master_password(self):
        try:
            with open(self.master_password_path, "rb") as file:
                self.master_password = file.read()
                rprint("[green]Master Password loaded successfully[/green]")
        except FileNotFoundError as e:
            rprint("[red]Failed to load master password[/red]")


    #Validate Master Password
    def validate_master_password(self, entered_password):
        return bcrypt.checkpw(entered_password.encode("utf-8"), self.master_password)


    #Creates a key for encrpytion/decryption
    def manage_key(self, path=None, generate_new=False):
        path = path or self.key_path
        if generate_new:
            self.key = Fernet.generate_key()
            with open(path, "wb") as file:
                file.write(self.key)
            rprint("[green] Key successfully generated")
        else:
            try:
                with open(path, "rb") as file:
                    self.key = file.read()
            except FileNotFoundError as e:
                rprint("[red]Error: [/red]", str(e))


    #Load Password file
    def load_passwords(self):
        if self.key is None and self.password_file is None:
            print("Password File not available")
        try:
            with open(self.password_file, "rb") as file:
                lines = file.readlines()
                for line in lines:
                     parts = line.strip().split(b":")
                     if len(parts) == 2:
                        site = parts[0].decode()
                        encrypted_password = parts[1]
                        cipher_suite = Fernet(self.key)
                        decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
                        self.password_dict[site] = decrypted_password
        except FileNotFoundError:
            rprint("[red]Failure to locate saved passwords[/red]")
            pass


    #Encrypt and save the password to the database
    def save_password(self, site, password):
        self.password_dict[site] = password

        if self.password_file is not None:
            with open(self.password_file, "ab") as file:
                encrypted = Fernet(self.key).encrypt(password.encode())
                file.write(site.encode() + b":" + encrypted + b"\n")


    #Retrieve the password from the decrypted dictionary in load passwords
    def get_password(self, site):
        return self.password_dict.get(site)


    #Change Password
    def change_password(self, site, new_password):
        if site in self.password_dict:
            self.password_dict[site] = new_password

            # Re-write all passwords to the file
            with open(self.password_file, "wb") as file:
                for site, password in self.password_dict.items():
                    encrypted = Fernet(self.key).encrypt(password.encode())
                    file.write(site.encode() + b":" + encrypted + b"\n")
            rprint("[green]Password has been updated for: [/green]", site)
        else:
            rprint("[red]No entry found for site: [/red]", site)


    #List all stored websites and passwords:
    def print_all(self):
        if not self.password_dict:
            rprint("[red]No Usernames/Passwords Found[/red]")

        for site, password in self.password_dict.items():
            rprint(f"[blue]Site: [/blue] {site}")
            rprint(f"[blue]Password: [/blue] {password}")


    #Create a random password for the user
    def create_random_password(self, length=12):
        characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        random_password = "".join(random.choice(characters)for _ in range(length))
        return random_password


def main():
    #Initialize the password manager class
    pm = PasswordManager()

    #Verify key is loaded prior to setting master password, if not creating one
    if pm.key is None or len(pm.key) != 44:
        rprint("[yellow]No valid encryption key found. Creating a new one[/yellow]")
        pm.manage_key(generate_new=True)

    #Verifying there is a master password, if not, creating one
    if pm.master_password is None:
        while True:
            rprint("[red]No Master Password set, please enter one [/red]")
            master_password = getpass.getpass("Enter Desired master password: ")
            master_password2 = getpass.getpass("Please re-enter master password: ")

            if master_password == master_password2:
                rprint("[green]Master password entered sucessfully[/green]")
                pm.set_master_password(master_password)
                break
            else:
                rprint("[red]Passwords do not match, please try again[/red]")
    else:
        while True:
            entered_password = getpass.getpass("Enter Master Password: ")
            if pm.validate_master_password(entered_password):
                rprint("[green]Logged in succcessfully![/green]")
                break
            else:
                rprint("[red]Incorrect password entry, please try again.[/red]")
                continue

    #Initialize the Command-Line-Interface
    cli(pm)


#Function to host the command line interface
def cli(pm):
    done = False
    while not done:
        print("""Please select an option:
        1: Manage Key
        2: Add a new password
        3: Retrieve a password
        4: Generate a random password for me
        5: Change Master Password
        6: Update a password
        7: Print all websites and passwords
        Q: Quit
        """)

        option = input("Please enter an option: ").lower()
        match option:
            case "1": #Manage Key
                path = input("Please enter a path (leave empty to use the default path): ")
                generate_new_input = input("Do you want to generate a new key? (y/N): ").lower()
                if generate_new_input == 'y':
                    generate_new = True
                else:
                    generate_new = False

                if path:
                    pm.manage_key(path=path, generate_new=generate_new)
                else:
                    pm.manage_key(generate_new=generate_new)
            case "2": #Add a password
                try:
                    site = input("Enter the Website: ")
                    password = input("Please enter the password or press (1) to generate a strong password: ")
                    if password == "1":
                        random_password = pm.create_random_password()
                        pm.save_password(site, random_password)
                        rprint("[green]Random password sucessfully added:[/green]", random_password)
                    else:
                        pm.save_password(site, password)
                        rprint("[green]Password for site sucessfully added: [/green]", site)
                except Exception as e:
                    rprint("[red]Error attemptiong to save a new password[/red]", str(e))
            case "3": #Get password
                try:
                    site = input("Please enter the website you would like the password to: ")
                    password = pm.get_password(site)
                    if password is not None:
                        rprint("[green]The password has been copied to your clipboard for: [/green]", site)
                        pyperclip.copy(pm.get_password(site))
                    else:
                        rprint("[red]No password found for : [/red]", site)
                except Exception as e:
                    rprint("[red]Error: [/red]", str(e))
            case "4": #Generate a random password
                try:
                    random_password1 = pm.create_random_password()
                    print("[green]You're new password has been created and has been copied to the clipboard: [/green]", random_password1)
                    pyperclip.copy(random_password1)
                except Exception as e:
                    rprint("[red]Error attempting to create a random password: [/red]", str(e))
            case "5": #Change Master Password
                master_password = getpass.getpass("Enter new master password: ")
                pm.set_master_password(master_password)
                rprint("[green]Master password successfully changed[/green]")
            case "6": #Update password
                try:
                    site = input("Enter the website to change the password: ")
                    new_password = input("Please enter a new password: ")
                    pm.change_password(site, new_password)
                except:
                    rprint("[red]Error attempting to change the password for site: ", site)
            case "7":
                rprint("[red]CAUTION, This will print all websites and passwords![/red]")
                choice = input("Do you want to continue? Y- Yes, N- No: ").lower()
                if choice == "y":
                    pm.print_all()
                else:
                    continue
            case "q":
                done = True
            case _:
                rprint("[red]Please enter a valid option[/red]")


if __name__ == "__main__":
    main()







