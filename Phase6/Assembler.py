print("Hello")

# Open the .asm file for reading and writing.
file1 = open("TestFiles/Add.asm", "w+")

# this is the file we are going to be writing to.
file2 = open("Output/Add.asm", "w")


#loop file 1 line by line 
line = file1.readline()

while(line):
    print(line.strip())
    line = file1.readline()
    
    