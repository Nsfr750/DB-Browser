"""
MySQL database plugin for DB Browser
"""

from .base_plugin import BaseDatabasePlugin
import mysql.connector
from typing import Dict, List, Any

class MySQLPlugin(BaseDatabasePlugin):
    """MySQL database handler plugin"""
    
    def __init__(self):
        super().__init__("MySQL", "1.0.0")
        self.connection = None
        
    def initialize(self) -> bool:
        """Initialize the MySQL plugin"""
        try:
            # Test connection to ensure MySQL is available
            mysql.connector.connect(host='localhost', user='root', password='root')
            return True
        except Exception as e:
            print(f"Error initializing MySQL plugin: {str(e)}")
            return False
    
    def shutdown(self) -> None:
        """Shutdown the MySQL plugin"""
        if self.connection:
            self.connection.close()
    
    def get_metadata(self) -> Dict[str, Any]:
        """Get plugin metadata"""
        return {
            'name': self.name,
            'version': self.version,
            'type': 'database',
            'supports': ['mysql', 'mariadb']
        }
    
    def connect(self, connection_string: str) -> bool:
        """Connect to MySQL database"""
        try:
            # Parse connection string
            conn_params = {}
            for param in connection_string.split(';'):
                if '=' in param:
                    key, value = param.split('=', 1)
                    conn_params[key.lower()] = value
            
            # Connect to database
            self.connection = mysql.connector.connect(
                host=conn_params.get('host', 'localhost'),
                user=conn_params.get('user', 'root'),
                password=conn_params.get('password', 'root'),
                database=conn_params.get('database')
            )
            return True
        except Exception as e:
            print(f"Error connecting to MySQL: {str(e)}")
            return False
    
    def disconnect(self) -> None:
        """Disconnect from MySQL database"""
        if self.connection:
            self.connection.close()
            self.connection = None
    
    def get_tables(self) -> List[str]:
        """Get list of tables in the database"""
        if not self.connection:
            return []
            
        try:
            cursor = self.connection.cursor()
            cursor.execute("SHOW TABLES")
            tables = [row[0] for row in cursor.fetchall()]
            cursor.close()
            return tables
        except Exception as e:
            print(f"Error getting tables: {str(e)}")
            return []
    
    def execute_query(self, query: str) -> Any:
        """Execute SQL query"""
        if not self.connection:
            return None
            
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query)
            if query.strip().upper().startswith(('SELECT', 'SHOW')):
                result = cursor.fetchall()
            else:
                self.connection.commit()
                result = cursor.rowcount
            cursor.close()
            return result
        except Exception as e:
            print(f"Error executing query: {str(e)}")
            return None
