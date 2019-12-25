#!/usr/bin/python3

import os
import sys
import subprocess
import time

wait_time = 5

print('Serpentlabs unzap 0.3')
print('----------------------\n')

if len(sys.argv) == 1:
    inp_dir = os.getcwd()
elif len(sys.argv) == 2:
    inp_dir = sys.argv[1]
else:
    raise NotImplementedError("Only one dir argument or no argument supported right now.")

if os.name == 'posix':
    szip = '7z'
elif os.name == 'nt':
    szip = r"C:\Program Files\7-Zip\7z.exe"

archive_type = {'.zip', '.rar'}

archive_files = [(x.path, x.name) for x in os.scandir(inp_dir.strip()) if x.name[-4:].lower() in archive_type]

print(f'Notice: Waiting {wait_time} seconds between each archive.\n')

successes = 0
failures = []

for i, archive in enumerate(archive_files):
    archive_path = archive[0]
    archive_name = archive[1]
    path_without_ext = archive[0][:-4]
    print('Extracting: ', archive_path)

    a = subprocess.run([szip, "e", archive_path, f"-o{path_without_ext}"], stdout=subprocess.PIPE, shell=False).returncode
    if a == 0:
        os.remove(archive_path)
        subfolders = [f.path for f in os.scandir(path_without_ext) if f.is_dir()]

        if subfolders:
            print(len(subfolders),'inside folder found for',archive_name,'. Deleting empty directories...')
            for subfolder in subfolders:
                try:
                    os.rmdir(subfolder)
                except OSError:
                    print('Deleting an inside folder failed. Probably not empty.')

        print(archive_name, "==> extracted fine and archive deleted.\n")
        successes += 1
        if i + 1 < len(archive_files):
            time.sleep(wait_time)
    else:
        print(archive_name, "==> There was an error!\n")
        failures.append(archive_name)

print('Done extracting' , len(archive_files), 'archives.')
print('successes:' , successes , 'failures:', len(failures))

if failures:
    print('Errors:')
    for failure in failures:
        print(failure)