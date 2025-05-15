from app import SQLiteApp
import tkinter as tk
from version import get_version, get_version_info
from sponsor import Sponsor

def main():
    root = tk.Tk()
    version_info = get_version_info()
    root.title(f'Database Browser v{version_info["full_version"]}')
    root.geometry('800x600')  # Set initial window size
    
    # Initialize Sponsor
    sponsor = Sponsor(root)
    
    # Add Sponsor menu to the app
    app = SQLiteApp(root, sponsor)
    
    root.protocol('WM_DELETE_WINDOW', app.close)
    root.mainloop()

if __name__ == '__main__':
    main()
