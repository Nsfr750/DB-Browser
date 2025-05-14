# SQLite Database Browser

A Python-based GUI application for browsing and exporting SQLite database files. This application allows users to open any SQLite database file, view its contents in a table format, and export the data to CSV files.

## Features

- Open and browse any SQLite database file
- Support for multiple tables within a database
- Interactive table selection for databases with multiple tables
- Data displayed in a scrollable table view with column headers
- Export table data to CSV files
- User-friendly interface with menu-based navigation
- About and Sponsors information
- Sponsor support through various platforms
- Proper error handling and user feedback

## Requirements

All dependencies are part of Python's standard library:
- Python 3.x
- tkinter (GUI framework)
- sqlite3 (Database operations)
- webbrowser (Sponsor links)
- csv (Data export)

## Installation

1. Clone or download this repository
2. Ensure you have Python 3.x installed
3. No additional package installation is required

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
- Open any SQLite database file (*.db)
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
