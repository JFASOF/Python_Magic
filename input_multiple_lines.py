"""sumary_line"""
"""sumary_line

lines = []

while True:
    u_input = input()
    
    if u_input == '' : 
        break 
    else: 
        lines.append(u_input + '\n') 
        
print(lines)
print(''.join(lines))
"""


"""sumary_line

DESC arguments: use sys package
Press CTRL + D (Unix) or CTRL + Z (Windows) to exit
import sys 

user_input = sys.stdin.readlines()
print(user_input)
print(''.join(user_input))

"""

#print(''.join(['a\n', 'b\n', 'c\n']))

lines = []


while True:
    try:
        lines.append(input())
    except EOFError:
        lines_str = '\n'.join(lines)
        print(lines_str)

        break

print(lines)