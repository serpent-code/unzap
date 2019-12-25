# unzap
A small python script to extract all zip and rar files in a directory and deleting said archive files after successful extraction.

Works under Linux and Windows.

It uses 7zip so 7zip needs to be already installed. Edit the files and point to 7zip binary.
By default it is assumed "7z" is already in the PATH under Linux and under windows "C:\Program Files\7-Zip\7z.exe" is looked for.


One of the aims was to prevent over heating if there are many files to extract so by default it sleeps for 5 seconds between each archive file. You can change this behavior easily by setting wait_time = 0 in unzap-dir.py.

Example usage:

cd into a directory and run unzap-dir.py with no arguments.

or

`unzap-dir.py /home/you/somedir/`

`unzap-file.py /home/you/somearchive.zip`
