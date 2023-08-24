import os
import zipfile

bin_dir = os.path.join(os.path.dirname(__file__), 'bin')
csv_dir = os.path.join(os.path.dirname(__file__), 'csv')

for file in os.listdir(bin_dir):
    if file.endswith('.zip') and not file.startswith('.'):
        print('Extraindo arquivo: ' + file)
        with zipfile.ZipFile(os.path.join(bin_dir, file), 'r') as zip_ref:
            extracted_files = zip_ref.namelist()
            for extracted_file in extracted_files:
                # Extracted files have no extension and a unique name, so rename them
                new_file_name = os.path.splitext(file)[0] + '.csv'
                extracted_file_path = os.path.join(csv_dir, new_file_name)
                with zip_ref.open(extracted_file) as src, open(extracted_file_path, 'wb') as dst:
                    dst.write(src.read())

        os.remove(os.path.join(bin_dir, file))
