# Development Guide

## Project Structure

```
DB-Browser/
│
├── docs/                   # Documentation files
├── tests/                  # Unit and integration tests
├── plugins/                # Plugin system
│   ├── database_handlers/  # Database handler plugins
│   ├── ui_plugins/        # UI component plugins
│   └── export_plugins/    # Data export plugins
├── sample_databases/       # Sample database creation scripts
│   ├── create_sample_sqlite.py
│   ├── create_sample_access.py
│   ├── create_sample_mysql.py
│   ├── create_sample_postgres.py
│   └── create_sample_mvo.py
│
├── src/                    # Source code
│   ├── app/               # Main application code
│   │   ├── __init__.py
│   │   ├── main.py        # Application entry point
│   │   └── ui/           # UI components
│   │       ├── __init__.py
│   │       ├── main_window.py
│   │       ├── table_view.py
│   │       └── query_editor.py
│   ├── database_handlers/ # Database handler implementations
│   │   ├── __init__.py
│   │   ├── sqlite_handler.py
│   │   ├── mysql_handler.py
│   │   ├── postgres_handler.py
│   │   └── access_handler.py
│   ├── plugins/           # Core plugin system
│   │   ├── __init__.py
│   │   └── base_plugin.py
│   └── utils/             # Utility functions
│       ├── __init__.py
│       └── helpers.py
├── tests/                  # Unit and integration tests
│   ├── __init__.py
│   ├── test_database_handlers.py
│   ├── test_ui.py
│   └── test_plugins.py
├── requirements.txt        # Project dependencies
└── requirements-dev.txt    # Development dependencies
```

## Development Environment Setup

1. Clone the repository
2. Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install development dependencies
   ```bash
   pip install -r requirements-dev.txt
   ```

## Development Guidelines

### Code Style

- Follow PEP 8 guidelines
- Use type hints for all functions and methods
- Write comprehensive docstrings using Google style
- Use meaningful variable and function names
- Keep lines under 100 characters
- Use snake_case for variables and functions
- Use PascalCase for classes
- Use UPPER_CASE for constants

### Project Structure

1. All source code should be in the `src` directory
2. Tests should be in the `tests` directory
3. Plugins should be in the appropriate subdirectory under `plugins`
4. Sample database scripts should be in `sample_databases`
5. Documentation should be in `docs`

### Database Handler Development

#### Requirements

1. Inherit from `BaseDatabasePlugin`
2. Implement all required interface methods
3. Add appropriate error handling
4. Include unit tests
5. Document all methods and parameters

#### Implementation Guidelines

1. Use connection pooling for server-based databases
2. Implement proper error handling
3. Use parameterized queries to prevent SQL injection
4. Add timeout handling
5. Implement proper cleanup in finally blocks

#### Testing

1. Test connection handling
2. Test table listing
3. Test query execution
4. Test error conditions
5. Test performance with large datasets
6. Test data export functionality

### Plugin Development

#### Plugin Types

1. Database Handlers
   - Handle specific database types
   - Implement database operations
   - Manage connections

2. UI Components
   - Add new interface elements
   - Extend existing UI
   - Implement custom controls

3. Export Plugins
   - Add new data export formats
   - Implement data transformation
   - Handle file formats

#### Plugin Structure

```python
from plugins.base_plugin import BasePlugin

class YourPlugin(BasePlugin):
    def __init__(self):
        super().__init__()
        self.name = "Your Plugin Name"
        self.description = "Plugin description"
        self.version = "1.0"

    def initialize(self, root):
        """Initialize the plugin"""
        pass

    def cleanup(self):
        """Cleanup resources"""
        pass

    # Implement plugin-specific methods
```

#### Plugin Registration

1. Place plugin files in the appropriate directory:
   - Database handlers: `plugins/database_handlers/`
   - UI components: `plugins/ui_plugins/`
   - Export plugins: `plugins/export_plugins/`

2. The plugin manager will automatically discover and load your plugin

### Error Handling

1. Use specific exception types
2. Provide meaningful error messages
3. Implement proper cleanup in finally blocks
4. Log errors appropriately
5. Handle connection timeouts
6. Prevent resource leaks

### Performance Considerations

1. Use connection pooling for server-based databases
2. Implement proper caching
3. Use batch operations for bulk data
4. Optimize queries
5. Monitor memory usage
6. Implement proper error handling

### Security Best Practices

1. Never store passwords in code
2. Use environment variables for sensitive data
3. Implement proper error handling
4. Use prepared statements
5. Implement connection timeouts
6. Use appropriate character encoding
7. Implement proper cleanup
8. Validate all inputs

### Testing Guidelines

1. Write unit tests for all components
2. Test error conditions
3. Test edge cases
4. Test performance
5. Test integration points
6. Test data export
7. Test UI components
8. Test database handlers
9. Test plugins

### Version Control

1. Use Git for version control
2. Create feature branches
3. Write meaningful commit messages
4. Use pull requests for code review
5. Tag releases
6. Update changelog

### Documentation

1. Document all public APIs
2. Write usage examples
3. Include error handling examples
4. Document configuration options
5. Keep documentation up to date
6. Include installation instructions
7. Document dependencies
8. Include troubleshooting guide

## Development Guidelines

### Code Style

- Follow PEP 8 guidelines
- Use type hints
- Write docstrings for all functions and classes
- Maintain consistent code formatting

### Database Handler Development

#### Adding New Database Support

1. Create a new handler class in `database_handlers.py`
2. Inherit from `DatabaseHandler`
3. Implement these required methods:
   - `_validate_connection_params()`
   - `_establish_connection()`
   - `get_tables()`
   - `execute_query()`
   - `export_to_csv()`
   - `close()`

#### Example Handler Template

```python
class NewDatabaseHandler(DatabaseHandler):
    def __init__(self, db_path_or_params):
        super().__init__(db_path_or_params)
        self.connection = None

    def _validate_connection_params(self):
        # Validate input parameters
        pass

    def _establish_connection(self):
        # Create database connection
        pass

    def get_tables(self) -> List[str]:
        # Return list of tables
        pass

    def execute_query(self, query: str, params: tuple = None) -> List[Dict[str, Any]]:
        # Execute database query
        pass

    def export_to_csv(self, table_name: str, output_path: str):
        # Export table to CSV
        pass

    def close(self):
        # Close database connection
        pass
```

### Sponsor System Integration

The sponsor system is implemented in `sponsor.py` and provides:

1. Integration with multiple sponsorship platforms
   - GitHub Sponsors
   - Patreon
   - PayPal
   - Discord Community

2. Sponsor information display
   - Sponsor profiles
   - Support links
   - Contribution tiers

3. Integration points
   - Help menu → Sponsors
   - About dialog
   - Application footer

### Sample Database Scripts

The project includes sample database creation scripts in Python:

1. `create_sample_sqlite.py`
   - Creates a sample SQLite database
   - Includes Employees and Departments tables
   - Demonstrates basic SQLite operations

2. `create_sample_access.py`
   - Creates a sample Microsoft Access database
   - Uses Jet OLEDB 3.51 driver
   - Requires Microsoft Access Database Engine

3. `create_sample_mvo.py`
   - Creates a sample MVO database
   - JSON-based storage
   - Demonstrates MVO database structure

### Keyboard Shortcuts

The application supports the following keyboard shortcuts:

- Ctrl+O: Open Database
- Ctrl+E: Export to CSV
- Ctrl+Q: Quit Application
- F1: Show About Dialog
- Ctrl+S: Show Sponsors

### Testing

The project includes a comprehensive test suite in the `tests/` directory. To run tests:

```bash
pytest tests/
```

### Code Quality

To check code quality:

```bash
flake8 .
```

1. Integration with multiple sponsorship platforms
   - GitHub Sponsors
   - Patreon
   - PayPal
   - Discord Community

2. Sponsor information display
   - Sponsor profiles
   - Support links
   - Contribution tiers

3. Integration points
   - Help menu → Sponsors
   - About dialog
   - Application footer

### Sample Database Scripts

The project includes sample database creation scripts in Python:

1. `create_sample_sqlite.py`
   - Creates a sample SQLite database
   - Includes Employees and Departments tables
   - Demonstrates basic SQLite operations

2. `create_sample_access.py`
   - Creates a sample Microsoft Access database
   - Uses Jet OLEDB 3.51 driver
   - Requires Microsoft Access Database Engine

3. `create_sample_mvo.py`
   - Creates a sample MVO database
   - JSON-based storage
   - Demonstrates MVO database structure

### Linting

Run flake8 to check code quality:
```bash
flake8 .
```

## Testing

- Write unit tests for all new features
- Use pytest for testing
- Ensure 80% code coverage

#### Database Handler Testing

- Test connection for each database type
- Verify table listing
- Test query execution
- Check CSV export functionality
- Validate error handling

##### Example Test Cases

```python
def test_database_handler_connection():
    handler = get_database_handler(db_path='test.db')
    assert handler is not None
    handler.connect()
    assert handler.get_tables() is not None
    handler.close()

def test_database_query_execution():
    handler = get_database_handler(db_path='test.db')
    handler.connect()
    results = handler.execute_query('SELECT * FROM test_table')
    assert len(results) > 0
    handler.close()
```
2. Implement standard methods:
   - `get_connection_details()`
   - `list_tables()`
   - Error handling

## Version Management

- Update `version.py` for new releases
- Follow Semantic Versioning
- Add changelog entries

## Pull Request Process

1. Ensure all tests pass
2. Update documentation
3. Add description of changes
4. Request code review

## Debugging

- Use logging instead of print statements
- Provide detailed error messages
- Catch and handle specific exceptions

## Performance Considerations

- Optimize database queries
- Use efficient data structures
- Minimize memory usage for large databases

## Security

- Never hardcode database credentials
- Use secure connection methods
- Validate and sanitize user inputs
