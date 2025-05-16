# Supported Database Types

This document provides detailed information about the database types supported by the DB Browser.

## Database Types Overview

| Database Type | File Extension | Required Dependencies | Notes |
|---------------|----------------|-----------------------|-------|
| SQLite        | .db            | None                  | Built-in Python support |
| MySQL         | .sql           | mysql-connector-python | Requires MySQL server |
| PostgreSQL    | .sql           | psycopg2             | Requires PostgreSQL server |
| Microsoft Access | .accdb, .mdb | Microsoft Access Database Engine | Windows only |
| MVO           | .mvo           | None                 | JSON-based storage |
| dBase         | .dbf           | dbf                  | Legacy database format |

## Database Connection Details

### Sample Database Directory
All sample databases created through the application are stored in the `sample_databases` directory:
- MySQL: `sample_databases/sample_mysql.sql`
- PostgreSQL: `sample_databases/sample_postgres.sql`
- SQLite: `sample_databases/sample_sqlite.db`
- Access: `sample_databases/sample.accdb`
- MVO: `sample_databases/sample.mvo`
- dBase: `sample_databases/sample.dbf`

### Additional Requirements

#### MySQL
- Install MySQL server
- Install `mysql-connector-python` package
- Default credentials: root/root

#### PostgreSQL
- Install PostgreSQL server
- Install `psycopg2` package
- Default credentials: postgres/postgres

#### Microsoft Access
- Install Microsoft Access Database Engine from: https://www.microsoft.com/en-us/download/details.aspx?id=54920
- Windows only

#### dBase
- Install `dbf` package
- Legacy database format support

## Database Features

### Common Features
- Browse and view tables
- View table structure
- Execute SQL queries
- Export data to CSV
- Import data from CSV

### Database-Specific Features

#### MySQL/PostgreSQL
- Support for server-based databases
- Connection pooling
- Transaction support
- Index management

#### SQLite
- File-based database
- No server required
- Lightweight and portable

#### Access
- Microsoft Office integration
- Form-based data entry
- Report generation

#### MVO
- JSON-based storage
- Schema-less design
- Easy data manipulation

#### dBase
- Legacy compatibility
- Fixed record length
- Simple structure
