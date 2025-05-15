# Database Browser Documentation

## Overview

Database Browser is a powerful, cross-platform GUI application designed to simplify database exploration and data export across multiple database formats.

## Features

### Supported Database Types
- SQLite (.db)
- MySQL (network)
- Microsoft Access (.mdb, .accdb)
- Multiversion Object (.mvo)
- dBase (.dbf, .db3)

### Key Capabilities
- Universal Database Handler
  - Unified interface across database types
  - Automatic handler selection
  - Consistent method signatures

- Database Operations
  - Browse database tables
  - Execute custom queries
  - Export table data to CSV
  - Robust connection management

### Advanced Features
- Comprehensive logging
- Detailed error handling
- Cross-platform compatibility
- Extensible architecture

## Installation

### Prerequisites
- Python 3.8+
- Required dependencies:
  ```
  pip install pyodbc mysqlclient sqlite3
  ```

### Configuration
Database connections can be configured using:
- File paths for local databases
- Connection parameters for network databases

#### Example Connection
```python
from database_handlers import get_database_handler

# SQLite Connection
handler = get_database_handler(db_path='example.db')

# MySQL Connection
handler = get_database_handler(connection_params={
    'type': 'mysql',
    'host': 'localhost',
    'user': 'username',
    'password': 'password',
    'database': 'mydb'
})
```
- pip 21.0+

### Dependencies

Install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

```bash
python main.py
```

### Supported Database Formats

1. **SQLite** (.db, .sqlite)
   - Lightweight, serverless database
   - Direct file-based storage

2. **Microsoft Access** (.mdb, .accdb)
   - Uses Jet OLEDB 3.51 driver
   - Supports legacy Access databases

3. **MVO** (.mvo)
   - Multiversion Object database
   - Specialized database format

4. **MySQL** (.sql)
   - Requires database connection details
   - Supports remote and local MySQL databases

## Configuration

### Database Connection

- For MySQL, provide connection details in the connection dialog
- Supports host, username, password, and database name

## Versioning

The project follows Semantic Versioning 2.0.0.

- **Current Version**: 1.2.0-beta
- Version format: MAJOR.MINOR.PATCH
- Qualifier: beta, alpha, rc

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Specify your license here, e.g., MIT, GPL]

## Support

For issues and feature requests, please use the GitHub Issues section.

## Development

### Running Tests

```bash
pytest tests/
```

### Code Linting

```bash
flake8 .
```

## Roadmap

- [ ] Add more database format support
- [ ] Improve error handling
- [ ] Enhance export functionality
- [ ] Create comprehensive test suite
