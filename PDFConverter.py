import tkinter as tk
from tkinter import filedialog
from fpdf import FPDF
from docx2pdf import convert as docx_to_pdf

root = tk.Tk()

class TextAndDocxToPdfConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Converter")
        self.root.geometry("400x200")

        self.label = tk.Label(root, text="Select a text or docx file to convert to PDF")
        self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="Select Text/Docx File", command=self.select_file)
        self.select_button.pack()

        self.convert_button = tk.Button(root, text="Convert to PDF", command=self.convert_to_pdf, state=tk.DISABLED)
        self.convert_button.pack(pady=10)

        self.pdf_output_path = None  # Initialize the variable

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("Docx Files", "*.docx")])
        if file_path:
            self.file_path = file_path
            self.convert_button.config(state=tk.NORMAL)
            self.label.config(text=f"Selected file: {file_path}")
        else:
            self.label.config(text="No file selected.")
            self.convert_button.config(state=tk.DISABLED)

    def convert_to_pdf(self):
        self.pdf_output_path = None  # Reset pdf_output_path

        if self.file_path.endswith(".txt"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.set_font("Arial", size=12)

            # Encode the line as UTF-8 before adding it to the PDF
            
            with open(self.file_path, "r", encoding="utf-8") as text_file:
                for line in text_file:
                    pdf.multi_cell(0, 10, line.encode('latin-1', 'replace').decode('latin-1'))

            self.pdf_output_path = self.file_path.replace(".txt", ".pdf")
            pdf.output(self.pdf_output_path)

        elif self.file_path.endswith(".docx"):
            docx_to_pdf(self.file_path)
            self.pdf_output_path = self.file_path.replace(".docx", ".pdf")

        # Updating UI label

        if self.pdf_output_path:
            self.label.config(text=f"File converted and saved as {self.pdf_output_path}")
        else:
            self.label.config(text="Unsupported file type selected.")

        # Disabling the conversion button
        
        self.convert_button.config(state=tk.DISABLED)

app = TextAndDocxToPdfConverter(root)
root.mainloop()
