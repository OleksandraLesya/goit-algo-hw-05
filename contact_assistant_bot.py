"""
Contact Assistant Bot
This console bot allows the user to manage a list of contacts with their phone numbers.
Supported commands: add, phone, all, exit/close, hello.
It includes a decorator to handle common input errors like missing arguments or unknown names.
"""
import functools
import sys

def input_error(func):
    """
    A decorator that catches KeyError, ValueError, and IndexError
    exceptions from the decorated function and returns a user-friendly
    error message.
    """
    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name or Contact not found."
        except ValueError:
            # This could be for missing arguments or wrong format.
            # Example: "add" without name/phone will raise ValueError in handler.
            return "Give me name and phone please."
        except IndexError:
            # This often happens if the input is too short
            # for parsing or accessing args[0] directly without checks.
            # Example: "phone" without a name.
            return "Enter the argument for the command."
        except Exception as e: # Catch any other unexpected errors for robustness
            return f"An unexpected error occurred: {e}"
    return inner

def parse_input(user_input: str) -> tuple:
    """
    Parses the user's input string into a command and its arguments.
    Args:
        user_input (str): The raw input string from the user.
    Returns:
        tuple: A tuple containing the command (str) and a list of arguments (list[str]).
               Returns an empty string for the command and an empty list for args if input is empty.
    """
    parts = user_input.split()
    if not parts:
        return "", []
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args

@input_error
def add_contact(args: list, contacts: dict) -> str:
    """
    Adds a new contact to the contacts dictionary.
    Args:
        args (list): A list containing exactly two elements: [name, phone_number].
        contacts (dict): The dictionary where contacts are stored.
    Returns:
        str: A confirmation message "Contact added.".
    Raises:
        ValueError: If the number of arguments is not 2.
    """

    name, phone = args

    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args: list, contacts: dict) -> str:
    """
    Changes the phone number for an existing contact.
    Args:
        args (list): A list containing exactly two elements: [name, new_phone_number].
        contacts (dict): The dictionary where contacts are stored.
    Returns:
        str: A confirmation message "Contact updated.".
    Raises:
        ValueError: If the number of arguments is not 2.
        KeyError: If the contact name does not exist in the contacts dictionary.
    """

    name, phone = args

    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args: list, contacts: dict) -> str:
    """
    Retrieves the phone number for a specified contact.
    Args:
        args (list): A list containing exactly one element: [name].
        contacts (dict): The dictionary where contacts are stored.
    Returns:
        str: The phone number of the contact.
    Raises:
        ValueError: If the number of arguments is not 1.
        KeyError: If the contact name does not exist in the contacts dictionary.
    """
    name = args[0]
    if name not in contacts:
        raise KeyError
    return contacts[name]

def all_contacts(contacts: dict) -> str:
    """
    Displays all saved contacts with their phone numbers.
    Args:
        contacts (dict): The dictionary where contacts are stored.
    Returns:
        str: A formatted string listing all contacts, 
        or "No contacts saved." if the dictionary is empty.
    """
    if not contacts:
        return "No contacts saved."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    """
    The main function that runs the assistant bot.
    It processes user commands in a loop until 'close' or 'exit' is entered.
    """
    contacts = {} # Dictionary for contacts storage: {name: phone number}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(all_contacts(contacts))
        elif command == "": # Handle empty input gracefully
            continue
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
