# Database Handlers

## Overview

The Database Handlers module provides a unified, extensible interface for interacting with various database types. It abstracts away the complexities of different database connections and provides a consistent set of methods for database operations.

## Supported Database Types

- SQLite (.db)
- MySQL (network)
- Microsoft Access (.mdb, .accdb)
- Multiversion Object (.mvo)
- dBase (.dbf, .db3)

## Core Components

### `get_database_handler()`

A factory method that automatically selects the appropriate database handler based on input.

#### Parameters
- `db_path` (optional): Path to a local database file
- `connection_params` (optional): Dictionary of connection parameters for network databases

#### Returns
An instance of a database handler with a consistent interface.

### Database Handler Interface

Each database handler implements the following methods:

- `connect()`: Establish a database connection
- `get_tables()`: List available tables
- `execute_query(query, params)`: Run a database query
- `export_to_csv(table_name, output_path)`: Export table data to CSV
- `close()`: Close the database connection

## Usage Examples

### File-based Database Connection

```python
from database_handlers import get_database_handler

# SQLite Connection
sqlite_handler = get_database_handler(db_path='employees.db')
sqlite_handler.connect()

# List tables
tables = sqlite_handler.get_tables()

# Execute query
results = sqlite_handler.execute_query('SELECT * FROM employees')

# Export to CSV
sqlite_handler.export_to_csv('employees', 'employees_export.csv')
sqlite_handler.close()
```

### Network Database Connection

```python
# MySQL Connection
mysql_handler = get_database_handler(connection_params={
    'type': 'mysql',
    'host': 'localhost',
    'user': 'username',
    'password': 'password',
    'database': 'company_db'
})
mysql_handler.connect()
```

## Error Handling

- Comprehensive logging of database operations
- Detailed error messages
- Consistent exception handling across database types

## Extending Database Support

To add support for a new database type:
1. Create a new handler class inheriting from `DatabaseHandler`
2. Implement required methods
3. Update `get_database_handler()` to recognize the new database type

## Best Practices

- Always use `connect()` and `close()` methods
- Handle potential exceptions
- Use parameterized queries to prevent SQL injection
- Export large datasets to CSV for analysis

## Logging

Database operations are logged with detailed information:
- Connection attempts
- Query executions
- Export operations
- Error messages

Logs are stored in `database_browser.log` by default.
