import MySQLdb
import tkinter as tk
from tkinter import messagebox, simpledialog

class MySQLDatabase:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = MySQLdb.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.database
            )
            self.cursor = self.connection.cursor()
            return True
        except MySQLdb.Error as e:
            messagebox.showerror("Connection Error", f"Failed to connect to MySQL database: {e}")
            return False

    def disconnect(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            self.connection = None
            self.cursor = None

    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            return True
        except MySQLdb.Error as e:
            messagebox.showerror("Query Error", f"Failed to execute query: {e}")
            return False

    def fetch_data(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except MySQLdb.Error as e:
            messagebox.showerror("Fetch Error", f"Failed to fetch data: {e}")
            return None

    @staticmethod
    def get_connection_details():
        root = tk.Tk()
        root.withdraw()  # Hide the main window

        host = simpledialog.askstring("MySQL Connection", "Enter MySQL Host:", initialvalue="localhost")
        if not host:
            return None

        user = simpledialog.askstring("MySQL Connection", "Enter MySQL Username:")
        if not user:
            return None

        password = simpledialog.askstring("MySQL Connection", "Enter MySQL Password:", show='*')
        if password is None:
            return None

        database = simpledialog.askstring("MySQL Connection", "Enter Database Name:")
        if not database:
            return None

        return {
            'host': host,
            'user': user,
            'password': password,
            'database': database
        }
