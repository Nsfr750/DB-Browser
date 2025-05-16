import sqlite3
import os
from datetime import datetime

def create_sample_sqlite():
    """
    Create a sample SQLite database with Employees and Departments tables.
    
    Returns:
        str: Path to the created database file
    """
    try:
        # Create a new SQLite database
        db_path = os.path.join(os.path.dirname(__file__), 'sample.db')
        
        # Connect to SQLite database (creates it if it doesn't exist)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Create sample tables
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Employees (
                EmployeeID INTEGER PRIMARY KEY,
                FirstName TEXT,
                LastName TEXT,
                Department TEXT,
                Salary REAL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Departments (
                DepartmentID INTEGER PRIMARY KEY,
                DepartmentName TEXT,
                Location TEXT
            )
        """)

        # Insert sample data into Employees
        employees_data = [
            (1, 'John', 'Doe', 'IT', 75000.00),
            (2, 'Jane', 'Smith', 'HR', 65000.00),
            (3, 'Bob', 'Johnson', 'Finance', 80000.00),
            (4, 'Alice', 'Williams', 'IT', 72000.00),
            (5, 'Charlie', 'Brown', 'HR', 62000.00)
        ]

        cursor.executemany(
            "INSERT OR IGNORE INTO Employees (EmployeeID, FirstName, LastName, Department, Salary) "
            "VALUES (?, ?, ?, ?, ?)",
            employees_data
        )

        # Insert sample data into Departments
        departments_data = [
            (1, 'IT', 'Building A - Floor 2'),
            (2, 'HR', 'Building B - Floor 1'),
            (3, 'Finance', 'Building A - Floor 3')
        ]
        
        cursor.executemany(
            "INSERT OR IGNORE INTO Departments (DepartmentID, DepartmentName, Location) "
            "VALUES (?, ?, ?)",
            departments_data
        )
        
        # Commit the changes and close the connection
        conn.commit()
        print(f"Sample SQLite database created successfully at: {db_path}")
        print("Created tables: Employees, Departments")
        print("You can now open this database in the Database Browser application.")
        return db_path

    except sqlite3.Error as e:
        print(f"Error creating SQLite database: {str(e)}")
        return None

    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == '__main__':
    create_sample_sqlite()
