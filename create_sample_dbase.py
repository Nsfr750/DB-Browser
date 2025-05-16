"""
Create sample dBase database with sample data for testing.
"""

import os
from dbf import Table, Field, Date
from datetime import datetime

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
    employees = Table(
        'sample.dbf',
        'EMPID N(4,0); FIRSTNAME C(20); LASTNAME C(20); POSITION C(20); SALARY N(10,2); HIREDATE D'
    )
    employees.open()
    employees.append(employees_data)
    employees.close()

    # Create Departments table
    departments = Table(
        'departments.dbf',
        'DEPTID N(4,0); DEPTNAME C(30); LOCATION C(50)'
    )
    departments.open()
    departments.append(departments_data)
    departments.close()

    print("Sample dBase database created successfully!")
    print("Created tables:")
    print("- sample.dbf (Employees)")
    print("- departments.dbf (Departments)")
    print("You can now open these databases in the Database Browser application.")

except Exception as e:
    print(f"Error creating dBase database: {str(e)}")
