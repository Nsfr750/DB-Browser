import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
import os
from database_handlers import get_database_handler, DatabaseHandler
from sponsor import Sponsor

class SQLiteApp:
    def __init__(self, root, sponsor=None):
        self.root = root
        self.root.title('Database Browser')
        self.sponsor = sponsor
        self.create_widgets()
        self.conn = None
        self.current_table = None
        self.db_handler = None

    def ask_table_selection(self, tables):
        dialog = tk.Toplevel(self.root)
        dialog.title('Select Table')
        dialog.geometry('300x200')
        dialog.transient(self.root)
        dialog.grab_set()

        label = ttk.Label(dialog, text='Select a table to view:')
        label.pack(pady=10)

        table_var = tk.StringVar()
        table_list = ttk.Combobox(dialog, textvariable=table_var, values=tables, state='readonly')
        table_list.pack(pady=5)
        table_list.set(tables[0])

        selected_table = [None]

        def on_ok():
            selected_table[0] = table_var.get()
            dialog.destroy()

        def on_cancel():
            dialog.destroy()

        ttk.Button(dialog, text='OK', command=on_ok).pack(pady=5)
        ttk.Button(dialog, text='Cancel', command=on_cancel).pack(pady=5)

        dialog.wait_window()
        return selected_table[0]

    def create_widgets(self):
        # Create menu bar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Create File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='Open Database', command=self.open_database, accelerator='Ctrl+O')
        file_menu.add_command(label='Export to CSV', command=self.export_to_csv, accelerator='Ctrl+E')
        file_menu.add_separator()
        file_menu.add_command(label='Create Sample Database', command=self.create_sample_database)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.root.quit, accelerator='Ctrl+Q')

        # Create Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Help', menu=help_menu)
        help_menu.add_command(label='About', command=self.show_about, accelerator='F1')
        help_menu.add_command(label='Sponsors', command=self.show_sponsors)

    def show_sponsors(self):
        if self.sponsor:
            self.sponsor.show_sponsor()

    def create_sample_database(self):
        """Show dialog to create sample databases"""
        dialog = tk.Toplevel(self.root)
        dialog.title('Create Sample Database')
        dialog.geometry('400x350')  # Increased height to accommodate more options
        dialog.transient(self.root)
        dialog.grab_set()

        # Create frame for database options
        frame = ttk.Frame(dialog)
        frame.pack(padx=10, pady=10, fill='both', expand=True)

        # Add radio buttons for database types
        self.db_type = tk.StringVar(value='sqlite')
        
        sqlite_radio = ttk.Radiobutton(frame, text="SQLite Database", variable=self.db_type, value='sqlite')
        sqlite_radio.pack(anchor='w', pady=5)
        
        access_radio = ttk.Radiobutton(frame, text="Microsoft Access Database", variable=self.db_type, value='access')
        access_radio.pack(anchor='w', pady=5)
        
        mvo_radio = ttk.Radiobutton(frame, text="MVO Database", variable=self.db_type, value='mvo')
        mvo_radio.pack(anchor='w', pady=5)
        
        dbase_radio = ttk.Radiobutton(frame, text="dBase Database", variable=self.db_type, value='dbase')
        dbase_radio.pack(anchor='w', pady=5)
        
        mysql_radio = ttk.Radiobutton(frame, text="MySQL Database", variable=self.db_type, value='mysql')
        mysql_radio.pack(anchor='w', pady=5)
        
        postgres_radio = ttk.Radiobutton(frame, text="PostgreSQL Database", variable=self.db_type, value='postgres')
        postgres_radio.pack(anchor='w', pady=5)

        # Add description labels
        desc_frame = ttk.Frame(frame)
        desc_frame.pack(fill='x', pady=10)

        self.desc_label = ttk.Label(desc_frame, text="", wraplength=350)
        self.desc_label.pack()

        # Update description when selection changes
        self.db_type.trace('w', self.update_description)
        self.update_description()  # Initialize with SQLite description

        # Add buttons
        button_frame = ttk.Frame(frame)
        button_frame.pack(fill='x', pady=10)

        ttk.Button(button_frame, text='Create', command=lambda: self.create_selected_database(dialog)).pack(side='left', padx=5)
        ttk.Button(button_frame, text='Cancel', command=dialog.destroy).pack(side='left', padx=5)

        dialog.wait_window()

    def update_description(self, *args):
        """Update description based on selected database type"""
        db_type = self.db_type.get()
        if db_type == 'sqlite':
            self.desc_label.config(text="Create a sample SQLite database with Employees and Departments tables.")
        elif db_type == 'access':
            self.desc_label.config(text="Create a sample Microsoft Access database with Employees and Departments tables.")
        elif db_type == 'mvo':
            self.desc_label.config(text="Create a sample MVO database with JSON-based storage.")
        elif db_type == 'dbase':
            self.desc_label.config(text="Create a sample dBase database with Employees and Departments tables.")
        elif db_type == 'mysql':
            self.desc_label.config(text="Create a sample MySQL database with Employees and Departments tables.")
        elif db_type == 'postgres':
            self.desc_label.config(text="Create a sample PostgreSQL database with Employees and Departments tables.")

    def create_selected_database(self, dialog):
        """Create the selected sample database"""
        try:
            db_type = self.db_type.get()
            
            # Get the script path based on database type
            script_path = {
                'sqlite': 'create_sample_sqlite.py',
                'access': 'create_sample_access.py',
                'mvo': 'create_sample_mvo.py',
                'dbase': 'create_sample_dbase.py',
                'mysql': 'create_sample_mysql.py',
                'postgres': 'create_sample_sql.py'
            }.get(db_type)

            if not script_path:
                raise ValueError("Invalid database type selected")

            # Run the appropriate script
            import subprocess
            subprocess.run(['python', script_path])
            
            messagebox.showinfo('Success', f'Sample {db_type} database created successfully!\nConnection details saved in sample_databases directory.')
            dialog.destroy()

        except Exception as e:
            messagebox.showerror('Error', f'Failed to create sample database: {str(e)}')
            dialog.destroy()

        # Status bar
        self.status_bar = ttk.Label(self.root, text='Ready', relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Keyboard shortcuts
        self.root.bind('<Control-o>', lambda e: self.open_database())
        self.root.bind('<Control-e>', lambda e: self.export_to_csv())
        self.root.bind('<Control-q>', lambda e: self.root.quit())
        self.root.bind('<F1>', lambda e: self.show_about())
        self.root.bind('<Control-s>', lambda e: self.show_sponsors())

    def open_database(self):
        try:
            db_path = filedialog.askopenfilename(
                title='Open Database',
                filetypes=[
                    ('SQLite Database', '*.db'),
                    ('MySQL Database', '*.sql'),
                    ('Access Database', '*.accdb'),
                    ('dBase Database', '*.dbf *.db3'),
                    ('Microsoft Access Database', '*.mdb'),
                    ('PostgresSQL Database', '*.psql'),
                    ('Multiversion Object Database', '*.mvo'),
                    ('All Database Files', '*.db *.sql *.accdb *.dbf *.db3 *.psql *.mvo'),
                    ('All Files', '*.*')
                ])
            
            if not db_path:
                return
                
            self.load_database(db_path)
        
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def load_database(self, db_path):
        try:
            # Close any existing database handler
            if self.db_handler:
                self.db_handler.close()
            
            # Get the appropriate database handler
            self.db_handler = get_database_handler(db_path)
            
            if not self.db_handler:
                messagebox.showerror('Error', f'No handler found for database type: {db_path}')
                return
            
            self.db_handler.connect()
            
            # Get tables
            tables = self.db_handler.get_tables()
            
            if not tables:
                messagebox.showwarning('Warning', 'No tables found in the database')
                return
            
            # Ask user to select a table
            selected_table = self.ask_table_selection(tables)
            
            if selected_table:
                # Clear existing treeview
                for i in self.tree.get_children():
                    self.tree.delete(i)
                
                # Fetch and display table data
                query = f'SELECT * FROM {selected_table}'
                rows = self.db_handler.execute_query(query)
                
                if rows:
                    # Configure treeview columns
                    columns = list(rows[0].keys())
                    self.tree['columns'] = columns
                    for col in columns:
                        self.tree.heading(col, text=col)
                        self.tree.column(col, anchor='center', width=100)
                    
                    # Insert data
                    for row in rows:
                        self.tree.insert('', 'end', values=list(row.values()))
                
                # Update status bar
                self.status_bar.config(text=f'Loaded {selected_table} from {os.path.basename(db_path)}')
                self.current_table = selected_table
        
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def export_to_csv(self):
        try:
            if not self.db_handler:
                messagebox.showerror('Error', 'No database connection')
                return

            # Get list of tables
            tables = self.db_handler.get_tables()
            if not tables:
                messagebox.showwarning('Warning', 'No tables found in the database')
                return

            # If there's only one table, use it; otherwise ask user to select
            if len(tables) == 1:
                selected_table = tables[0]
            else:
                selected_table = self.ask_table_selection(tables)
                if not selected_table:
                    return

            # Ask user for save location
            file_path = filedialog.asksaveasfilename(
                defaultextension='.csv',
                filetypes=[('CSV files', '*.csv'), ('All files', '*.*')],
                initialfile=f'{selected_table}.csv'
            )

            if not file_path:
                return

            query = f'SELECT * FROM {selected_table}'
            rows = self.db_handler.execute_query(query)

            with open(file_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                # Get column names from cursor description
                columns = list(rows[0].keys())
                writer.writerow(columns)
                writer.writerows([list(row.values()) for row in rows])
            
            messagebox.showinfo('Success', f'Data exported to {os.path.basename(file_path)}')
        
        except Exception as e:
            messagebox.showerror('Export Error', str(e))

    def show_about(self):
        from about import About
        About.show_about(self.root)

    def show_sponsors(self):
        try:
            from sponsor import Sponsor
            sponsor = Sponsor(self.root)
            sponsor.show_sponsor()
        except ImportError:
            messagebox.showwarning('Sponsors', 'Sponsor information is not available.')
        except Exception as e:
            messagebox.showerror('Error', f'Error loading sponsor information: {str(e)}')

    def close(self):
        if self.db_handler:
            self.db_handler.close()
        self.root.quit()

if __name__ == '__main__':
    root = tk.Tk()
    app = SQLiteApp(root)
    root.protocol('WM_DELETE_WINDOW', app.close)
    root.mainloop()
