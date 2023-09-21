import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox
'''from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas'''
from fpdf import FPDF

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Note Saver - {filepath}")

def save_file():
    """Save the current file."""
    filepath = window.title()
    if "Note Saver - " in filepath:
        filepath = filepath.replace("Note Saver - ", "")
        with open(filepath, "w") as output_file:
            text = txt_edit.get(1.0, tk.END)
            output_file.write(text)
    else:
        save_as_file()

def save_as_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Note Saver - {filepath}")

def new_file():
    """Create a new empty file."""
    txt_edit.delete(1.0, tk.END)
    window.title("Note Saver - New File")

class PDF(FPDF):
    '''def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'My PDF Title', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')'''

def pdf_saver():
    # Use the print function from tkinter to print the contents of the Text widget
    txt_to_print = txt_edit.get(1.0, tk.END)
    pdf_file = asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF Files","*.pdf")]
    )
    if not pdf_file:
        return
    
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt_to_print)
    pdf.output(pdf_file)
    
    '''# Create a PDF document and add the text to it
    c = canvas.Canvas(pdf_file, pagesize=letter)
    c.drawString(100, 750, txt_to_print)
    c.save()'''

def cut_text():
    copy_text()
    txt_edit.delete(tk.SEL_FIRST, tk.SEL_LAST)

def copy_text():
    txt_edit.clipboard_clear()
    txt_edit.clipboard_append(txt_edit.selection_get())

def paste_text():
    txt_edit.insert(tk.INSERT, txt_edit.clipboard_get())

window = tk.Tk()
window.title("Note Saver")
window.rowconfigure(0, minsize=550, weight=1)
window.columnconfigure(1, minsize=1000, weight=1)

# Create a Menu bar
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# Create a "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add colors to the menu items
menu_bar.configure(bg='light yellow')
#file_menu.configure(bg='white')

# File menu options
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As...", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Convert to pdf", command=pdf_saver)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

# Create an "Edit" menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
#edit_menu.configure(bg='white')

# Edit menu options
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)

# Create a Text widget
txt_edit = tk.Text(window)
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
