# 📊 Supported Database Types

This document provides comprehensive information about all database types supported by DB Browser.

## 📋 Overview

DB Browser supports multiple database formats, each with its own characteristics and use cases. The following table summarizes the supported database types:

| Database Type | File Extension | Purpose | Key Features |
|---------------|----------------|----------|-------------|
| SQLite        | .db            | Lightweight storage | File-based, no server required, ACID-compliant |
| MySQL         | .sql           | Enterprise-level RDBMS | High performance, scalability, ACID-compliant |
| PostgreSQL    | .sql           | Advanced RDBMS | Advanced features, JSON support, ACID-compliant |
| Microsoft Access | .accdb, .mdb | Desktop database | Microsoft Office integration, form-based UI |
| MVO           | .mvo           | Flexible storage | Schema-less, JSON-based, easy to modify |
| dBase         | .dbf           | Legacy format | Fixed record length, simple structure |

## 🔍 Detailed Database Information

### SQLite Database
- **File-based**: No server installation required
- **ACID-compliant**: Ensures data integrity
- **Lightweight**: Ideal for small to medium applications
- **Portable**: Database is a single file
- **Example**: `sample_databases/sample_sqlite.db`

### MySQL Database
- **Server-based**: Requires MySQL server
- **High performance**: Optimized for large datasets
- **Scalable**: Supports millions of records
- **Example**: `sample_databases/sample_mysql.sql`
- **Connection Details**: 
  - Host: localhost
  - User: root
  - Password: root
  - Database: sample_db

### PostgreSQL Database
- **Advanced features**: JSON support, array types, full-text search
- **ACID-compliant**: Enterprise-grade reliability
- **Example**: `sample_databases/sample_postgres.sql`
- **Connection Details**: 
  - Host: localhost
  - User: postgres
  - Password: postgres
  - Database: sample_db

### Microsoft Access Database
- **Windows-only**: Requires Microsoft Access Database Engine
- **Form-based**: Easy data entry interface
- **Example**: `sample_databases/sample.accdb`
- **Download**: [Microsoft Access Database Engine](https://www.microsoft.com/en-us/download/details.aspx?id=54920)

### MVO Database
- **JSON-based**: Flexible schema
- **Schema-less**: Easy to modify structure
- **Example**: `sample_databases/sample.mvo`
- **Structure**: 
  ```json
  {
    "employees": [
      {
        "id": 1,
        "name": "John Doe",
        "position": "Manager"
      }
    ]
  }
  ```

### dBase Database
- **Legacy format**: Fixed record length
- **Simple structure**: Easy to understand
- **Example**: `sample_databases/sample.dbf`
- **Structure**: 
  ```
  Field Name: ID     Type: N     Length: 4
  Field Name: NAME   Type: C     Length: 50
  Field Name: POS    Type: C     Length: 50
  ```

## 🏗️ Database Operations

### Common Operations
- **Table Management**: Create, modify, delete tables
- **Data Manipulation**: CRUD operations
- **Data Export**: CSV, JSON, Excel
- **Data Import**: CSV, JSON
- **SQL Queries**: Complex queries supported

### Database-Specific Operations

#### MySQL/PostgreSQL
- **Transactions**: ACID-compliant
- **Indexes**: Performance optimization
- **Views**: Virtual tables
- **Stored Procedures**: Complex business logic

#### SQLite
- **File Management**: Backup/restore
- **Encryption**: Secure storage
- **Memory Database**: In-memory operations

#### Access
- **Forms**: Data entry interfaces
- **Reports**: Data visualization
- **Macros**: Automation

#### MVO
- **Dynamic Schema**: Modify structure on-the-fly
- **Embedded JSON**: Complex data structures
- **Version Control**: Track changes

#### dBase
- **Fixed Records**: Consistent data structure
- **Memo Files**: Large text storage
- **Index Files**: Performance optimization

## 📝 Best Practices

### General
- Always backup your databases
- Use meaningful table and column names
- Implement proper indexing
- Regular maintenance

### Database-Specific

#### MySQL/PostgreSQL
- Use transactions for data integrity
- Implement proper indexing
- Regular database maintenance
- Use connection pooling

#### SQLite
- Use WAL mode for better concurrency
- Implement proper vacuuming
- Use PRAGMA statements for optimization

#### Access
- Split database for better performance
- Use proper form design
- Regular compact/repair

#### MVO
- Use consistent JSON structure
- Implement proper validation
- Regular data backup

#### dBase
- Use proper record length
- Implement proper indexing
- Regular maintenance

## ❌ Common Pitfalls

### Performance
- Not using proper indexing
- Large result sets without limits
- Complex joins without optimization

### Data Integrity
- Not using transactions
- Inconsistent data types
- Missing validation

### Security
- Using default credentials
- Not encrypting sensitive data
- Improper access control

## 📚 Further Reading
- [Sample Databases](sample_databases.md)
- [Database Operations](database_operations.md)
- [SQL Queries](sql_queries.md)
- [Troubleshooting](troubleshooting.md)
