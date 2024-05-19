import subprocess
import os

def convert_odt_to_pdf(odt_file, libreoffice_path,filetype):
    # Create a temporary file path for the PDF
    out_file = os.path.splitext(odt_file)[0] + "."+filetype
    
    # Command to convert ODT to PDF using LibreOffice
    command = [libreoffice_path, "--headless", "--convert-to", filetype, odt_file, "--outdir", os.path.dirname(odt_file)]
    
    # Execute the command
    try:
        subprocess.run(command, check=True)
        print(f"Conversion successful. Output saved at: {out_file}")
    except subprocess.CalledProcessError as e:
        print(f"Conversion failed: {e}")
        out_file = None
    
    return out_file


import os

# Function to get a list of ODT files in a directory
def get_odt_files(directory):
    odt_files = []
    for file in os.listdir(directory):
        if file.endswith(".odt"):
            odt_files.append(os.path.join(directory, file))
    return odt_files

# Function to convert all ODT files in a directory to PDF
def convert_all_odt_to_pdf(directory, libreoffice_path,filetype):
    odt_files = get_odt_files(directory)
    for odt_file in odt_files:
        convert_odt_to_pdf(odt_file, libreoffice_path,filetype)



if __name__ == "__main__":
    directory_path = r"D:\Coder-12356\documents"  # Replace with the path to your ODT file
    libreoffice_path = r"C:/Program Files/LibreOffice/program/soffice.exe"  # Replace with the path to your LibreOffice executable
    filetype = "pdf"
    pdf_file_path = convert_all_odt_to_pdf(directory_path, libreoffice_path,filetype)
