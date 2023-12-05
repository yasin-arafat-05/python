import os
import shutil

source_folder = r'C:\Users\Hp\Desktop\testFolder'
destination_folder = r'C:\Users\Hp\Desktop\cppFiles'

files = os.listdir(source_folder)

for filename in files:
    if filename.endswith('.cpp'):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        shutil.copy(source_path, destination_path)