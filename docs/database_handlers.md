# Database Handlers

## Overview

The Database Handlers module provides a unified, extensible interface for interacting with various database types. It abstracts away the complexities of different database connections and provides a consistent set of methods for database operations.

## Supported Database Types

- SQLite (.db)
  - File-based database
  - SQLite3 compatible
  - No server required
- MySQL (network)
  - Server-based database
  - Requires MySQL server
  - Supports transactions
- PostgreSQL (network)
  - Server-based database
  - Requires PostgreSQL server
  - Supports advanced features like JSON
- Microsoft Access (.mdb, .accdb)
  - File-based database
  - Requires Microsoft Access drivers
  - Legacy support
- Multiversion Object (.mvo)
  - File-based database
  - Legacy format
  - Multi-value fields support
- dBase (.dbf, .db3)
  - File-based database
  - Fixed-width fields
  - Legacy compatibility

## Core Components

### `get_database_handler()`

A factory method that automatically selects the appropriate database handler based on input.

#### Parameters
- `db_path` (optional): Path to a local database file
  - Required for file-based databases
  - Example: `get_database_handler(db_path='employees.db')`
- `connection_params` (optional): Dictionary of connection parameters for network databases
  - Required for server-based databases
  - Format:
    ```python
    {
        'type': 'mysql' or 'postgresql',  # Required
        'host': 'hostname',              # Required
        'user': 'username',              # Required
        'password': 'password',          # Required
        'database': 'database_name',     # Required
        'port': 3306 or 5432,           # Optional, defaults to standard port
        'timeout': 30,                   # Optional, connection timeout in seconds
        'charset': 'utf8mb4',            # Optional, character set
    }
    ```

#### Returns
An instance of a database handler with a consistent interface.

### Database Handler Interface

Each database handler implements the following methods:

- `connect()`: Establish a database connection
  - Raises `ConnectionError` on failure
  - Returns connection status
- `get_tables()`: List available tables
  - Returns list of table names
  - Raises `DatabaseError` if connection is closed
- `get_columns(table_name)`: Get table structure
  - Returns list of column definitions
  - Raises `TableNotFoundError` if table doesn't exist
- `get_data(table_name, limit=None)`: Get table data
  - Returns list of rows
  - Optional limit parameter
  - Raises `DatabaseError` on query failure
- `execute_query(query, params=None)`: Run a database query
  - Supports parameterized queries
  - Returns query results
  - Raises `QueryError` on failure
- `export_to_csv(table_name, output_path)`: Export table data to CSV
  - Creates CSV file with table data
  - Includes headers
  - Raises `ExportError` on failure
- `close()`: Close the database connection
  - Cleans up resources
  - Raises `ConnectionError` if already closed

### Error Handling

The database handlers implement a consistent error handling system:

```python
try:
    handler = get_database_handler(connection_params=params)
    handler.connect()
    
    # Execute operations
    tables = handler.get_tables()
    data = handler.get_data('employees')
    
except ConnectionError as e:
    print(f"Connection failed: {e}")
except DatabaseError as e:
    print(f"Database error: {e}")
except QueryError as e:
    print(f"Query failed: {e}")
except TableNotFoundError as e:
    print(f"Table not found: {e}")
except ExportError as e:
    print(f"Export failed: {e}")
finally:
    if handler:
        try:
            handler.close()
        except ConnectionError:
            pass

### Creating Custom Handlers

To create a custom database handler:

1. Create a new class that inherits from `BaseDatabasePlugin`
2. Implement all required methods from the interface
3. Add appropriate error handling
4. Place the handler in the `plugins/database_handlers` directory
5. The plugin manager will automatically discover and load your handler

Example:

```python
from plugins.base_plugin import BaseDatabasePlugin
from database_handlers import DatabaseError, ConnectionError

class CustomDatabaseHandler(BaseDatabasePlugin):
    def __init__(self):
        super().__init__()
        self.connection = None
        
    def connect(self):
        try:
            # Your connection logic here
            self.connection = self._create_connection()
            return True
        except Exception as e:
            raise ConnectionError(f"Failed to connect: {e}")
            
    def get_tables(self):
        if not self.connection:
            raise DatabaseError("Not connected")
        # Your table listing logic here
        return tables
        
    # Implement other required methods...
```

### Performance Considerations

1. Use parameterized queries to prevent SQL injection
2. Implement proper connection pooling for server-based databases
3. Use appropriate indexing for large datasets
4. Implement caching for frequently accessed data
5. Use batch operations for bulk data processing

### Security Best Practices

1. Never store passwords in code
2. Use environment variables for sensitive credentials
3. Implement proper error handling to prevent information leakage
4. Use prepared statements to prevent SQL injection
5. Implement connection timeouts
6. Use appropriate character encoding
7. Implement proper cleanup in finally blocks

### Testing Guidelines

1. Test connection for each database type
2. Verify table listing
3. Test query execution with various parameters
4. Test error handling
5. Test connection pooling
6. Test transaction handling
7. Test data export functionality
8. Test performance with large datasets

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
