import json

class MVOError(Exception):
    """Base exception class for MVO database errors"""
    pass

class MVOConnection:
    """
    Multiversion Object (MVO) Database Connection Handler
    """
    def __init__(self, db_path):
        self.db_path = db_path
        self.data = self._load_mvo_file()
        self._cursor = None

    def _load_mvo_file(self):
        """Load and parse the MVO database file"""
        try:
            with open(self.db_path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            raise MVOError("Invalid MVO database format")
        except IOError as e:
            raise MVOError(f"Error reading MVO database: {str(e)}")

    def cursor(self):
        """Return a cursor object for the MVO database"""
        if not self._cursor:
            self._cursor = MVOCursor(self.data)
        return self._cursor

    def close(self):
        """Close the database connection"""
        self.data = None
        self._cursor = None

    def get_tables(self):
        """Get list of tables in the MVO database"""
        return list(self.data.keys())

class MVOCursor:
    """Cursor implementation for MVO database"""
    def __init__(self, data):
        self.data = data
        self.current_table = None
        self.current_rows = None
        self.description = None
        self._row_index = 0

    def execute(self, query, params=None):
        """Execute a query on the MVO database"""
        # For MVO, we only support simple "SELECT * FROM table" queries
        if not query.lower().startswith("select * from "):
            raise ValueError("Only 'SELECT * FROM table' queries are supported for MVO databases")
        
        table_name = query[14:].strip('" \'')
        if table_name not in self.data:
            raise MVOError(f"Table '{table_name}' not found in MVO database")

        self.current_table = table_name
        self.current_rows = self.data[table_name]["rows"]
        
        # Create description based on columns
        columns = self.data[table_name]["columns"]
        self.description = [(col, None, None, None, None, None, None) for col in columns]
        
        self._row_index = 0
        return self

    def fetchall(self):
        """Fetch all rows from the current result set"""
        if self.current_rows is None:
            raise ValueError("No query has been executed yet")
        return self.current_rows

    def fetchone(self):
        """Fetch the next row from the current result set"""
        if self.current_rows is None:
            raise ValueError("No query has been executed yet")
        
        if self._row_index >= len(self.current_rows):
            return None
        
        row = self.current_rows[self._row_index]
        self._row_index += 1
        return row
