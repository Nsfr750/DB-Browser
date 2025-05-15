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
│
├── mysql_db.py             # MySQL database handler
├── mvo_db.py               # MVO database handler
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
   pip install pytest flake8
   ```

## Coding Standards

- Follow PEP 8 guidelines
- Use type hints
- Write docstrings for all functions and classes
- Maintain consistent code formatting

### Linting

Run flake8 to check code quality:
```bash
flake8 .
```

## Testing

### Running Tests

```bash
pytest tests/
```

### Test Coverage

- Aim for >80% test coverage
- Write unit tests for each module
- Include integration tests for database interactions

## Database Handlers

### Adding New Database Support

1. Create a new database handler module (e.g., `postgres_db.py`)
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
