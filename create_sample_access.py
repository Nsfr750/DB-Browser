import pyodbc
import os
from datetime import datetime

def create_sample_access():
    """
    Create a sample Microsoft Access database with Employees and Departments tables.
    
    Returns:
        str: Path to the created database file
    """
    try:
        # Create a new Access database
        db_path = os.path.join(os.path.dirname(__file__), 'sample.accdb')
        
        # Create connection string
        conn_str = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            f'DBQ={db_path};'
        )
        
        # Create connection
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Create sample tables
        cursor.execute("""
            CREATE TABLE Employees (
                EmployeeID AUTOINCREMENT PRIMARY KEY,
                FirstName TEXT(50),
                LastName TEXT(50),
                Department TEXT(50),
                Salary CURRENCY,
                HireDate DATE
            )
        """)

        cursor.execute("""
            CREATE TABLE Departments (
                DepartmentID AUTOINCREMENT PRIMARY KEY,
                DepartmentName TEXT(50),
                Location TEXT(100)
            )
        """)

        # Insert sample data into Employees
        employees_data = [
            (1, 'John', 'Doe', 'IT', 75000.00, datetime(2022, 1, 15)),
            (2, 'Jane', 'Smith', 'HR', 65000.00, datetime(2022, 3, 20)),
            (3, 'Bob', 'Johnson', 'Finance', 80000.00, datetime(2022, 5, 10)),
            (4, 'Alice', 'Williams', 'IT', 72000.00, datetime(2022, 7, 5)),
            (5, 'Charlie', 'Brown', 'HR', 62000.00, datetime(2022, 9, 12))
        ]

        cursor.executemany(
            "INSERT INTO Employees (EmployeeID, FirstName, LastName, Department, Salary, HireDate) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            employees_data
        )

        # Insert sample data into Departments
        departments_data = [
            (1, 'IT', 'Building A - Floor 2'),
            (2, 'HR', 'Building B - Floor 1'),
            (3, 'Finance', 'Building A - Floor 3')
        ]
        
        cursor.executemany(
            "INSERT INTO Departments (DepartmentID, DepartmentName, Location) "
            "VALUES (?, ?, ?)",
            departments_data
        )
        
        # Commit the changes and close the connection
        conn.commit()
        print(f"Sample Access database created successfully at: {db_path}")
        print("Created tables: Employees, Departments")
        print("You can now open this database in the Database Browser application.")
        return db_path
    except pyodbc.Error as e:
        print(f"Error creating Access database: {str(e)}")
        print("\nNOTE: Make sure you have the Microsoft Access Database Engine installed.")
        print("You can download it from: https://www.microsoft.com/en-us/download/details.aspx?id=54920")
        return None
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == '__main__':
    create_sample_access()
