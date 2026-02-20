import sqlite3

DB_PATH = "mydiary.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE,
                phone TEXT NOT NULL,
                address TEXT UNIQUE
            )
        ''')
        conn.commit()

def get_next_unknown(column_name, prefix):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        # Find the max number used in unknown names/addresses
        cursor.execute(f"SELECT {column_name} FROM contacts WHERE {column_name} LIKE '{prefix}%'")
        existing = cursor.fetchall()
        
        nums = []
        for (val,) in existing:
            try:
                num = int(val.replace(prefix, ""))
                nums.append(num)
            except ValueError:
                continue
        
        next_num = max(nums) + 1 if nums else 1
        return f"{prefix}{next_num}"

def add_contact(phone, name=None, address=None):
    if not name:
        name = get_next_unknown("name", "unknown_")
    if not address:
        address = get_next_unknown("address", "unknown_address_")
    
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO contacts (name, phone, address) VALUES (?, ?, ?)",
                (name, phone, address)
            )
            conn.commit()
            return True, f"Added: {name}, {phone}, {address}"
        except sqlite3.IntegrityError as e:
            return False, f"Error: {e}"

def list_contacts():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, phone, address FROM contacts")
        return cursor.fetchall()
