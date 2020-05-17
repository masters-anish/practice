
import ast
#input_str = sys.stdin.read()
input_str = "bmaunmdbraai"

message1 = ""
message2 = ""
pos = 0
condition_check = len(input_str)
for x in range(len(input_str)):
    if pos == len(input_str):
        break
    message1 = message1 + input_str[pos]  
    #print(input_str[pos])
    message2 = message2 + input_str[pos + 1]      
    #print(input_str[pos + 1])
    if pos >= condition_check + 2 :
        break 
    else: 
        pos = pos + 2
print (message1,message2)  
print (input_str[1::2])
print (input_str[0::2])
#print(message1,message2)
    