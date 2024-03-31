#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from termcolor import colored
import random
import time

def scrape_usernames(username):
    url = f"https://www.instagram.com/{username}/"
    try:
        time.sleep(random.uniform(1, 3))  # Add random delay between 1 and 3 seconds
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()  # Raise exception for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        usernames = [username]
        similar_usernames = []
        for suggestion in soup.find_all('a', {'class': 'FPmhX notranslate _0imsa '}):
            suggestion_username = suggestion.text
            if username.lower() in suggestion_username.lower():
                similar_usernames.append(suggestion_username)
            if len(similar_usernames) == 20:
                break
        return similar_usernames
    except requests.exceptions.RequestException as e:
        print(colored(f"Error: {e}", 'red'))
        return []

def check_passwords(usernames, passwords):
    matched = False
    for username in usernames:
        time.sleep(random.uniform(1, 3))  # Add random delay between 1 and 3 seconds
        if username in passwords:
            print(colored(f"{username}: {username} - Matched", 'green'))
            matched = True
        else:
            print(colored(f"{username} - Not matched", 'red'))
    return matched

def main():
    username = input("Enter Instagram username: ")
    password1 = input("Enter password 1: ")
    password2 = input("Enter password 2: ")
    password3 = input("Enter password 3: ")
    passwords = [password1, password2, password3]
    
    print("\nScraping usernames...")
    usernames = scrape_usernames(username)
    
    if usernames:
        print("\nChecking passwords...")
        matched = check_passwords(usernames, passwords)
        
        if not matched:
            print(colored("No matches found for any username-password pair.", 'red'))
    else:
        print(colored("Exiting due to error.", 'red'))

if __name__ == "__main__":
    main()
