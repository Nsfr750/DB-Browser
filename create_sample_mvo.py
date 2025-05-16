import json
import os
from datetime import datetime

def create_sample_mvo():
    """
    Create a sample MVO database with Employees and Departments tables.
    
    Returns:
        str: Path to the created database file
    """
    try:
        # Create a new MVO database
        db_path = os.path.join(os.path.dirname(__file__), 'sample.mvo')
        
        # Create database structure
        database = {
            "version": "1.0",
            "tables": {
                "Employees": {
                    "fields": {
                        "EmployeeID": "integer",
                        "FirstName": "text",
                        "LastName": "text",
                        "Department": "text",
                        "Salary": "decimal",
                        "HireDate": "date"
                    },
                    "records": []
                },
                "Departments": {
                    "fields": {
                        "DepartmentID": "integer",
                        "DepartmentName": "text",
                        "Location": "text"
                    },
                    "records": []
                }
            }
        }

        # Add sample data to Employees
        employees_data = [
            {"EmployeeID": 1, "FirstName": "John", "LastName": "Doe", "Department": "IT", "Salary": 75000.00, "HireDate": "2022-01-15"},
            {"EmployeeID": 2, "FirstName": "Jane", "LastName": "Smith", "Department": "HR", "Salary": 65000.00, "HireDate": "2022-03-20"},
            {"EmployeeID": 3, "FirstName": "Bob", "LastName": "Johnson", "Department": "Finance", "Salary": 80000.00, "HireDate": "2022-05-10"},
            {"EmployeeID": 4, "FirstName": "Alice", "LastName": "Williams", "Department": "IT", "Salary": 72000.00, "HireDate": "2022-07-05"},
            {"EmployeeID": 5, "FirstName": "Charlie", "LastName": "Brown", "Department": "HR", "Salary": 62000.00, "HireDate": "2022-09-12"}
        ]
        database["tables"]["Employees"]["records"] = employees_data

        # Add sample data to Departments
        departments_data = [
            {"DepartmentID": 1, "DepartmentName": "IT", "Location": "Building A - Floor 2"},
            {"DepartmentID": 2, "DepartmentName": "HR", "Location": "Building B - Floor 1"},
            {"DepartmentID": 3, "DepartmentName": "Finance", "Location": "Building A - Floor 3"}
        ]
        database["tables"]["Departments"]["records"] = departments_data

        # Write to file
        with open(db_path, 'w', encoding='utf-8') as f:
            json.dump(database, f, ensure_ascii=False, indent=2)

        print(f"Sample MVO database created successfully at: {db_path}")
        print("Created tables: Employees, Departments")
        print("You can now open this database in the Database Browser application.")
        return db_path
    except Exception as e:
        print(f"Error creating MVO database: {str(e)}")
        return None

if __name__ == '__main__':
    create_sample_mvo()
