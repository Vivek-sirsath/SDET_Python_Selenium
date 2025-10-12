# BINARY FILE HANDLING :

# JPG (Image) FILE HANDLING :-
f1 = open("IMG.jpg","rb")

# Reading the binary file
# print(f1.read())   # b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\..............   (b'\ for binary)
# This returns the data in console in Hexadecimal format. Understandable by Computer.

# Save the 'f1' file in a variable after reading
bytes = f1.read()

f2 = open("IMG_NEW.jpg","wb")   # This will create New file if not exist.

# Write the data from 'f1' to 'f2'
f2.write(bytes)

f1.close()
f2.close()













