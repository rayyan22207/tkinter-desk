import shelve
import os

# Function to save a token with a specific key
# This function stores the token persistently in a shelf file (auth_data.db).
def save_token(key, token):
    """
    Save a token to the shelf file with the specified key.

    Args:
        key (str): The key to associate with the token.
        token (str): The token value to save.

    Example:
        save_token('access_token', 'your-token-here')
    """
    with shelve.open('auth_data') as db:
        db[key] = token
    print(f"Token saved for {key}!")

# Function to retrieve a token by its key
# This function fetches the token associated with the key, if it exists.
def get_token(key):
    """
    Retrieve a token from the shelf file by its key.

    Args:
        key (str): The key of the token to retrieve.

    Returns:
        str or None: The token if found, otherwise None.

    Example:
        token = get_token('access_token')
    """
    with shelve.open('auth_data') as db:
        token = db.get(key, None)
    if token:
        print(f"Token retrieved for {key}: {token}")
    else:
        print(f"No token found for {key}")
    return token

# Function to delete a token by its key
# This function removes the token associated with the key.
def delete_token(key):
    """
    Delete a token from the shelf file by its key.

    Args:
        key (str): The key of the token to delete.

    Example:
        delete_token('access_token')
    """
    with shelve.open('auth_data') as db:
        if key in db:
            del db[key]
            print(f"Token for {key} deleted.")
        else:
            print(f"No token found for {key} to delete.")

# Function to list all saved tokens
# This function retrieves all keys in the shelf file.
def list_all_tokens():
    """
    List all keys of the saved tokens in the shelf file.

    Returns:
        list: A list of all keys.

    Example:
        keys = list_all_tokens()
    """
    with shelve.open('auth_data') as db:
        keys = list(db.keys())
    print(f"Saved tokens: {keys}")
    return keys

# Function to clear all tokens
# This function deletes the entire shelf file and all its contents.
def clear_all_tokens():
    """
    Clear all tokens by removing the shelf file.

    Example:
        clear_all_tokens()
    """
    if os.path.exists('auth_data.db'):
        os.remove('auth_data.db')
        print("All tokens cleared.")
    else:
        print("No token file to clear.")
