import pytest
from io import StringIO
import sys
from project import PasswordManager

def main():
    test_create_random_password()
    test_save_password()
    test_print_all()
    test_validate_master_pass()

#Test random password creation
def test_create_random_password():
    pm = PasswordManager()
    password = pm.create_random_password(length=12)

    assert len(password) == 12
    assert isinstance(password, str)


#Test Save Password and Get Password
def test_save_password():
    pm = PasswordManager()

    site = "test_website"
    password = "test_password"

    pm.save_password(site, password)

    get_password = pm.get_password(site)
    assert get_password == password

def test_print_all():
    pm = PasswordManager()
    pm.save_password("website", "password")

    out = StringIO()
    original_stdout = sys.stdout
    sys.stdout = out

    pm.print_all()

    sys.stdout = original_stdout
    out.seek(0)
    output = out.read()

    assert "website" in output
    assert "password" in output

def test_validate_master_pass():
    pm = PasswordManager()

    test_master_password = "password"
    pm.set_master_password(test_master_password)

    assert pm.validate_master_password("password123") == False




if __name__ == "__main__":
    main()






