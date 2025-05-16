# Database Browser

[![Version](https://img.shields.io/badge/version-1.3.1--beta.1-blue.svg)](https://semver.org)
[![Python Versions](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 🌟 Overview

Database Browser is a powerful, cross-platform GUI application designed to simplify database exploration and data management across multiple database formats. It features a modular plugin system that allows for easy extension and customization.

## 🚀 Features

- Database Support
  - SQLite (.db)
  - MySQL (network) - Requires MySQL server
  - PostgreSQL (network) - Requires PostgreSQL server
  - Microsoft Access (.mdb, .accdb) - Requires Microsoft Access drivers
  - MVO (.mvo) - Legacy support
  - dBase (.dbf, .db3) - Legacy support
  - Plugin system for additional database types

- Data Operations
  - View table structure and data
  - Execute SQL queries
  - Import and export data
  - Create sample databases
  - Export to CSV
  - Comprehensive error handling

- User Interface
  - Modern, user-friendly graphical interface
  - Organized sample databases
  - Comprehensive help system (Ctrl+H)
  - Sponsor integration system
  - Cross-platform compatibility

- Development Features
  - Plugin system for extensibility
  - Comprehensive error handling
  - Version: 1.3.1-beta.1

### Database Handler Usage

The `get_database_handler()` function provides a unified interface for working with different database types. See [Database Handlers](Docs/database_handlers.md) for full documentation.

```python
from database_handlers import get_database_handler

# File-based database (SQLite)
sqlite_handler = get_database_handler(db_path='example.db')
sqlite_handler.connect()

# Network database (MySQL)
mysql_params = {
    'type': 'mysql',
    'host': 'localhost',
    'user': 'username',
    'password': 'password',
    'database': 'mydb'
}
mysql_handler = get_database_handler(connection_params=mysql_params)
mysql_handler.connect()

# Common operations
handler.get_tables()        # List all tables
handler.get_columns('table') # Get table structure
handler.get_data('table')    # Get table data
handler.execute_query('SELECT * FROM table')  # Execute query
handler.export_to_csv('table', 'output.csv')  # Export to CSV
handler.close()                              # Close connection
``

## 📦 Installation

1. Install Python 3.8 or higher
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## 🛠️ Development Setup

For developers:

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

## 📚 Documentation

For detailed documentation, see:

- [Database Handlers](Docs/database_handlers.md)
- [Sample Databases](Docs/sample_databases.md)
- [Development Guide](Docs/development.md)
- [Change Log](CHANGELOG.md)
- [Online Documentation](https://github.com/Nsfr750/DB-Browser/blob/main/docs/index.md)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🛠️ Troubleshooting

### Common Issues

1. Database Connection Problems
   - Verify database server is running
   - Check connection parameters
   - Ensure proper permissions
   - See [Troubleshooting Guide](Docs/database_handlers.md#troubleshooting)

2. File Access Issues
   - Check file permissions
   - Verify file path
   - Ensure file exists
   - See [File Access Guide](Docs/database_handlers.md#file-access)

3. Query Errors
   - Check SQL syntax
   - Verify table and column names
   - Check data types
   - See [Query Guide](Docs/database_handlers.md#query-execution)
   ```

## Additional Requirements for Specific Database Types

- **MySQL**: Install `mysql-connector-python`
- **PostgreSQL**: Install `psycopg2`
- **Microsoft Access**: Install Microsoft Access Database Engine from: https://www.microsoft.com/en-us/download/details.aspx?id=54920
- **dBase**: Install `dbf` package
- **MVO**: No additional requirements

## 🖱️ Usage

Run the application:
```bash
python main.py
```

## 📝 Documentation

For detailed information, check our documentation:
- [User Guide](docs/index.md)
- [Development Guide](docs/development.md)
- [Changelog](CHANGELOG.md)

## 🔧 Development

### Running Tests
```bash
pytest tests/
```

### Code Quality
```bash
flake8 .
```

## 📊 Version

- **Current Version**: 1.3.1-beta
- **Version Management**: Semantic Versioning 2.0.0
  - Major: 1
  - Minor: 3
  - Patch: 1
  - Qualifier: beta

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📜 License

MIT License

## 🆘 Support

For issues and feature requests, please use the GitHub Issues section.

## 🗺️ Roadmap

- [ ] Add more database format support
- [ ] Improve error handling
- [ ] Enhance export functionality
- [ ] Create comprehensive test suite

## 💡 Acknowledgments

- Python Community
- Open Source Contributors

## 🤝 Support the Project

You can support this project through various platforms:
- GitHub Sponsors
- Discord Community
- PayPal
- Patreon

Check the "Help" → "Sponsors" menu in the application for direct links.
