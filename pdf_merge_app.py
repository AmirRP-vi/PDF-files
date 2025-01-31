import os
from tkinter import Tk, filedialog
from PyPDF2 import PdfMerger

Tk().withdraw

initial_directory = "/mnt/c/"

pdf_files = filedialog.askopenfilenames(title="Select PDF's to merge",
                                         filetypes=[("PDF files", "*.pdf")],
                                         initialdir=initial_directory)

if not pdf_files:
    print("No files selected. Exiting...")
    exit()

output_file = filedialog.asksaveasfilename(title="Save merged PDF as",
                                            defaultextension=".pdf",
                                              filetypes=[("PDF files", "*.pdf")],
                                              initialdir=initial_directory)

if not output_file:
    print("No output file selected. Exiting...")
    exit()

merger = PdfMerger()
for pdf_file in pdf_files:
    merger.append(pdf_file)

merger.write(output_file)
merger.close()
print(f"Files merged into {output_file}")