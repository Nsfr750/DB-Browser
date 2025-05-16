from app import SQLiteApp
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import sqlite3
import json
import os
from datetime import datetime
from database_handlers import get_database_handler
from database_handlers import MVOError
from version import get_version, get_version_info
from plugins.plugin_manager import PluginManager
from create_sample_dbase import create_sample_dbase
from create_sample_sqlite import create_sample_sqlite
from create_sample_access import create_sample_access
from create_sample_mvo import create_sample_mvo
from create_sample_mysql import create_sample_mysql
from create_sample_sql import create_sample_sql
from sponsor import Sponsor

def main():
    root = tk.Tk()
    version_info = get_version_info()
    root.title(f'Database Browser v{version_info["full_version"]}')
    root.geometry('800x600')  # Set initial window size
    
    # Initialize Sponsor
    sponsor = Sponsor(root)
    
    # Initialize Plugin Manager
    plugin_manager = PluginManager(root)
    
    # Initialize the app
    app = SQLiteApp(root, sponsor)
    app.plugin_manager = plugin_manager
    
    root.protocol('WM_DELETE_WINDOW', app.close)
    root.mainloop()

if __name__ == '__main__':
    main()
