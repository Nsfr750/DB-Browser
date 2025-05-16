# Plugin System Guide

## Overview

The Database Browser features a modular plugin system that allows for easy extension and customization. Plugins can extend the application's functionality in various ways, including database handlers, UI components, and export formats.

## Plugin Types

### Database Handlers

Database handler plugins provide support for additional database formats. They must implement the `BaseDatabasePlugin` interface.

#### Required Methods

```python
from plugins.base_plugin import BaseDatabasePlugin

class CustomDatabaseHandler(BaseDatabasePlugin):
    def __init__(self):
        super().__init__()
        self.name = "Custom Database Handler"
        self.version = "1.0"
        self.description = "Handles custom database format"
        
    def connect(self, connection_params):
        """Connect to the database"""
        raise NotImplementedError
        
    def get_tables(self):
        """Get list of tables"""
        raise NotImplementedError
        
    def execute_query(self, query, params=None):
        """Execute a database query"""
        raise NotImplementedError
        
    def close(self):
        """Close the database connection"""
        raise NotImplementedError
```

### UI Plugins

UI plugins extend the application's user interface with new components or functionality.

#### Required Methods

```python
from plugins.base_plugin import BaseUIPlugin

class CustomUIPlugin(BaseUIPlugin):
    def __init__(self, root):
        super().__init__(root)
        self.name = "Custom UI Component"
        self.version = "1.0"
        self.description = "Adds custom UI functionality"
        
    def initialize(self):
        """Initialize the plugin UI"""
        raise NotImplementedError
        
    def cleanup(self):
        """Cleanup resources"""
        raise NotImplementedError
```

### Export Plugins

Export plugins provide additional data export formats.

#### Required Methods

```python
from plugins.base_plugin import BaseExportPlugin

class CustomExportPlugin(BaseExportPlugin):
    def __init__(self):
        super().__init__()
        self.name = "Custom Export Format"
        self.version = "1.0"
        self.description = "Exports data in custom format"
        
    def export_data(self, data, output_path):
        """Export data to specified format"""
        raise NotImplementedError
```

## Plugin Discovery

1. Plugins are automatically discovered in the following directories:
   - Database Handlers: `plugins/database_handlers/`
   - UI Plugins: `plugins/ui_plugins/`
   - Export Plugins: `plugins/export_plugins/`

2. The plugin manager scans these directories at application startup
3. Plugins must have a valid Python file with a class that inherits from the appropriate base plugin
4. Plugins can be enabled/disabled through the application settings

## Plugin Lifecycle

1. **Initialization**
   - Plugin is discovered by the plugin manager
   - Constructor is called
   - `initialize()` method is called (for UI plugins)

2. **Operation**
   - Plugin methods are called as needed
   - Error handling should be implemented
   - Resources should be managed properly

3. **Cleanup**
   - `cleanup()` method is called when plugin is disabled
   - Resources should be released
   - UI elements should be destroyed

## Best Practices

### Code Organization

1. Place plugin files in the appropriate directory:
   ```
   plugins/
   ├── database_handlers/
   │   └── custom_handler.py
   ├── ui_plugins/
   │   └── custom_ui.py
   └── export_plugins/
       └── custom_export.py
   ```

2. Use meaningful names for plugin files and classes
3. Include docstrings for all methods
4. Use type hints
5. Follow PEP 8 guidelines

### Error Handling

1. Implement proper error handling
2. Use specific exception types
3. Provide meaningful error messages
4. Clean up resources in finally blocks

### Resource Management

1. Release resources in `cleanup()` method
2. Use context managers when possible
3. Implement proper cleanup for UI elements
4. Handle file operations carefully

### Testing

1. Test plugins independently
2. Test integration with the main application
3. Test error conditions
4. Test cleanup operations

## Example Plugin

Here's a complete example of a database handler plugin:

```python
"""
Custom Database Handler Plugin

Handles custom database format operations.
"""

from plugins.base_plugin import BaseDatabasePlugin
from typing import Dict, List, Any
import logging

logger = logging.getLogger(__name__)

class CustomDatabaseHandler(BaseDatabasePlugin):
    """Handles custom database format operations."""
    
    def __init__(self):
        super().__init__()
        self.name = "Custom Database Handler"
        self.version = "1.0"
        self.description = "Handles custom database format"
        self.connection = None
        
    def connect(self, connection_params: Dict[str, Any]) -> bool:
        """Connect to the database.
        
        Args:
            connection_params: Dictionary containing connection parameters
            
        Returns:
            bool: True if connection was successful, False otherwise
        """
        try:
            # Your connection logic here
            self.connection = self._create_connection(connection_params)
            return True
        except Exception as e:
            logger.error(f"Connection failed: {e}")
            raise ConnectionError(f"Failed to connect: {e}")
            
    def get_tables(self) -> List[str]:
        """Get list of tables in the database.
        
        Returns:
            List[str]: List of table names
        """
        if not self.connection:
            raise ConnectionError("Not connected")
            
        try:
            # Your table listing logic here
            return []
        except Exception as e:
            logger.error(f"Failed to get tables: {e}")
            raise DatabaseError(f"Failed to get tables: {e}")
            
    def execute_query(self, query: str, params: Dict = None) -> List[Dict]:
        """Execute a database query.
        
        Args:
            query: SQL query to execute
            params: Query parameters
            
        Returns:
            List[Dict]: Query results
        """
        if not self.connection:
            raise ConnectionError("Not connected")
            
        try:
            # Your query execution logic here
            return []
        except Exception as e:
            logger.error(f"Query failed: {e}")
            raise QueryError(f"Query failed: {e}")
            
    def close(self) -> None:
        """Close the database connection."""
        if self.connection:
            try:
                self.connection.close()
            except Exception as e:
                logger.error(f"Failed to close connection: {e}")
            finally:
                self.connection = None
```

## Troubleshooting

### Common Issues

1. **Plugin Not Loading**
   - Verify plugin file is in the correct directory
   - Check for syntax errors in plugin code
   - Ensure plugin inherits from the correct base class
   - Verify plugin has required metadata (name, version, description)

2. **Connection Issues**
   - Check connection parameters
   - Verify database server is running
   - Check permissions
   - Review error logs

3. **Resource Leaks**
   - Implement proper cleanup in `cleanup()` method
   - Use context managers
   - Release resources in finally blocks
   - Monitor memory usage

4. **UI Issues**
   - Verify UI elements are properly initialized
   - Check for widget destruction in cleanup
   - Review event bindings
   - Test layout and positioning

## Contributing

1. Create a new branch for your plugin:
   ```bash
   git checkout -b feature/plugin-name
   ```

2. Add your plugin to the appropriate directory
3. Write tests for your plugin
4. Update documentation
5. Create a pull request

## License

The plugin system is released under the MIT License. See LICENSE file for details.
