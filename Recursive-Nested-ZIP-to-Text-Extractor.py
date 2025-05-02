import zipfile
import os

def extract_nested_zip(zip_path, output_dir):

    current_zip_path = zip_path
    while True:
        try:
            with zipfile.ZipFile(current_zip_path, 'r') as zip_file:
                files = zip_file.namelist()
                if len(files) == 1 and files[0].endswith('.zip'):
                    nested_zip_path = os.path.join(output_dir, files[0])
                    zip_file.extract(files[0], output_dir)
                    current_zip_path = nested_zip_path
                elif len(files) == 1 and files[0].endswith('.txt'):
                    # Extract the text file and return its content
                    with zip_file.open(files[0]) as txt_file:
                        return txt_file.read().decode('utf-8')
                else:
                    raise Exception("Unexpected file structure")
        except zipfile.BadZipFile:
            raise Exception("Encountered a corrupted ZIP file.")
        except Exception as e:
            raise e

zip_file_path = r'C:/Users/Arda Hoşcan/.spyder-py3/Coklu Degiskenelr (Multiple variables)/matryoshka.zip'  # Update this to your actual file path
output_directory = r'C:/Users/Arda Hoşcan/.spyder-py3/Coklu Degiskenelr'  # Directory for extracted files
os.makedirs(output_directory, exist_ok=True)
try:
    innermost_text_content = extract_nested_zip(zip_file_path, output_directory)
    print("Innermost Text Content:")
    print(innermost_text_content)
except Exception as e:
    print(f"Error: {e}")
