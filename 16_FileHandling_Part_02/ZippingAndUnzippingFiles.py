# ZIPPING FILES :-

# zipfile - Module
# ZipFile - Class
# ZIP_DEFLATED -  Variable
# ZIP_STORED - Variable
# Module contains classes and variables.

print("==================================== ZIPPING ============================================")

# CASE 1:
# Create a normal text file with 200 lines. File size will be 4kb
from zipfile import ZipFile, ZIP_DEFLATED,ZIP_STORED
with open("abcd.txt","w") as f:
    f.write("This is first text file\n" * 200)

with open("wxyz.txt","w") as f1:
    f1.write("This is second text file\n" * 200)

# CASE 2:
# create a text file without compression using ZipFile class (compression parameter - ZIP_STORED)
# This will create a zip folder
# 'no_compressed.zip' - 4kb folder size containing file 'abcd.txt' - 4kb
with ZipFile("no_compressed.zip","w",compression=ZIP_STORED) as f:
    f.write("abcd.txt")

# CASE 3:
# Create a text file with compression using ZipFile class (compression parameter - ZIP_DEFLATED)
# This will create a zip folder
# 'compressed.zip' - 1kb  containing both files 'abcd.txt' - 4kb and 'wxyz.txt' - 6kb respectively.
with ZipFile("compressed.zip","w",compression=ZIP_DEFLATED) as f:
    f.write("abcd.txt")
    f.write("wxyz.txt")

print("==================================== UNZIPPING ============================================")

# UNZIPPING :-

# We'll use extractall() method to unzip the zip folder.
# This folder will contain all the files of zip folder.

with ZipFile("compressed.zip", "r") as unzip:
    print(unzip.namelist())   # ['abcd.txt', 'wxyz.txt']
    unzip.extractall("Unzipped_Folder")
    # unzip.extract("abcd.txt","Unzipped_Folder")   # we can extract specific file also.




