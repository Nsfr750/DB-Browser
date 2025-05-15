# Database Browser

[![Version](https://img.shields.io/badge/version-1.2.0--beta-blue.svg)](https://semver.org)
[![Python Versions](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 🌟 Overview

Database Browser is a powerful, cross-platform GUI application designed to simplify database exploration and data management across multiple database formats.

## 🚀 Features

### Supported Databases
- 💾 SQLite (.db, .sqlite)
- 📊 Microsoft Access (.mdb, .accdb)
- 🗃️ MVO (Multiversion Object) (.mvo)
- 🐬 MySQL (.sql)

### Key Capabilities
- 📋 Browse and view database tables
- 📤 Export table data to CSV
- 🖥️ User-friendly graphical interface
- 🛡️ Robust error handling
- 🌐 Cross-platform compatibility

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip 21.0+

### Setup
1. Clone the repository
```bash
git clone https://github.com/yourusername/DB-Browser.git
cd DB-Browser
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

## 🖱️ Usage

Run the application:
```bash
python main.py
```

## 📝 Documentation

For detailed information, check our documentation:
- [User Guide](docs/index.md)
- [Development Guide](docs/development.md)

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

- **Current Version**: 1.2.0-beta
- **Version Management**: Semantic Versioning 2.0.0
  - Major: 1
  - Minor: 2
  - Patch: 0
  - Qualifier: beta

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📜 License

[Specify your license here, e.g., MIT]

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

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
python main.py
```

### Supported Databases
- SQLite (.db, .sqlite)
- Microsoft Access (.mdb, .accdb)
- MVO Databases (.mvo)
- MySQL (.sql)

## Contributing
Contributions are welcome! Please submit pull requests or open issues.

## License
[Add your license information here]

### Core Requirements
- Python 3.x
- tkinter (GUI framework, part of Python)
- sqlite3 (SQLite operations, part of Python)
- csv (Data export, part of Python)
- webbrowser (Sponsor links, part of Python)

### Additional Requirements for Access and MVO Databases
- pyodbc>=4.0.39 (for Access/Jet DB support)
- json (part of Python's standard library)
- Microsoft Access Database Engine (required for .mdb/.accdb files)

## Installation

1. Clone or download this repository
2. Ensure you have Python 3.x installed
3. Install required packages:
```bash
pip install -r requirements.txt
```
4. For Access database support, install the [Microsoft Access Database Engine](https://www.microsoft.com/en-us/download/details.aspx?id=54920)

## Usage

1. Run the application:
```bash
python main.py
```

2. Using the application:
   - Click "File" → "Open Database" to select a SQLite database file
   - If the database has multiple tables, select the desired table from the dialog
   - View the data in the table view
   - Use horizontal and vertical scrollbars to navigate large datasets
   - Click "File" → "Export to CSV" to save the current table data as a CSV file
   - Access "Help" → "About" for application information
   - View "Help" → "Sponsors" to see project supporters

## File Structure

- `main.py`: Entry point of the application
- `app.py`: Main application logic and GUI implementation
- `sponsor.py`: Sponsor information and support functionality
- `requirements.txt`: List of dependencies (all standard library)

## Features in Detail

### Database Operations
- Support for multiple database formats:
  - SQLite databases (*.db)
  - Microsoft Access databases (*.mdb, *.accdb)
  - MVO databases (*.mvo)
- Automatic database type detection
- Automatic table detection
- Support for multiple tables
- Safe database connection handling

### Data Display
- Scrollable table view
- Dynamic column headers
- Automatic column width adjustment
- Support for large datasets

### Data Export
- Export to CSV format
- Custom save location
- Preserve column headers
- Default filename based on table name

### Help and Support
- About dialog with application information
- Sponsors showcase with scrollable list
- Direct links to support the project
- Multiple support platforms (GitHub, Discord, PayPal, Patreon)

## Error Handling

The application includes comprehensive error handling for:
- Database connection issues
- Invalid database files
- Empty databases
- File access errors
- Export operations

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## Support the Project

You can support this project through various platforms:
- GitHub Sponsors
- Discord Community
- PayPal
- Patreon

Check the "Help" → "Sponsors" menu in the application for direct links.
