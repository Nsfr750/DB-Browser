# Sample Databases

This document explains how to create and use sample databases in the DB Browser.

## Creating Sample Databases

The application provides a "Create Sample Database" menu that allows you to create sample databases for testing and development purposes. All sample databases are created in the `sample_databases` directory.

### Available Database Types

1. **SQLite Database**
   - Creates a sample SQLite database file
   - Tables: Employees, Departments
   - Location: `sample_databases/sample_sqlite.db`

2. **MySQL Database**
   - Creates a MySQL database with connection details
   - Tables: Employees, Departments
   - Location: `sample_databases/sample_mysql.sql`
   - Requires MySQL server installation

3. **PostgreSQL Database**
   - Creates a PostgreSQL database with connection details
   - Tables: Employees, Departments
   - Location: `sample_databases/sample_postgres.sql`
   - Requires PostgreSQL server installation

4. **Microsoft Access Database**
   - Creates a sample Access database
   - Tables: Employees, Departments
   - Location: `sample_databases/sample.accdb`
   - Requires Microsoft Access Database Engine

5. **MVO Database**
   - Creates a sample MVO database
   - Tables: Employees, Departments
   - Location: `sample_databases/sample.mvo`
   - JSON-based storage

6. **dBase Database**
   - Creates a sample dBase database
   - Tables: Employees, Departments
   - Location: `sample_databases/sample.dbf`
   - Legacy database format

## Using Sample Databases

1. Open the main application window
2. Click on "File" -> "Create Sample Database"
3. Select the desired database type
4. Click "Create"
5. The database will be created in the `sample_databases` directory
6. You can then open the created database using the "Open Database" menu option

## Sample Data Structure

All sample databases contain two tables with the following structure:

### Employees Table
- empid (Primary Key)
- firstname (VARCHAR)
- lastname (VARCHAR)
- position (VARCHAR)
- salary (DECIMAL)
- hiredate (DATE)

### Departments Table
- deptid (Primary Key)
- deptname (VARCHAR)
- location (VARCHAR)

## Additional Notes

- Each sample database contains test data for demonstration purposes
- The `sample_databases` directory is automatically created if it doesn't exist
- Connection details for MySQL and PostgreSQL databases are saved in .sql files
- You can safely delete the `sample_databases` directory to start fresh
