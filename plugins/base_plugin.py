"""
Base plugin interface for DB Browser
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List

class BasePlugin(ABC):
    """Base class for all plugins"""
    
    def __init__(self, name: str, version: str):
        self.name = name
        self.version = version
        self.enabled = True
        
    @abstractmethod
    def initialize(self) -> bool:
        """Initialize the plugin"""
        pass
    
    @abstractmethod
    def shutdown(self) -> None:
        """Shutdown the plugin"""
        pass
    
    @abstractmethod
    def get_metadata(self) -> Dict[str, Any]:
        """Get plugin metadata"""
        pass

class BaseDatabasePlugin(BasePlugin):
    """Base class for database handler plugins"""
    
    @abstractmethod
    def connect(self, connection_string: str) -> bool:
        """Connect to database"""
        pass
    
    @abstractmethod
    def disconnect(self) -> None:
        """Disconnect from database"""
        pass
    
    @abstractmethod
    def get_tables(self) -> List[str]:
        """Get list of tables"""
        pass
    
    @abstractmethod
    def execute_query(self, query: str) -> Any:
        """Execute SQL query"""
        pass

class BaseUIPlugin(BasePlugin):
    """Base class for UI plugins"""
    
    @abstractmethod
    def create_ui(self, parent) -> Any:
        """Create UI elements"""
        pass
    
    @abstractmethod
    def update_ui(self, data: Dict[str, Any]) -> None:
        """Update UI with new data"""
        pass

class BaseExportPlugin(BasePlugin):
    """Base class for export plugins"""
    
    @abstractmethod
    def export_data(self, data: Any, format: str) -> bool:
        """Export data to specified format"""
        pass
    
    @abstractmethod
    def get_supported_formats(self) -> List[str]:
        """Get list of supported export formats"""
        pass
