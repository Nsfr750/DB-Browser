# Development Guide

## Project Structure

```
DB-Browser/
│
├── docs/                   # Documentation files
├── tests/                  # Unit and integration tests
│
├── main.py                 # Application entry point
├── app.py                  # Main application logic
├── version.py              # Version management
├── about.py                # About dialog implementation
├── sponsor.py              # Sponsor system implementation
├── sample_databases/       # Sample database creation scripts
│   ├── create_sample_sqlite.py
│   ├── create_sample_access.py
│   └── create_sample_mvo.py
│
├── mysql_db.py             # MySQL database handler
├── mvo_db.py               # MVO database handler
├── postgres_db.py          # PostgreSQL database handler
│
└── requirements.txt        # Project dependencies
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
   pip install -r requirements.txt
   pip install pytest
   ```

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
