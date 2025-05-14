import pyodbc
import os

# Create a new Access database
db_path = os.path.join(os.path.dirname(__file__), 'sample.accdb')

# Connection string for creating a new database
conn_str = (
    r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
    f"DBQ={db_path};"
    "Create_DB=True;"
)

try:
    # Create the database
    conn = pyodbc.connect(conn_str, autocommit=True)
    conn.close()

    # Connect to the created database
    conn = pyodbc.connect(f"Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={db_path}")
    cursor = conn.cursor()

    # Create sample tables
    cursor.execute("""
        CREATE TABLE Employees (
            EmployeeID INT PRIMARY KEY,
            FirstName VARCHAR(50),
            LastName VARCHAR(50),
            Department VARCHAR(50),
            Salary DECIMAL(10,2)
        )
    """)

    cursor.execute("""
        CREATE TABLE Departments (
            DepartmentID INT PRIMARY KEY,
            DepartmentName VARCHAR(50),
            Location VARCHAR(100)
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

    for emp in employees_data:
        cursor.execute(
            "INSERT INTO Employees (EmployeeID, FirstName, LastName, Department, Salary) "
            "VALUES (?, ?, ?, ?, ?)",
            emp
        )

    # Insert sample data into Departments
    departments_data = [
        (1, 'IT', 'Building A - Floor 2'),
        (2, 'HR', 'Building B - Floor 1'),
        (3, 'Finance', 'Building A - Floor 3')
    ]

    for dept in departments_data:
        cursor.execute(
            "INSERT INTO Departments (DepartmentID, DepartmentName, Location) "
            "VALUES (?, ?, ?)",
            dept
        )

    conn.commit()
    print(f"Sample Access database created successfully at: {db_path}")
    print("Created tables: Employees, Departments")
    print("You can now open this database in the Database Browser application.")

except pyodbc.Error as e:
    print(f"Error: {str(e)}")
    print("\nNOTE: Make sure you have the Microsoft Access Database Engine installed.")
    print("You can download it from: https://www.microsoft.com/en-us/download/details.aspx?id=54920")

finally:
    if 'conn' in locals():
        conn.close()
