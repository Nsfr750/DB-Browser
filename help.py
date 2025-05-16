import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import webbrowser
from urllib.parse import quote

class HelpSystem:
    def __init__(self, parent):
        self.parent = parent
        self.help_window = None
        self.current_section = "Introduction"
        
        # Store help content
        self.help_content = {
            "Introduction": """
Database Browser Help System
==========================

Welcome to Database Browser! This application allows you to explore and manage multiple database formats through a user-friendly interface.

Main Features:
- Browse and query multiple database types
- View table structure and data
- Execute SQL queries
- Import and export data
- Create sample databases for testing
- Cross-platform compatibility
            """,
            "Getting Started": """
Getting Started
==============

1. Launch the Application
   - Run main.py to start the application
   - The main window will appear with database selection options

2. Select Database Type
   - Choose from available database types:
     - SQLite (.db)
     - MySQL (network)
     - PostgreSQL (network)
     - Microsoft Access (.mdb, .accdb)
     - MVO (.mvo)
     - dBase (.dbf, .db3)

3. Create or Connect
   - For file-based databases: Select a file or create a new one
   - For network databases: Enter connection parameters
            """,
            "Database Operations": """
Database Operations
==================

1. Viewing Data
   - Browse tables in the database
   - View table structure (columns)
   - Browse table data
   - Export data to CSV

2. Querying Data
   - Use the query editor to write SQL queries
   - Execute queries and view results
   - Save query results

3. Managing Connections
   - Open multiple database connections
   - Switch between connections
   - Close connections when done
            """,
            "Sample Databases": """
Sample Databases
===============

The application includes sample databases for testing:

1. SQLite Sample
   - Contains an employees table with sample data
   - Located in sample_databases/sample_sqlite.db

2. MySQL Sample
   - Contains employees and departments tables
   - Located in sample_databases/sample_mysql.sql

3. PostgreSQL Sample
   - Contains employees and departments tables
   - Located in sample_databases/sample_postgres.sql

4. Access Sample
   - Contains sample business data
   - Located in sample_databases/sample_access.mdb
            """,
            "Troubleshooting": """
Troubleshooting
==============

Common Issues:

1. Connection Problems
   - Verify database server is running
   - Check connection parameters
   - Ensure proper permissions

2. File Access Issues
   - Check file permissions
   - Verify file path
   - Ensure file exists

3. Query Errors
   - Check SQL syntax
   - Verify table and column names
   - Check data types
            """,
            "About": """
About Database Browser
=====================

Version: 1.3.1-beta.1

License: MIT

Source Code: https://github.com/Nsfr750/DB-Browser

For more information, visit our documentation at:
https://github.com/Nsfr750/DB-Browser/blob/main/Docs/index.md
            """
        }

    def show_help(self):
        """Show the help window"""
        if self.help_window:
            self.help_window.lift()
            return

        self.help_window = tk.Toplevel(self.parent)
        self.help_window.title("Database Browser Help")
        self.help_window.geometry("800x600")

        # Create main frame
        main_frame = ttk.Frame(self.help_window)
        main_frame.pack(fill='both', expand=True, padx=5, pady=5)

        # Create left frame for section selection
        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side='left', fill='y', padx=(0, 5))

        # Create right frame for content display
        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side='right', fill='both', expand=True)

        # Add section selection
        section_label = ttk.Label(left_frame, text="Sections:")
        section_label.pack(pady=(0, 5))

        # Create section buttons
        for section in self.help_content.keys():
            button = ttk.Button(
                left_frame,
                text=section,
                command=lambda s=section: self.show_section(s)
            )
            button.pack(fill='x', pady=2)

        # Add content display
        self.content_text = scrolledtext.ScrolledText(
            right_frame,
            wrap='word',
            width=80,
            height=30
        )
        self.content_text.pack(fill='both', expand=True)

        # Add search functionality
        search_frame = ttk.Frame(right_frame)
        search_frame.pack(fill='x', pady=(5, 0))

        search_label = ttk.Label(search_frame, text="Search:")
        search_label.pack(side='left', padx=(0, 5))

        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side='left', fill='x', expand=True)
        search_entry.bind('<KeyRelease>', self.search_content)

        # Add online documentation link
        docs_button = ttk.Button(
            right_frame,
            text="View Online Documentation",
            command=self.open_online_docs
        )
        docs_button.pack(pady=(5, 0))

        # Show initial section
        self.show_section("Introduction")

    def show_section(self, section):
        """Show the selected section"""
        self.current_section = section
        content = self.help_content.get(section, "Section not found")
        self.content_text.delete(1.0, tk.END)
        self.content_text.insert(tk.END, content)

    def search_content(self, event):
        """Search through help content"""
        query = self.search_var.get().lower()
        if not query:
            self.show_section(self.current_section)
            return

        # Search through all sections
        search_results = []
        for section, content in self.help_content.items():
            if query in content.lower():
                search_results.append((section, content))

        if search_results:
            self.content_text.delete(1.0, tk.END)
            self.content_text.insert(tk.END, "Search Results:\n\n")
            for section, content in search_results:
                self.content_text.insert(tk.END, f"=== {section} ===\n\n")
                self.content_text.insert(tk.END, content)
                self.content_text.insert(tk.END, "\n\n")
        else:
            self.content_text.delete(1.0, tk.END)
            self.content_text.insert(tk.END, "No results found for: " + query)

    def open_online_docs(self):
        """Open online documentation"""
        url = "https://github.com/Nsfr750/DB-Browser/blob/main/docs/index.md"
        webbrowser.open(url)

    def close_help(self):
        """Close the help window"""
        if self.help_window:
            self.help_window.destroy()
            self.help_window = None
