import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import scrolledtext

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Editor")
        self.root.geometry("600x400")

        # Create a menu bar
        self.create_menu()

        # Create a text widget
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, undo=True)
        self.text_area.pack(expand=1, fill=tk.BOTH)

        # Create a status bar
        self.status_bar = tk.Label(root, text="Word Count: 0", anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Bind events
        self.text_area.bind("<KeyRelease>", self.update_word_count)

        # Initialize filename
        self.filename = None

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open...", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As...", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

    def new_file(self):
        self.filename = None
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Text Files", "*.txt"),
                                                          ("All Files", "*.*")])
        if file_path:
            self.filename = file_path
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())
            self.update_word_count()

    def save_file(self):
        if self.filename:
            with open(self.filename, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text Files", "*.txt"),
                                                           ("All Files", "*.*")])
        if file_path:
            self.filename = file_path
            self.save_file()

    def update_word_count(self, event=None):
        text = self.text_area.get(1.0, tk.END)
        word_count = len(text.split())
        self.status_bar.config(text=f"Word Count: {word_count}")

def main():
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
