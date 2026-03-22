"""
Command line tools to filter out users by a parameter and print a filtered list.
"""

import json


PATH_TO_USERS_LIST = "users.json"


def load_users():
    """
    Load the list of users from a file

    Returns:
        list of dictionaries with information about users
    """
    try:
        with open(PATH_TO_USERS_LIST, "r", encoding="utf-8") as file:
            users = json.load(file)
            return users
    except FileNotFoundError:
        print(f"List not found: {PATH_TO_USERS_LIST} does not exist.")
    except PermissionError:
        print(f"Cannot read file {PATH_TO_USERS_LIST}. Permission denied.")
    except UnicodeDecodeError:
        print(f"Cannot read file {PATH_TO_USERS_LIST}. Encoding should be UTF-8")
    except OSError as e:
        print(f"Failed to load {PATH_TO_USERS_LIST}: {e}")
    return None


def print_users(users: list, no_users_message: str = "No users found."):
    """
    Print users from a list.

    Args:
        users: list of dictionaries with information about users.
        no_users_message: message to print if the list is empty.
    """
    if users:
        for user in users:
            print(user)
    else:
        print(no_users_message)


def filter_users_by_age(users: list[dict]) -> list:
    """
    Filter users list by the age entered by the user.

    Args:
        users: list of users

    Returns:
        filtered list of users with the name entered by the user
    """
    age = int(input("Enter age to filter users: ").strip())
    filtered_users = [user for user in users if user["age"] == age]
    return filtered_users


def filter_users_by_name(users: list[dict]) -> list:
    """
    Filter users list by name entered by the user.

    Args:
        users: list of users

    Returns:
        filtered list of users with the name entered by the user
    """
    name = input("Enter a name to filter users: ").strip()
    filtered_users = [user for user in users if user["name"].lower() ==
                      name.lower()]
    return filtered_users


def filter_users_by_email(users: list[dict]) -> list:
    """
    Filter users list by email entered by the user.

    Args:
        users: list of users

    Returns:
        filtered list of users with the name entered by the user
    """
    name = input("Enter email to filter users: ").strip()
    filtered_users = [user for user in users if user["email"].lower() ==
                      name.lower()]
    return filtered_users


def filter_users(filter_by):
    """
    Filter users with a function filter_by, print filtered list of users.

    Args:
        filter_by: a function used for filtering users list.
    """
    users = load_users()
    filtered_users = filter_by(users)
    print_users(filtered_users)


def call(filter_option: str):
    """
    Call filter_users function with a correct filtering function from
    the DISPATCHER

    Args:
        filter_option: keyword to call filtering function from the DISPATCHER
    """
    filter_users(DISPATCHER[filter_option])


DISPATCHER = {
    "age": filter_users_by_age,
    "name": filter_users_by_name,
    "email": filter_users_by_email
}


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (Currently, only "
                          "'name' and 'age' are supported): ").strip().lower()
    if filter_option in DISPATCHER:
        call(filter_option)
    else:
        print("Filtering by that option is not yet supported.")
