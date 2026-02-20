# MyDiary

A simple Python package to manage contacts in an SQLite database.

## Installation

```bash
pip install -e .
```

## Usage

```bash
# Add a contact with just a phone number
mydiary add 1234567890

# Add a contact with name and phone
mydiary add 9876543210 --name "John Doe"

# Add a contact with phone and address
mydiary add 5551234567 --address "123 Maple St"

# List all contacts
mydiary list
```
