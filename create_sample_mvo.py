import json
import os

# Sample MVO database structure
sample_db = {
    "Employees": {
        "columns": ["EmployeeID", "FirstName", "LastName", "Department", "Salary"],
        "rows": [
            [1, "John", "Doe", "IT", 75000.00],
            [2, "Jane", "Smith", "HR", 65000.00],
            [3, "Bob", "Johnson", "Finance", 80000.00],
            [4, "Alice", "Williams", "IT", 72000.00],
            [5, "Charlie", "Brown", "HR", 62000.00]
        ]
    },
    "Departments": {
        "columns": ["DepartmentID", "DepartmentName", "Location"],
        "rows": [
            [1, "IT", "Building A - Floor 2"],
            [2, "HR", "Building B - Floor 1"],
            [3, "Finance", "Building A - Floor 3"]
        ]
    }
}

# Create a new MVO database file
db_path = os.path.join(os.path.dirname(__file__), 'sample.mvo')

try:
    with open(db_path, 'w') as f:
        json.dump(sample_db, f, indent=2)
    print(f"Sample MVO database created successfully at: {db_path}")
    print("Created tables: Employees, Departments")
    print("You can now open this database in the Database Browser application.")
except IOError as e:
    print(f"Error creating MVO database: {str(e)}")
