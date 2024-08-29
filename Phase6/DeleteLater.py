# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
'''
x = "(D=D+1;JLE)"
semiColon = ';'

if semiColon in x: 
    print("FOUND")

string = "D=D+1"
last_three = string[:1]
print(last_three)

'''

x = 111
y = 000 

y = y * (10 ** 3)
x += y
print(x)



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