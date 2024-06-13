from connection import get_db_connection

# SQL statements to create tables
CREATE_PRODUCTS_TABLE = '''
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL
);
'''

CREATE_TRANSACTIONS_TABLE = '''
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    quantity INTEGER,
    date TEXT,
    FOREIGN KEY (product_id) REFERENCES products (product_id)
);
'''

CREATE_SUPPLIERS_TABLE = '''
CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    supplier_name TEXT NOT NULL
);
'''

# Function to create tables
def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(CREATE_PRODUCTS_TABLE)
    cursor.execute(CREATE_TRANSACTIONS_TABLE)
    cursor.execute(CREATE_SUPPLIERS_TABLE)

    conn.commit()
    conn.close()

# Call the function to create tables
if __name__ == "__main__":
    create_tables()
