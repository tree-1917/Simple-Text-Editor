# --- Text Editor --- #
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


class TextEditor:
    def __init__(self, master):
        """This is simple text editor"""
        master.geometry('500x500+700+300')
        self.master = master
        self.text_editor = Text(master)
        self.btn_frame = Frame(master, relief=RAISED, bd=2)
        self.open_button = Button(
            self.btn_frame, text="Open", command=self.file_open)
        self.save_button = Button(
            self.btn_frame, text="Save As...", command=self.save_file)
        # put element in GUI
        self.open_button.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        self.save_button.grid(row=1, column=0, sticky="ew", padx=5)
        self.btn_frame.grid(row=0, column=0, sticky='ns')
        self.text_editor.grid(row=0, column=1, sticky="nsew")

    def file_open(self):
        """Open a file for in text editor for editing"""
        file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", '*.txt'), ("All Files", "*.*")]
        )
        if not file_path:
            return

        self.text_editor.delete('1.0', END)
        with open(file_path, mode='r', encoding='utf-8') as input_file:
            text = input_file.read()
            self.text_editor.insert(END, text)
        self.master.title(f"Simple Text Editor - {file_path}")

    def save_file(self):
        """Save the Current file as a new file in txt format."""
        file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[
                                             ("Text Files", '*.txt'), ("All Files", '*.*')])
        if not file_path:
            return
        
        with open(file_path, mode='w', encoding='utf-8') as output_file:
            text = self.text_editor.get('1.0', END)
            output_file.write(text)
        self.master.title(f"Simple Text Editor - {file_path}")


def main():
    root = Tk()
    text_editor = TextEditor(root)
    root.mainloop()


if __name__ == "__main__":
    main()
