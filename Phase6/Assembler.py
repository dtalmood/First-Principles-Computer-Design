# Predefined symbols equate to memory locations
symbolTable = {
    'SP': 0,      'LCL': 1,    'ARG': 2,   'THIS': 3,   'THAT': 4,
    'R0': 0,      'R1': 1,    'R2': 2,    'R3': 3,    'R4': 4,
    'R5': 5,      'R6': 6,    'R7': 7,    'R8': 8,    'R9': 9,
    'R10': 10,    'R11': 11,  'R12': 12,  'R13': 13,  'R14': 14,
    'R15': 15,    'SCREEN': 16384, 'KBD': 24576
}

jump = {
    'JGT': 1,      'JEQ': 2,      "JGE": 3,      "JLT": 4,
    'JNE': 5,      'JLE': 6,      "JMP": 7
}

dest = {
    'M': 1,      'D': 2,      'DM': 3,       'A': 4,
    'AM':5,      'AD':6,      'ADM': 7      
}

compNoA = {
    '0': 42,      '1': 63,      '-1': 58,      'D': 12,
    'A': 48,      '!D': 13,     '!A': 49,      '-D': 15,
    '-A': 51,     'D+1': 31,    'A+1': 55,     'D-1': 14,
    'A-1': 50,    'D+A': 2,     'D-A': 19,     'A-D': 7,
    'D&A': 0,     'D|A': 21  
}

compWithA = {
    'M': 48,      '!M': 49,      '-M': 51,      'M+1': 55,
    'M-1': 50,    'D+M': 2,      'D-M': 19,     'M-D': 7,
    'D&M': 0,     'D|M': 21

}

# Global variable to keep track of variable symbol addresses
valueSymbol = 16

def convertDecimalToBinary(value,numOfBits):
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
        rest = numOfBits-count
    else:   
        rest = numOfBits-count+1
    final_answer = '0' * rest + str(answer)
    print("Final Answer:", final_answer)
    return final_answer

def AInstruction(mainLine):
    global valueSymbol  # Ensure we are using the global variable
    print("A-Instruction")
    current = mainLine[1:]

    # Decimal
    if current.isdigit():
        print("Found Decimal")
        value = int(current)
        result = convertDecimalToBinary(value,15)
        return result
    
    # Check if Predefined Symbol 
    elif current in symbolTable: 
        value = symbolTable[current]
        result = convertDecimalToBinary(value,15)
        return result

    # If not predefined, then we have a variable 
    else:
        # Check if the variable is already defined
        if current not in symbolTable:
            # Add the variable to symbolTable with the next available address
            symbolTable[current] = valueSymbol
            valueSymbol += 1    
        
        # Get the address for the variable
        value = symbolTable[current]
        result = convertDecimalToBinary(value,15)
        return result


def LInstruction(mainLine, pc):
    print("L-Instruction")
    # Remove parentheses from the symbol name
    symbol = mainLine[1:-1]
    symbolTable[symbol] = pc 
    result = convertDecimalToBinary(pc,15) 
    return result

def CInstruction(mainLine):
    print("C-Instruction")

    #First Lets Check if we have jump
    
    semiC = ';'
    if semiC in mainLine: # Jump 
        dest = '='

    #else: # No Jump
    



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