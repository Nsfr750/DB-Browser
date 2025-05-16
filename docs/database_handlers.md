# Database Handlers

## Overview

The Database Handlers module provides a unified, extensible interface for interacting with various database types. It abstracts away the complexities of different database connections and provides a consistent set of methods for database operations.

## Supported Database Types

- SQLite (.db)
- MySQL (network)
- PostgreSQL (network)
- Microsoft Access (.mdb, .accdb)
- Multiversion Object (.mvo)
- dBase (.dbf, .db3)

## Core Components

### `get_database_handler()`

A factory method that automatically selects the appropriate database handler based on input.

#### Parameters
- `db_path` (optional): Path to a local database file
- `connection_params` (optional): Dictionary of connection parameters for network databases. Format:
  ```python
  {
    'type': 'mysql' or 'postgresql',
    'host': 'hostname',
    'user': 'username',
    'password': 'password',
    'database': 'database_name'
  }
  ```

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

# Get table structure
columns = sqlite_handler.get_columns('employees')

# Get data
data = sqlite_handler.get_data('employees')
```

### Network Database Connection

```python
from database_handlers import get_database_handler

# MySQL Connection
mysql_params = {
    'type': 'mysql',
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'mydb'
}
mysql_handler = get_database_handler(connection_params=mysql_params)
mysql_handler.connect()

# PostgreSQL Connection
postgres_params = {
    'type': 'postgresql',
    'host': 'localhost',
    'user': 'postgres',
    'password': 'password',
    'database': 'mydb'
}
postgres_handler = get_database_handler(connection_params=postgres_params)
postgres_handler.connect()

# Execute query
result = mysql_handler.execute_query("SELECT * FROM employees WHERE salary > %s", (50000,))
```

### Error Handling

```python
try:
    handler = get_database_handler(connection_params=params)
    handler.connect()
    # ... database operations ...
finally:
    if handler:
        handler.close()
```

### Plugin Integration

Database handlers can be extended through plugins. To create a custom database handler plugin:

1. Create a new handler class that inherits from `BaseDatabasePlugin`
2. Implement the required database handler methods
3. Place the plugin in the `plugins/database_handlers` directory
4. The plugin manager will automatically discover and load your handler

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
