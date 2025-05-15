import sqlite3
import pyodbc
import MySQLdb
from mvo_db import MVOConnection, MVOError
import json
import csv
import os
import logging
from typing import List, Dict, Any, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='database_browser.log',
    filemode='a'
)

class DatabaseHandler:
    def __init__(self, db_path: str = None, connection_params: Dict[str, Any] = None):
        self.db_path = db_path
        self.connection_params = connection_params
        self.conn = None
        self.cursor = None
        self.logger = logging.getLogger(self.__class__.__name__)

    def connect(self):
        try:
            self._validate_connection_params()
            self._establish_connection()
            self.logger.info(f"Successfully connected to database: {self.db_path or self.connection_params}")
        except Exception as e:
            self.logger.error(f"Connection error: {str(e)}")
            raise

    def _validate_connection_params(self):
        """Validate connection parameters before attempting to connect."""
        pass

    def _establish_connection(self):
        """Establish the actual database connection."""
        raise NotImplementedError("Subclasses must implement _establish_connection method")

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
    def __init__(self, connection_params: Dict[str, Any]):
        super().__init__(connection_params=connection_params)
        self.conn = None
        self.cursor = None

    def _validate_connection_params(self):
        required_params = ['host', 'user', 'password', 'database']
        for param in required_params:
            if param not in self.connection_params:
                raise ValueError(f"Missing required MySQL connection parameter: {param}")

    def _establish_connection(self):
        try:
            self.conn = MySQLdb.connect(
                host=self.connection_params['host'],
                user=self.connection_params['user'],
                passwd=self.connection_params['password'],
                db=self.connection_params['database']
            )
            self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)
        except MySQLdb.Error as e:
            raise ValueError(f"MySQL Connection Error: {e}")

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

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

class MVOHandler(DatabaseHandler):
    def __init__(self, db_path: str):
        super().__init__(db_path=db_path)
        self.mvo_conn = None

    def _establish_connection(self):
        try:
            self.mvo_conn = MVOConnection(self.db_path)
        except MVOError as e:
            raise ValueError(f"MVO Connection Error: {e}")

    def get_tables(self) -> List[str]:
        return self.mvo_conn.get_tables()

    def execute_query(self, query: str = None, params: tuple = None) -> List[Dict[str, Any]]:
        tables = self.get_tables()
        if not tables:
            return []
        
        # If no specific query, return first table's data
        table_name = tables[0]
        return [dict(record) for record in self.mvo_conn.data[table_name]]

    def export_to_csv(self, table_name: str, output_path: str):
        if table_name not in self.mvo_conn.data:
            raise ValueError(f"Table {table_name} not found")
        
        data = self.mvo_conn.data[table_name]
        if not data:
            return
        
        headers = list(data[0].keys())
        
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            for record in data:
                writer.writerow([record.get(header, '') for header in headers])

    def close(self):
        if self.mvo_conn:
            self.mvo_conn.close()

class AccessHandler(DatabaseHandler):
    def __init__(self, db_path: str):
        super().__init__(db_path=db_path)
        self.conn = None
        self.cursor = None

    def _establish_connection(self):
        try:
            conn_str = f'DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={self.db_path}'
            self.conn = pyodbc.connect(conn_str)
            self.cursor = self.conn.cursor()
        except pyodbc.Error as e:
            raise ValueError(f"Access Database Connection Error: {e}")

    def get_tables(self) -> List[str]:
        tables = []
        for table_info in self.cursor.tables(tableType='TABLE'):
            tables.append(table_info.table_name)
        return tables

    def execute_query(self, query: str = None, params: tuple = None) -> List[Dict[str, Any]]:
        if not query:
            # If no query provided, fetch first table
            tables = self.get_tables()
            if not tables:
                return []
            query = f'SELECT * FROM [{tables[0]}]'
        
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        
        columns = [column[0] for column in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def export_to_csv(self, table_name: str, output_path: str):
        query = f'SELECT * FROM [{table_name}]'
        self.cursor.execute(query)
        
        columns = [column[0] for column in self.cursor.description]
        
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(columns)
            writer.writerows(self.cursor.fetchall())

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

class DBaseHandler(DatabaseHandler):
    def __init__(self, db_path: str):
        super().__init__(db_path=db_path)
        self.table = None

    def connect(self):
        try:
            self.table = dbf.Table(self.db_path)
            self.table.open()
        except Exception as e:
            raise ValueError(f"Error opening dBase file: {e}")

    def get_tables(self) -> List[str]:
        # For dBase, we return the single table name
        return [os.path.splitext(os.path.basename(self.db_path))[0]]

    def execute_query(self, query: str = None, params: tuple = None) -> List[Dict[str, Any]]:
        if not self.table:
            raise ValueError("Database not connected")
        
        # Convert dBase records to dictionaries
        return [dict(record) for record in self.table]

    def export_to_csv(self, table_name: str, output_path: str):
        if not self.table:
            raise ValueError("Database not connected")
        
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write headers
            headers = self.table.field_names
            writer.writerow(headers)
            
            # Write data
            for record in self.table:
                writer.writerow([getattr(record, field) for field in headers])

    def close(self):
        if self.table:
            self.table.close()

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

def get_database_handler(db_path: str = None, connection_params: Dict[str, Any] = None) -> Optional[DatabaseHandler]:
    """
    Factory method to create the appropriate database handler based on input.
    
    :param db_path: Path to the database file
    :param connection_params: Dictionary of connection parameters
    :return: Appropriate DatabaseHandler instance or None
    """
    logger = logging.getLogger('DatabaseHandlerFactory')
    
    try:
        if db_path:
            # File-based databases
            if db_path.endswith('.db'):
                logger.info(f"Creating SQLite handler for {db_path}")
                return SQLiteHandler(db_path)
            elif db_path.endswith(('.dbf', '.db3')):
                logger.info(f"Creating dBase handler for {db_path}")
                return DBaseHandler(db_path)
            elif db_path.endswith(('.mdb', '.accdb')):
                logger.info(f"Creating Access handler for {db_path}")
                return AccessHandler(db_path)
            elif db_path.endswith('.mvo'):
                logger.info(f"Creating MVO handler for {db_path}")
                return MVOHandler(db_path)
        
        # Network databases
        if connection_params:
            db_type = connection_params.get('type', '').lower()
            if db_type == 'mysql':
                logger.info(f"Creating MySQL handler for {connection_params.get('database', 'unknown')}")
                return MySQLHandler(connection_params)
            elif db_type == 'postgresql':
                logger.info(f"Creating PostgreSQL handler for {connection_params.get('database', 'unknown')}")
                return PostgreSQLHandler(connection_params)
        
        logger.error("No suitable database handler found")
        raise ValueError("Unsupported database type or insufficient connection information")
    
    except Exception as e:
        logger.error(f"Error creating database handler: {str(e)}")
        raise
