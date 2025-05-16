"""
Plugin manager for DB Browser
"""

import importlib
import os
from typing import Dict, List, Type
from .base_plugin import BasePlugin, BaseDatabasePlugin, BaseUIPlugin, BaseExportPlugin

class PluginManager:
    """Manages plugins for DB Browser"""
    
    def __init__(self, root):
        self.root = root
        self.plugins: Dict[str, BasePlugin] = {}
        self.database_plugins: Dict[str, BaseDatabasePlugin] = {}
        self.ui_plugins: Dict[str, BaseUIPlugin] = {}
        self.export_plugins: Dict[str, BaseExportPlugin] = {}
        
    def load_plugins(self) -> None:
        """Load all available plugins"""
        # Load database handler plugins
        self._load_plugins_from_directory('database_handlers', BaseDatabasePlugin)
        # Load UI plugins
        self._load_plugins_from_directory('ui_plugins', BaseUIPlugin)
        # Load export plugins
        self._load_plugins_from_directory('export_plugins', BaseExportPlugin)
        
    def _load_plugins_from_directory(self, directory: str, base_class: Type) -> None:
        """Load plugins from a specific directory"""
        plugins_dir = os.path.join('plugins', directory)
        if not os.path.exists(plugins_dir):
            return
            
        for plugin_file in os.listdir(plugins_dir):
            if plugin_file.endswith('.py') and plugin_file != '__init__.py':
                module_name = plugin_file[:-3]
                try:
                    module = importlib.import_module(f'plugins.{directory}.{module_name}')
                    for attr_name in dir(module):
                        attr = getattr(module, attr_name)
                        if isinstance(attr, type) and issubclass(attr, base_class):
                            plugin = attr()
                            if plugin.initialize():
                                self.plugins[plugin.name] = plugin
                                if issubclass(attr, BaseDatabasePlugin):
                                    self.database_plugins[plugin.name] = plugin
                                elif issubclass(attr, BaseUIPlugin):
                                    self.ui_plugins[plugin.name] = plugin
                                elif issubclass(attr, BaseExportPlugin):
                                    self.export_plugins[plugin.name] = plugin
                except Exception as e:
                    print(f"Error loading plugin {module_name}: {str(e)}")
    
    def get_plugin(self, name: str) -> BasePlugin:
        """Get a plugin by name"""
        return self.plugins.get(name)
    
    def get_database_plugin(self, name: str) -> BaseDatabasePlugin:
        """Get a database plugin by name"""
        return self.database_plugins.get(name)
    
    def get_ui_plugin(self, name: str) -> BaseUIPlugin:
        """Get a UI plugin by name"""
        return self.ui_plugins.get(name)
    
    def get_export_plugin(self, name: str) -> BaseExportPlugin:
        """Get an export plugin by name"""
        return self.export_plugins.get(name)
    
    def get_all_plugins(self) -> List[BasePlugin]:
        """Get all loaded plugins"""
        return list(self.plugins.values())
    
    def get_all_database_plugins(self) -> List[BaseDatabasePlugin]:
        """Get all database plugins"""
        return list(self.database_plugins.values())
    
    def get_all_ui_plugins(self) -> List[BaseUIPlugin]:
        """Get all UI plugins"""
        return list(self.ui_plugins.values())
    
    def get_all_export_plugins(self) -> List[BaseExportPlugin]:
        """Get all export plugins"""
        return list(self.export_plugins.values())
    
    def shutdown(self) -> None:
        """Shutdown all plugins"""
        for plugin in self.plugins.values():
            try:
                plugin.shutdown()
            except Exception as e:
                print(f"Error shutting down plugin {plugin.name}: {str(e)}")
