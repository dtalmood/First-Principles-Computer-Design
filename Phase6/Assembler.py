# Open the .asm file for reading.
file1 = open("TestFiles/Add.asm", "r")

# This is the file we are going to be writing to.
file2 = open("Output/Add.asm", "w")

# Loop through file1 line by line
line = file1.readline()

while line:
    mainLine = line.strip() # Remove leading/trailing whitespace 

    if mainLine == "" or mainLine.startswith("//"): # Check Comment or Line 
        line = file1.readline()
        continue  # Skip Rest of Code 

    # Determine if A-instruction or C-instruction
    
    if mainLine.startswith('@'): # A-Instruction
       
         if(mainLine[1:2].isnumeric()): # Decimal
            print("Found Decimal")

        

        # Lablel

        # Symbol 
    
    else: # C-instruction
        print("C")

    # Read the next line
    line = file1.readline()

# Close the files after the operation
file1.close()
file2.close()
