#!/usr/bin/python3

import os
import sys
import subprocess

if os.name == 'posix':
    szip = '7z'
elif os.name == 'nt':
    szip = r"C:\Program Files\7-Zip\7z.exe"

if len(sys.argv) == 2:
    archive_full_path = sys.argv[1]
else:
    raise SystemExit('No file specified. Usage: python unzap-file.py myarchive.zip')

file = os.path.basename(archive_full_path)

if not file:
    raise SystemExit('''No file specified. Maybe a directory was given as argument.
This script works only with files.''')

path_without_ext = archive_full_path[:-4]
print('Extracting: ' , archive_full_path)

a = subprocess.run([szip, "e", file, f"-o{path_without_ext}"], stdout=subprocess.PIPE, shell=False).returncode
if a == 0:
    os.remove(archive_full_path)
    subfolders = [f.path for f in os.scandir(path_without_ext) if f.is_dir()]

    if subfolders:
        print(f'{len(subfolders)} inside folder found for {file}. Deleting empty directories...')
        for subfolder in subfolders:
            try:
                os.rmdir(subfolder)
            except OSError:
                print('Deleting an inside folder failed. Probably not empty.')

    print(file, "==> extracted fine and archive deleted.\n")

else:
    print(file, "==> There was an error!\n")