import os
import io
import fitz


def convert_PDF_to_string(filename, path):
    """
    Reads PDF, converting to string text
    """

    doc = fitz.open(f'{path}\\{filename}.pdf')
    text = ""
    for page in doc:
        text += page.getText("text")
    return text


def write_file(text, filename, path):
    """
    Writes text to TXT on folder_converted
    """
    with io.open(f"{path}\\{folder_converted}\\{filename}.txt", "w", encoding="utf-8") as text_file:
        print(text, file=text_file)
    return


path = str(os.getcwdb(), "utf-8")
folder_converted = "PDFtoTXT_Convertidos"

files_in_folder = os.listdir(path)
for file in files_in_folder:
    [filename, extension] = os.path.splitext(file)
    if (extension == '.pdf' or extension == '.PDF'):
        if(not os.path.exists(f"{path}\\{folder_converted}")):
            os.mkdir(f"{path}\\{folder_converted}")
        text = convert_PDF_to_string(filename, path)
        write_file(text, filename, path)
