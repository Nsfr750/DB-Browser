# Database Browser

[![Version](https://img.shields.io/badge/version-1.3.1--beta.1-blue.svg)](https://semver.org)
[![Python Versions](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 🌟 Overview

Database Browser is a powerful, cross-platform GUI application designed to simplify database exploration and data management across multiple database formats.

## 🚀 Features

- Browse and query multiple database formats:
  - SQLite
  - Microsoft Access
  - MySQL
  - PostgreSQL
  - MVO
  - dBase
- View table structure and data
- Execute SQL queries
- Import and export data
- Create sample databases for testing
- Organized sample databases in dedicated directory.

### Supported Databases
- 💾 SQLite (.db)
- 🐬 MySQL
- 🐘 PostgreSQL
- 📊 dBase (.dbf, .db3)
- 📊 Microsoft Access (.mdb, .accdb)
- 🗃️ MVO (Legacy support)

### Key Capabilities
- 📋 Browse and view database tables
- 📤 Export table data to CSV
- 🖥️ User-friendly graphical interface
- 🔌 Modular database handler architecture
- 🛡️ Robust error handling
- 🌐 Cross-platform compatibility
- 💡 Sponsor integration system
- 🏷️ Version: 1.3.1-beta.1

### Database Handler Usage

The `get_database_handler()` function in `database_handlers.py` provides a unified interface for working with different database types:

```python
from database_handlers import get_database_handler

# For file-based databases
handler = get_database_handler(db_path='example.db')

# For network databases
handler = get_database_handler(connection_params={
    'type': 'mysql',
    'host': 'localhost',
    'user': 'username',
    'password': 'password',
    'database': 'mydb'
})

# Common methods
handler.connect()
tables = handler.get_tables()
results = handler.execute_query('SELECT * FROM mytable')
handler.export_to_csv('mytable', 'output.csv')
handler.close()
```

## 📦 Installation

1. Install Python 3.8 or higher
2. Install required packages:
   ```bash
   pip install -r requirements.txt
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
