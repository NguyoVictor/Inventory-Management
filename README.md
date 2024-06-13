Sure! Here's a revised README file tailored to your Inventory Management System project.

---

# Inventory Management System (IMS)

## Introduction

The Inventory Management System (IMS) is designed to help businesses keep track of their inventory levels, manage product details, and handle transactions involving inventory items. The system provides functionalities to add, update, delete, and query inventory items and transactions.

## Project Structure

Take a look at the directory structure:

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
├── app.py
├── setup.py
├── connection.py
└── lib
    ├── models
    │   ├── __init__.py
    │   └── models.py
    ├── cli.py
    ├── helpers.py
```

## Setting Up the Environment

1. **Clone the repository**:
   ```sh
   git clone https://github.com/NguyoVictor/Inventory-Management.git

   cd Inventory-Management
   ```
## Running the Application

Execute the main application script to start the CLI:
```sh
python app.py
```

## Database Tables

### Products Table
The products table stores information about each product in the inventory.

| Column Name | Data Type | Description |
|-------------|------------|-------------|
| product_id  | INTEGER    | Unique identifier for the product |
| product_name| TEXT       | Name of the product |
| category    | TEXT       | Category of the product |

### Transactions Table
The transactions table records each transaction involving inventory items.

| Column Name   | Data Type | Description |
|---------------|------------|-------------|
| transaction_id| INTEGER    | Unique identifier for the transaction |
| product_id    | INTEGER    | Identifier for the product |
| quantity      | INTEGER    | Quantity of product involved |
| date          | TEXT       | Date of transaction |

### Suppliers Table
The suppliers table stores information about suppliers who provide products.

| Column Name   | Data Type | Description |
|---------------|------------|-------------|
| supplier_id   | INTEGER    | Unique identifier for the supplier |
| supplier_name | TEXT       | Name of the supplier |

## CLI Operations

### Main CLI
The main CLI script is located in `app.py`. This script initializes the database and presents a menu for the user to interact with the system.

### Helpers
Helper functions are located in `lib/helpers.py`. These functions perform specific tasks such as listing products, adding transactions, updating supplier information, etc.

### Models
The data models for the application are defined in `lib/models/models.py`. This includes the definitions for the `Product`, `Transaction`, and `Supplier` classes.

### Example Operations

1. **List Products**:
   ```sh
   python app.py
   ```

2. **Add Product**:
   Follow the prompts to enter product details.

3. **Update Product**:
   Follow the prompts to update a product's details.

4. **Delete Product**:
   Follow the prompts to delete a product.

5. **List Transactions**:
   Follow the prompts to view all transactions.

6. **Add Transaction**:
   Follow the prompts to add a new transaction.

## Conclusion

The Inventory Management System (IMS) is a comprehensive solution for managing inventory. It provides essential functionalities to handle products, transactions, and suppliers efficiently.

Happy coding!

## Resources

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)

---

This README should now be more aligned with your Inventory Management System project, providing clear instructions and a structured overview of the project. Adjust the URLs and paths as necessary to match your repository and file structure.