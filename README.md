# Database Browser

[![Version](https://img.shields.io/badge/version-1.2.0--beta-blue.svg)](https://semver.org)

A Python-based GUI application for browsing and exporting database files. This application supports multiple database formats, including SQLite, Microsoft Access, MVO, and MySQL databases, allowing users to view contents in a table format and export data to CSV files.

## Version Information

- **Current Version**: 1.2.0-beta
- **Version Management**: Follows Semantic Versioning 2.0.0
- **Version Details**: 
  - Major: 1
  - Minor: 2
  - Patch: 0
  - Qualifier: beta

## Features

- Open and browse multiple database formats:
  - SQLite (.db, .sqlite)
  - Microsoft Access (.mdb, .accdb) with Jet OLEDB 3.51 support
  - MVO (.mvo) - Multiversion Object database files
  - MySQL (.sql)
- Comprehensive database exploration:
  - List and view tables
  - Export table data to CSV
  - Interactive table selection
- User-friendly graphical interface
- Robust error handling and user feedback
- Cross-platform compatibility

## Recent Updates

- Added full support for MySQL databases
- Improved database connection and table listing
- Enhanced CSV export functionality
- Modular code structure with separate modules for different database types
- Better error handling and user experience

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`

### Dependencies

- tkinter (GUI framework)
- sqlite3 (SQLite database operations)
- pyodbc (ODBC database connectivity)
- MySQLdb (MySQL database connectivity)
- csv (Data export)

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
