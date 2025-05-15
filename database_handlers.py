import sqlite3
import pyodbc
import MySQLdb
from typing import List, Dict, Any
import csv
import os

class DatabaseHandler:
    def __init__(self, db_path: str = None, connection_params: Dict[str, Any] = None):
        self.db_path = db_path
        self.connection_params = connection_params
        self.conn = None
        self.cursor = None

    def connect(self):
        raise NotImplementedError("Subclasses must implement connect method")

    def get_tables(self) -> List[str]:
        raise NotImplementedError("Subclasses must implement get_tables method")

    def execute_query(self, query: str, params: tuple = None) -> List[Dict[str, Any]]:
        raise NotImplementedError("Subclasses must implement execute_query method")

    def export_to_csv(self, table_name: str, output_path: str):
        raise NotImplementedError("Subclasses must implement export_to_csv method")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

class SQLiteHandler(DatabaseHandler):
    def connect(self):
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def get_tables(self) -> List[str]:
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return [table[0] for table in self.cursor.fetchall()]

    def execute_query(self, query: str, params: tuple = None) -> List[Dict[str, Any]]:
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]

    def export_to_csv(self, table_name: str, output_path: str):
        query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        headers = [description[0] for description in self.cursor.description]
        
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(self.cursor.fetchall())

class MySQLHandler(DatabaseHandler):
    def connect(self):
        self.conn = MySQLdb.connect(
            host=self.connection_params.get('host', 'localhost'),
            user=self.connection_params.get('user', ''),
            passwd=self.connection_params.get('password', ''),
            db=self.connection_params.get('database', '')
        )
        self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)

    def get_tables(self) -> List[str]:
        self.cursor.execute("SHOW TABLES")
        return [table[0] for table in self.cursor.fetchall()]

    def execute_query(self, query: str, params: tuple = None) -> List[Dict[str, Any]]:
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        
        return self.cursor.fetchall()

    def export_to_csv(self, table_name: str, output_path: str):
        query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        headers = [column[0] for column in self.cursor.description]
        
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(self.cursor.fetchall())

class PostgreSQLHandler(DatabaseHandler):
    def __init__(self, connection_params: Dict[str, Any]):
        super().__init__(connection_params=connection_params)
        import psycopg2
        import psycopg2.extras

    def connect(self):
        self.conn = psycopg2.connect(
            host=self.connection_params.get('host', 'localhost'),
            user=self.connection_params.get('user', ''),
            password=self.connection_params.get('password', ''),
            database=self.connection_params.get('database', '')
        )
        self.cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def get_tables(self) -> List[str]:
        self.cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
        """)
        return [table[0] for table in self.cursor.fetchall()]

    def execute_query(self, query: str, params: tuple = None) -> List[Dict[str, Any]]:
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        
        return [dict(row) for row in self.cursor.fetchall()]

    def export_to_csv(self, table_name: str, output_path: str):
        query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        headers = [desc.name for desc in self.cursor.description]
        
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(self.cursor.fetchall())

def get_database_handler(db_path: str = None, connection_params: Dict[str, Any] = None) -> DatabaseHandler:
    """
    Factory method to create the appropriate database handler based on input.
    
    :param db_path: Path to the database file
    :param connection_params: Dictionary of connection parameters
    :return: Appropriate DatabaseHandler instance
    """
    if db_path:
        # File-based databases
        if db_path.endswith('.db'):
            return SQLiteHandler(db_path)
        elif db_path.endswith(('.mdb', '.accdb')):
            # MS Access via pyodbc
            return None  # TODO: Implement MS Access handler
    
    # Network databases
    if connection_params:
        db_type = connection_params.get('type', '').lower()
        if db_type == 'mysql':
            return MySQLHandler(connection_params)
        elif db_type == 'postgresql':
            return PostgreSQLHandler(connection_params)
    
    raise ValueError("Unsupported database type or insufficient connection information")
