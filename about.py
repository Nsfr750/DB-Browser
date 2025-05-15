import tkinter as tk
from tkinter import ttk

class About:
    @staticmethod
    def show_about(root):
        about_dialog = tk.Toplevel(root)
        about_dialog.title('About Database Browser')
        about_dialog.geometry('400x300')
        about_dialog.transient(root)
        about_dialog.grab_set()

        # Add app icon or logo here if you have one
        title = ttk.Label(about_dialog, text='Database Browser', font=('Helvetica', 16, 'bold'))
        title.pack(pady=20)

        version = ttk.Label(about_dialog, text='Version 1.2.0')
        version.pack()

        description = ttk.Label(about_dialog, text='A simple and efficient tool for browsing\nand exporting SQLite, Access (Jet DB), MVO, and MySQL databases.', justify=tk.CENTER)
        description.pack(pady=20)

        copyright = ttk.Label(about_dialog, text='© 2025 Nsfr750')
        copyright.pack(pady=10)

        ttk.Button(about_dialog, text='Close', command=about_dialog.destroy).pack(pady=20)
