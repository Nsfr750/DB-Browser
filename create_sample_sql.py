"""
Create sample PostgreSQL database with sample data for testing.
"""

import os
import psycopg2
from psycopg2 import sql
import json

# Sample data for Employees table
employees_data = [
    (1, "John", "Doe", "Manager", 75000.00, "2022-01-15"),
    (2, "Jane", "Smith", "Developer", 65000.00, "2022-03-20"),
    (3, "Bob", "Johnson", "Analyst", 60000.00, "2022-05-10"),
    (4, "Alice", "Williams", "Designer", 62000.00, "2022-07-05"),
    (5, "Charlie", "Brown", "Tester", 58000.00, "2022-09-12")
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
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname="mysql",
        user="mysql",
        password="mysql",
        host="localhost",
        port="5432"
    )
    
    conn.autocommit = True
    cur = conn.cursor()

    # Create database if it doesn't exist
    cur.execute(sql.SQL("CREATE DATABASE IF NOT EXISTS sample_db"))
    
    # Connect to the new database
    conn.close()
    conn = psycopg2.connect(
        dbname="sample_db",
        user="mysql",
        password="mysql",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    # Create Employees table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            empid SERIAL PRIMARY KEY,
            firstname VARCHAR(50) NOT NULL,
            lastname VARCHAR(50) NOT NULL,
            position VARCHAR(50) NOT NULL,
            salary DECIMAL(10,2) NOT NULL,
            hiredate DATE NOT NULL
        )
    """)

    # Create Departments table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS departments (
            deptid SERIAL PRIMARY KEY,
            deptname VARCHAR(50) NOT NULL,
            location VARCHAR(100) NOT NULL
        )
    """)

    # Insert sample data
    cur.executemany("""
        INSERT INTO employees (empid, firstname, lastname, position, salary, hiredate)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, employees_data)

    cur.executemany("""
        INSERT INTO departments (deptid, deptname, location)
        VALUES (%s, %s, %s)
    """, departments_data)

    # Create a JSON file with connection details
    connection_info = {
        "type": "postgresql",
        "host": "localhost",
        "user": "postgres",
        "password": "postgres",
        "database": "sample_db"
    }
    
    # Create sample_databases directory if it doesn't exist
    os.makedirs('sample_databases', exist_ok=True)
    
    # Save connection details to sample_databases directory
    with open(os.path.join('sample_databases', 'sample_postgres.sql'), "w") as f:
        json.dump(connection_info, f, indent=2)

    print("Sample PostgreSQL database created successfully!")
    print("Created tables:")
    print("- employees")
    print("- departments")
    print("Connection details saved to sample_databases directory")
    print("Connection details saved to sample.sql")
    print("You can now open this database in the Database Browser application.")

except Exception as e:
    print(f"Error creating PostgreSQL database: {str(e)}")
finally:
    if 'cur' in locals():
        cur.close()
    if 'conn' in locals():
        conn.close()
