import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
import pyodbc
import csv
import os

class SQLiteApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Database Browser')
        self.create_widgets()
        self.conn = None
        self.current_table = None
        self.db_type = None  # 'sqlite' or 'jet'

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
        file_menu.add_command(label='Open Database', command=self.open_database)
        file_menu.add_command(label='Export to CSV', command=self.export_to_csv)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.root.quit)

        # Create Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Help', menu=help_menu)
        help_menu.add_command(label='About', command=self.show_about)
        help_menu.add_command(label='Sponsors', command=self.show_sponsors)

        # Create Treeview
        self.tree = ttk.Treeview(self.root)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Add scrollbars
        vsb = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(self.root, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        # Grid layout
        self.tree.grid(column=0, row=0, sticky='nsew')
        vsb.grid(column=1, row=0, sticky='ns')
        hsb.grid(column=0, row=1, sticky='ew')
        
        # Configure grid weights
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def open_database(self):
        try:
            db_path = filedialog.askopenfilename(
                title='Open Database',
                filetypes=[('All Databases', '*.db;*.mdb;*.accdb'), ('SQLite Database', '*.db'),
                          ('MS Access Database', '*.mdb;*.accdb'), ('All Files', '*.*')]
            )
            
            if not db_path:
                return
                
            self.load_database(db_path)
            
        except Exception as e:
            messagebox.showerror('Error', f'Error opening database: {str(e)}')
    
    def get_tables(self):
        cursor = self.conn.cursor()
        if self.db_type == 'sqlite':
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            return [table[0] for table in cursor.fetchall()]
        else:  # jet
            tables = [table[2] for table in cursor.tables(tableType='TABLE')]
            return [table for table in tables if not table.startswith('MSys')]

    def load_database(self, db_path):
        try:
            # Close existing connection if any
            if self.conn:
                self.conn.close()
                
            # Determine database type from extension
            ext = os.path.splitext(db_path)[1].lower()
            if ext == '.db':
                self.db_type = 'sqlite'
                self.conn = sqlite3.connect(db_path)
            elif ext in ['.mdb', '.accdb']:
                self.db_type = 'jet'
                conn_str = f'Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={db_path}'
                self.conn = pyodbc.connect(conn_str)
            else:
                raise ValueError('Unsupported database format')
                
            self.root.title(f'Database Browser - {os.path.basename(db_path)}')
            
            # Get list of tables
            tables = self.get_tables()
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
            
            # Query the selected table
            cursor = self.conn.cursor()
            cursor.execute(f'SELECT * FROM "{selected_table}"')
            rows = cursor.fetchall()

            # Clear the treeview
            self.tree.delete(*self.tree.get_children())

            # Get column names from cursor description
            columns = [description[0] for description in cursor.description]
            self.tree['columns'] = columns
            
            # Configure column headings
            for col in columns:
                self.tree.heading(col, text=col)
                self.tree.column(col, width=100)

            # Insert data into the treeview
            for row in rows:
                self.tree.insert('', 'end', values=row)
        except sqlite3.Error as e:
            messagebox.showerror('Database Error', str(e))

    def export_to_csv(self):
        try:
            if not self.conn:
                messagebox.showerror('Error', 'No database loaded!')
                return

            # Get list of tables
            tables = self.get_tables()
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

            cursor = self.conn.cursor()
            cursor.execute(f'SELECT * FROM "{selected_table}"')
            rows = cursor.fetchall()

            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                # Get column names from cursor description
                columns = [description[0] for description in cursor.description]
                writer.writerow(columns)
                writer.writerows(rows)
            
            messagebox.showinfo('Success', f'Data exported to {os.path.basename(file_path)}')
        
        except sqlite3.Error as e:
            messagebox.showerror('Database Error', str(e))
        except IOError as e:
            messagebox.showerror('File Error', f'Error writing to CSV file: {str(e)}')
            writer.writerow(['Column1', 'Column2', 'Column3'])  # Adjust column names
            writer.writerows(rows)

        messagebox.showinfo('Success', 'Data exported to output.csv')

    def show_about(self):
        about_dialog = tk.Toplevel(self.root)
        about_dialog.title('About Database Browser')
        about_dialog.geometry('400x300')
        about_dialog.transient(self.root)
        about_dialog.grab_set()

        # Add app icon or logo here if you have one
        title = ttk.Label(about_dialog, text='Database Browser', font=('Helvetica', 16, 'bold'))
        title.pack(pady=20)

        version = ttk.Label(about_dialog, text='Version 1.0')
        version.pack()

        description = ttk.Label(about_dialog, text='A simple and efficient tool for browsing\nand exporting SQLite and Access (Jet DB) databases.', justify=tk.CENTER)
        description.pack(pady=20)

        copyright = ttk.Label(about_dialog, text='© 2025 Nsfr750')
        copyright.pack(pady=10)

        ttk.Button(about_dialog, text='Close', command=about_dialog.destroy).pack(pady=20)

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
        try:
            if self.conn:
                self.conn.close()
        except Exception as e:
            print(f"Error closing database: {e}")
        self.root.quit()

if __name__ == '__main__':
    root = tk.Tk()
    app = SQLiteApp(root)
    root.protocol('WM_DELETE_WINDOW', app.close)
    root.mainloop()
