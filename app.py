# main.py
from setup import create_tables
from helpers import (
    list_products, list_transactions, list_suppliers,
    add_product, add_transaction, add_supplier,
    update_product, update_transaction, update_supplier,
    delete_product, delete_transaction, delete_supplier
)

def main():
    create_tables()
    while True:
        print("""
        1. List products
        2. List transactions
        3. List suppliers
        4. Add product
        5. Add transaction
        6. Add supplier
        7. Update product
        8. Update transaction
        9. Update supplier
        10. Delete product
        11. Delete transaction
        12. Delete supplier
        13. Exit
        """)
        choice = input("Enter your choice: ")
        if choice == '1':
            list_products()
        elif choice == '2':
            list_transactions()
        elif choice == '3':
            list_suppliers()
        elif choice == '4':
            add_product()
        elif choice == '5':
            add_transaction()
        elif choice == '6':
            add_supplier()
        elif choice == '7':
            update_product()
        elif choice == '8':
            update_transaction()
        elif choice == '9':
            update_supplier()
        elif choice == '10':
            delete_product()
        elif choice == '11':
            delete_transaction()
        elif choice == '12':
            delete_supplier()
        elif choice == '13':
            print("Goodbye, thanks for using us!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
