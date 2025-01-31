from PyPDF2 import PdfMerger

merger = PdfMerger()

file_1 = "/mnt/c/Users/ToosArax/Desktop/file1.pdf" #path the file you want to upload
file_2 = "/mnt/c/Users/ToosArax/Desktop/file2.pdf" #path the file you want to upload
pdf_files = [file_1, file_2]

for pdf_file in pdf_files:
    merger.append(pdf_file)

output_file = "/mnt/c/Users/ToosArax/Desktop/merged_files.pdf" #path the file you want to be download 
merger.write(output_file)
merger.close()
print(f"Files merged into {output_file}")