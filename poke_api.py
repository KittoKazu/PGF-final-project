import requests
import poke_main

def call_api(url, param):
    """
    Function that calls an api based on a base URL and a parameter. (custom input)
    """
    try:
        response = requests.get(f"{url}{param}")
        check_api(response)
        response_dict = response.json()
        return response_dict
    except requests.exceptions.ConnectionError:
        print('Cannot connect to API, returning to menu')
        poke_main.main()

def check_api(response_name):
    """
    Checks if connection to the API was successful, if not, returns to the main menu of the program.
    """
    if response_name.status_code != 200:
        print('Something went wrong with finding a connection, returning to menu.')
        poke_main.main()