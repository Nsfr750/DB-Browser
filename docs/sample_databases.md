# 📊 Sample Databases

This document provides detailed information about creating and using sample databases in DB Browser.

## 📋 Overview

Sample databases are pre-configured databases that contain example data for testing and development purposes. They are created in the `sample_databases` directory and can be used to:
- Test database operations
- Learn database structure
- Demonstrate features
- Develop queries

## 🛠️ Creating Sample Databases

To create a sample database:

1. Open DB Browser
2. Go to "File" -> "Create Sample Database"
3. Select your desired database type
4. Click "Create"

### Available Database Types

#### SQLite Database
- **File**: `sample_databases/sample_sqlite.db`
- **Structure**: 
  ```sql
  CREATE TABLE employees (
    empid INTEGER PRIMARY KEY,
    firstname TEXT,
    lastname TEXT,
    position TEXT,
    salary REAL,
    hiredate DATE
  );
  ```
- **Features**: 
  - File-based storage
  - No server required
  - ACID-compliant

#### MySQL Database
- **File**: `sample_databases/sample_mysql.sql`
- **Structure**: 
  ```sql
  CREATE TABLE employees (
    empid INT AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    position VARCHAR(50),
    salary DECIMAL(10,2),
    hiredate DATE
  );
  ```
- **Requirements**: 
  - MySQL server
  - `mysql-connector-python` package
  - Default credentials: root/root

#### PostgreSQL Database
- **File**: `sample_databases/sample_postgres.sql`
- **Structure**: 
  ```sql
  CREATE TABLE employees (
    empid SERIAL PRIMARY KEY,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    position VARCHAR(50),
    salary DECIMAL(10,2),
    hiredate DATE
  );
  ```
- **Requirements**: 
  - PostgreSQL server
  - `psycopg2` package
  - Default credentials: postgres/postgres

#### Microsoft Access Database
- **File**: `sample_databases/sample.accdb`
- **Structure**: 
  - Employees table with same fields as above
  - Departments table with deptid, deptname, location
- **Requirements**: 
  - Microsoft Access Database Engine
  - Windows operating system

#### MVO Database
- **File**: `sample_databases/sample.mvo`
- **Structure**: 
  ```json
  {
    "employees": [
      {
        "empid": 1,
        "firstname": "John",
        "lastname": "Doe",
        "position": "Manager",
        "salary": 75000.00,
        "hiredate": "2022-01-15"
      }
    ],
    "departments": [
      {
        "deptid": 1,
        "deptname": "IT",
        "location": "Building A - Floor 2"
      }
    ]
  }
  ```
- **Features**: 
  - JSON-based storage
  - Schema-less design
  - Easy modification

#### dBase Database
- **File**: `sample_databases/sample.dbf`
- **Structure**: 
  - Employees table with fixed record length
  - Departments table with deptid, deptname, location
- **Features**: 
  - Legacy compatibility
  - Fixed record format
  - Simple structure

## 📊 Sample Data

All sample databases contain the following test data:

### Employees Table
| empid | firstname | lastname | position | salary | hiredate |
|-------|-----------|----------|----------|--------|----------|
| 1     | John      | Doe      | Manager  | 75000  | 2022-01-15 |
| 2     | Jane      | Smith    | Developer| 65000  | 2022-03-20 |
| 3     | Bob       | Johnson  | Analyst  | 60000  | 2022-05-10 |

### Departments Table
| deptid | deptname | location |
|--------|----------|----------|
| 1      | IT       | Building A - Floor 2 |
| 2      | HR       | Building B - Floor 1 |
| 3      | Finance  | Building A - Floor 3 |

## 📚 Using Sample Databases

1. **Opening a Sample Database**:
   - Go to "File" -> "Open Database"
   - Navigate to `sample_databases` directory
   - Select the desired database file

2. **Viewing Data**:
   - Tables are automatically loaded
   - Browse through records
   - View table structure

3. **Executing Queries**:
   - Use the SQL editor
   - Run SELECT, INSERT, UPDATE queries
   - View query results

## 🛠️ Maintenance

### Directory Management
- The `sample_databases` directory is created automatically
- You can safely delete it to start fresh
- All sample databases are recreated on demand

### Database Updates
- Sample data is consistent across all databases
- Structure remains the same for compatibility
- New versions may add additional sample data

### Best Practices
1. **Backup**: 
   - Regularly backup the `sample_databases` directory
   - Keep copies of important test data

2. **Testing**: 
   - Use sample databases for testing new features
   - Keep production data separate
   - Test queries before applying to real data

3. **Development**: 
   - Use sample data for development
   - Test database operations
   - Validate queries

## ❓ Troubleshooting

### Common Issues

#### Database Creation
- **Error**: "Database engine not found"
  - Solution: Install required database engine
  - Example: MySQL Connector for MySQL databases

- **Error**: "Permission denied"
  - Solution: Run as administrator
  - Check file permissions

#### Connection Issues
- **Error**: "Connection refused"
  - Solution: Start database server
  - Check connection settings

- **Error**: "Authentication failed"
  - Solution: Verify credentials
  - Check database permissions

## 📚 Further Reading
- [Database Types](database_types.md)
- [SQL Queries](sql_queries.md)
- [Data Import/Export](data_import_export.md)
- [Troubleshooting](troubleshooting.md)
