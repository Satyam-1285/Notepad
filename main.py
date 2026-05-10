import tkinter as tk
from tkinter import filedialog, messagebox

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Notepad")
        self.root.geometry("800x600")

        # Create a text area
        self.textarea = tk.Text(self.root, font=("Arial", 12), undo=True)
        self.textarea.pack(fill=tk.BOTH, expand=True)

        # Create a Menu Bar
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)

        # Add File Menu
        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

    def new_file(self):
        self.textarea.delete(1.0, tk.END)
        self.root.title("New File - Notepad")

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                                filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if file_path:
            self.textarea.delete(1.0, tk.END)
            with open(file_path, "r") as file:
                self.textarea.insert(1.0, file.read())
            self.root.title(f"{file_path} - Notepad")

    def save_file(self):
        file_path = filedialog.asksaveasfilename(initialfile='Untitled.txt',
                                                  defaultextension=".txt",
                                                  filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.textarea.get(1.0, tk.END))
            self.root.title(f"{file_path} - Notepad")

if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()
