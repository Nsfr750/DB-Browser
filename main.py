from app import SQLiteApp
import tkinter as tk

def main():
    root = tk.Tk()
    root.title('Database Browser')
    root.geometry('800x600')  # Set initial window size
    
    app = SQLiteApp(root)
    root.protocol('WM_DELETE_WINDOW', app.close)
    root.mainloop()

if __name__ == '__main__':
    main()
