import argparse
from mydiary.db import init_db, add_contact, list_contacts

def main():
    init_db()
    parser = argparse.ArgumentParser(description="MyDiary CLI - Keep your contacts safe")
    subparsers = parser.add_subparsers(dest="command")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new contact")
    add_parser.add_argument("phone", help="Phone number (required)")
    add_parser.add_argument("-n", "--name", help="Name of the contact")
    add_parser.add_argument("-a", "--address", help="Address of the contact")

    # List command
    subparsers.add_parser("list", help="List all contacts")

    args = parser.parse_args()

    if args.command == "add":
        success, message = add_contact(args.phone, args.name, args.address)
        print(message)
    elif args.command == "list":
        contacts = list_contacts()
        if not contacts:
            print("No contacts found.")
        for name, phone, address in contacts:
            print(f"Name: {name} | Phone: {phone} | Address: {address}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
