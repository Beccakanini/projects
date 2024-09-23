import tkinter as tk
from tkinter import filedialog
import platform

# Check the operating system to import the appropriate module
if platform.system() == "Windows":
    import win32print
else:
    import cups

def print_document():
    # Open file dialog to select the document to print
    filepath = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf"), ("Text Files", "*.txt")])
    
    if filepath:
        if platform.system() == "Windows":
            # Print document on Windows
            printer_name = win32print.GetDefaultPrinter()
            win32print.ShellExecute(0, "print", filepath, '/d:"%s"' % printer_name, ".", 0)
        else:
            # Print document on Linux/Mac
            conn = cups.Connection()
            printers = conn.getPrinters()
            default_printer = printers.keys()[0]
            conn.printFile(default_printer, filepath, "Print Job", {})

# Create the Tkinter application window
root = tk.Tk()

# Create a button to trigger document printing
print_button = tk.Button(root, text="Print Document", command=print_document)
print_button.pack()

# Run the Tkinter event loop
root.mainloop()
