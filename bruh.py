import json
import os

CRED_FILE = "credentials.json"
MASTER_PIN = "1234"  # You can change this to any 4-digit pin

def load_credentials():
    if not os.path.exists(CRED_FILE):
        return []
    with open(CRED_FILE, "r") as f:
        return json.load(f)

def save_credentials(creds):
    with open(CRED_FILE, "w") as f:
        json.dump(creds, f, indent=4)

def create_credential():
    site = input("Enter site name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    creds = load_credentials()
    creds.append({"site": site, "username": username, "password": password})
    save_credentials(creds)
    print("Credential saved successfully!\n")

def retrieve_credentials():
    site = input("Enter site name to retrieve: ")
    creds = load_credentials()
    found = False
    for cred in creds:
        if cred["site"].lower() == site.lower():
            print(f"Site: {cred['site']}\nUsername: {cred['username']}\nPassword: {cred['password']}\n")
            found = True
    if not found:
        print("No credentials found for this site.\n")

def main():
    pin = input("Enter your 4-digit master PIN: ")
    if pin != MASTER_PIN:
        print("Incorrect PIN. Access denied.")
        return

    while True:
        print("1. Create new credentials")
        print("2. Retrieve credentials")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            create_credential()
        elif choice == "2":
            retrieve_credentials()
        elif choice == "3":
            print("Exiting Password Manager.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()