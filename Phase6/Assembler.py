# Predefined symbols equate to memory locations
preDefinedSymbols = {
    'SP': 0,      'LCL': 1,    'ARG': 2,   'THIS': 3,   'THAT': 4,
    'R0': 0,      'R1': 1,    'R2': 2,    'R3': 3,    'R4': 4,
    'R5': 5,      'R6': 6,    'R7': 7,    'R8': 8,    'R9': 9,
    'R10': 10,    'R11': 11,  'R12': 12,  'R13': 13,  'R14': 14,
    'R15': 15,    'SCREEN': 16384, 'KBD': 24576
}
userDefinedSymbols= {}

def convertDecimalToBinary(value):
    print("Entered Function")
    count = 0
    current = 0 
    answer = 0
    while(value != 0):
        if(value % 2 == 1):
            current = 1
        else:
            current = 0
        
        answer += current * (10 ** count)
        count += 1
        value //= 2
    if(count == 0):
        rest = 15-count
    else:   
        rest = 15-count+1
    final_answer = '0' * rest + str(answer)
    print("Final Answer:", final_answer)
    return final_answer

def AInstruction(mainLine):
    print("A-Instruction")
    current = mainLine[1:]

    # Decimal
    if mainLine[1:2].isnumeric():  
        print("Found Decimal")
        value = int(current)
        result = convertDecimalToBinary(value)
        return result
    
    # Check if Predefined Symbol 
    elif current in preDefinedSymbols: 
        value = preDefinedSymbols[current]
        result = convertDecimalToBinary(value)
        return result

        

def LInstruction(mainLine, pc):
    print("L-Instruction")
    userDefinedSymbols[mainLine] = pc 
    result = convertDecimalToBinary(pc) 
    return result




def CInstruction(mainLine):
    print("C-Instruction")


def main():
    # Open the .asm file for reading.
    file1 = open("TestFiles/test.asm", "r")
    
    # This is the file we are going to be writing to.
    file2 = open("Output/test.hack", "w+")
    
    line = file1.readline()

    pc = 0

    # Loop through file1 line by line
    while line:
        mainLine = line.strip()  # Remove leading/trailing whitespace 
        
        if mainLine == "" or mainLine.startswith("//"):  # Comment or Empty Line 
            line = file1.readline()
            continue  # Skip Rest of code 
        # Determine if A, C or L instruction 
        
        if mainLine.startswith('@'):  # A-inst
            answer = AInstruction(mainLine)
            file2.write(f"{answer}\n")


        elif mainLine.startswith('(') and mainLine[-1] == ")":  #L-Inst        
            answer = LInstruction(mainLine, pc)
            file2.write(f"{answer}\n")
        
        else:  # C-Inst
            CInstruction(mainLine) 

        # Read the next line
        line = file1.readline()
        #increment our program counter
        pc += 1

    # Close the files after the operation
    file1.close()
    file2.close()

if __name__ == "__main__":
    main()
