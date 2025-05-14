# Database Browser

A Python-based GUI application for browsing and exporting database files. This application supports SQLite, Microsoft Access (Jet DB), and MVO (Multiversion Object) databases, allowing users to view contents in a table format and export data to CSV files.

## Features

- Open and browse multiple database formats:
  - SQLite (.db)
  - Microsoft Access (.mdb, .accdb)
  - MVO (.mvo) - Multiversion Object database files
- Export data to CSV files
- Support for multiple tables within a database
- Interactive table selection for databases with multiple tables
- Data displayed in a scrollable table view with column headers
- Export table data to CSV files
- User-friendly interface with menu-based navigation
- About and Sponsors information
- Sponsor support through various platforms
- Proper error handling and user feedback

## Requirements

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
