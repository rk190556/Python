# in appending we add new data with retaining previous data 
file=open("ex2.txt",'a')
l=["Line4","Line5","Line6"]
for item in l:
  file.write(item+"\n")

file.close()

# other file handling 
# r Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.

# r+ Opens a file for both reading and writing. The file pointer placed at the beginning of the file.

# w Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.

# w+ Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.

# a Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

# a+ Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The File opens in the append mode. If the file does not exist, it creates a new file for reading and writing.