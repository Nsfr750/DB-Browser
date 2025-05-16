"""
Create sample dBase database with sample data for testing.
"""

import os
from dbf import Table, Date, READ_WRITE
from datetime import datetime

def create_sample_dbase():
    """
    Create a sample dBase database with Employees and Departments tables.
    
    Returns:
        str: Path to the created database file
    """
    # Sample data for Employees table
    employees_data = [
        (1, "John", "Doe", "Manager", 75000.00, Date(2022, 1, 15)),
        (2, "Jane", "Smith", "Developer", 65000.00, Date(2022, 3, 20)),
        (3, "Bob", "Johnson", "Analyst", 60000.00, Date(2022, 5, 10)),
        (4, "Alice", "Williams", "Designer", 62000.00, Date(2022, 7, 5)),
        (5, "Charlie", "Brown", "Tester", 58000.00, Date(2022, 9, 12))
    ]

    # Sample data for Departments table
    departments_data = [
        (1, "IT", "Building A - Floor 2"),
        (2, "HR", "Building B - Floor 1"),
        (3, "Finance", "Building A - Floor 3"),
        (4, "Marketing", "Building C - Floor 1"),
        (5, "Sales", "Building C - Floor 2")
    ]

    try:
        # Create Employees table
        employees = Table('sample.dbf',
            'empid N(4,0); firstname C(50); lastname C(50); position C(50); salary N(10,2); hiredate D'
        )
        employees.open(READ_WRITE)
        
        # Add sample data
        for record in employees_data:
            employees.append(record[0], record[1], record[2], record[3], record[4], record[5])
        
        employees.close()

        # Create Departments table
        departments = Table('departments.dbf',
            'deptid N(4,0); deptname C(50); location C(100)'
        )
        departments.open(READ_WRITE)
        
        # Add sample data
        for record in departments_data:
            departments.append(record[0], record[1], record[2])
        
        departments.close()
        
        print("Sample dBase database created successfully!")
        print("Created tables:")
        print("- sample.dbf (Employees)")
        print("- departments.dbf (Departments)")
        print("You can now open these databases in the Database Browser application.")
        return os.path.abspath('sample.dbf')
    except Exception as e:
        print(f"Error creating dBase database: {str(e)}")
        return None

if __name__ == '__main__':
    create_sample_dbase()
