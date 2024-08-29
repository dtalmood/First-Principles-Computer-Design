# Predefined symbols equate to memory locations
symbolTable = {
    'SP': 0,      'LCL': 1,    'ARG': 2,   'THIS': 3,   'THAT': 4,
    'R0': 0,      'R1': 1,    'R2': 2,    'R3': 3,    'R4': 4,
    'R5': 5,      'R6': 6,    'R7': 7,    'R8': 8,    'R9': 9,
    'R10': 10,    'R11': 11,  'R12': 12,  'R13': 13,  'R14': 14,
    'R15': 15,    'SCREEN': 16384, 'KBD': 24576
}

jumpTable = {
    'JGT': 1,      'JEQ': 2,      "JGE": 3,      "JLT": 4,
    'JNE': 5,      'JLE': 6,      "JMP": 7
}

destTable = {
    'M': 1,      'D': 2,      'DM': 3,       'A': 4,
    'AM':5,      'AD':6,      'ADM': 7      
}

# a = 0
compNoA = {
    '0': 42,      '1': 63,      '-1': 58,      'D': 12,
    'A': 48,      '!D': 13,     '!A': 49,      '-D': 15,
    '-A': 51,     'D+1': 31,    'A+1': 55,     'D-1': 14,
    'A-1': 50,    'D+A': 2,     'D-A': 19,     'A-D': 7,
    'D&A': 0,     'D|A': 21  
}
# a = 1
compWithA = {
    'M': 48,      '!M': 49,      '-M': 51,      'M+1': 55,
    'M-1': 50,    'D+M': 2,      'D-M': 19,     'M-D': 7,
    'D&M': 0,     'D|M': 21

}

# Global variable to keep track of variable symbol addresses
valueSymbol = 16

# Value (int), numOfBits (int), Returns String
def convertDecimalToBinary(value,numOfBits):
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
    #print("Final Answer:", final_answer)
    return final_answer

def AInstruction(mainLine):
    global valueSymbol  # Ensure we are using the global variable
    current = mainLine[1:]

    # Decimal
    if current.isdigit():
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
    # Remove parentheses from the symbol name
    symbol = mainLine[1:-1]
    symbolTable[symbol] = pc 

def CInstruction(mainLine):
    print("C-Instruction")

    # Initialize current to binary string of jump part
    current = '000'  # Default jump bits if no jump is found
    semiC = ';'
    
    # Check if semicolon is present
    if semiC in mainLine:
        print("Jump Found")
        # Extract jump instruction
        lastThreeChar = mainLine.split(semiC)[-1].strip()  # Get jump part after ';'
        # Remove everything to the right of the semicolon (including the semicolon itself)
        mainLine = mainLine.split(semiC)[0].strip()
        jumpInst = jumpTable.get(lastThreeChar, 0)  # Get corresponding decimal value, default to 0
        print("Decimal Value of Jump = ",jumpInst)
        current = convertDecimalToBinary(jumpInst, 2)  # Convert to binary string with 3 bits
        print("decimal-->Binary(jump) = ", current)

    print("After Checking for Jump, Current = ",current)
    print("Mainline after removing Jump, Mainline = ",mainLine)

    # Handle Destination
    equal = '='
    temp = ''
    if equal in mainLine:  # Dest Found
        # Extract the destination part
        leftSide = mainLine.split(equal)[0].strip()  # Get part before '='
        # Remove everything to the left of the equal sign (including the equal sign itself)
        mainLine = mainLine.split(equal, 1)[-1].strip()
        dInst = destTable.get(leftSide, 0)  # Get corresponding decimal value, default to 0
        print("Decimal Value of Dest = ",dInst)
        temp = convertDecimalToBinary(dInst, 2)  # Convert to binary string with 3 bits
        print("decimal-->Binary(dest) = ", temp)

    else:  # No Dest
        temp = '000'  # Default destination part as '000'

    # Combine temp and current as binary strings
    combined_binary = temp + current
    
    print("After checking for Destination, Current = ", combined_binary)
    print("Mainline after removing Dest, Mainline = ",mainLine)

    # Handle Computation
    comp = ''
    if mainLine in compNoA:
        print("a = 0")
        compDec = compNoA[mainLine] # Grab decimal value
        comp = convertDecimalToBinary(compDec,5) # convert to binary
        print("Comp Dec Value = ", comp) 
        comp = '1110' + comp

    else:
        print("a = 1")
        compDec = compWithA[mainLine] # Grab decimal value
        comp = convertDecimalToBinary(compDec,5) # convert to binary
        print("Comp Dec Value = ", comp) 
        comp = '1111' + comp

    finalAnswer = comp + combined_binary
    print("FINAL RESULT = ", finalAnswer)

    return finalAnswer

def main():
    # Open the .asm file for reading.
    file1 = open("TestFiles/Max.asm", "r")
    
    # This is the file we are going to be writing to.
    file2 = open("Output/Max.hack", "w+")
    
    line = file1.readline()

    pc = 0

    # First pass to resolve all labels (L-instructions)
    while line:
        mainLine = line.strip()  # Remove leading/trailing whitespace 
        
        if mainLine == "" or mainLine.startswith("//"):  # Comment or Empty Line 
            line = file1.readline()
            continue  # Skip rest of code 
        
        if mainLine.startswith('(') and mainLine[-1] == ")":  # L-instruction
            LInstruction(mainLine, pc)
        else:
            pc += 1
        
        line = file1.readline()
    
    # Reset file pointer for second pass
    file1.seek(0)
    pc = 0

    # Second pass to translate A and C instructions
    line = file1.readline()
    while line:
        mainLine = line.strip()
        
        if mainLine == "" or mainLine.startswith("//") or (mainLine.startswith('(') and mainLine[-1] == ")"):
            line = file1.readline()
            continue
        
        if mainLine.startswith('@'):  # A-instruction
            answer = AInstruction(mainLine)
            file2.write(f"{answer}\n")
        
        else:  # C-instruction
            answer = CInstruction(mainLine) 
            file2.write(f"{answer}\n")
        
        line = file1.readline()
        pc += 1

    # Close the files after the operation
    file1.close()
    file2.close()


if __name__ == "__main__":
    main()