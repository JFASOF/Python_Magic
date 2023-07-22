my_str = 'Python Magic'
#my_str[start:stop:step]
result = my_str[:6]
print(result)  # 👉️ Python


result = my_str[:6] + '...' if len(my_str) > 5 else my_str
print(result)  # 👉️ Python...

# Creating a reusable function
def truncate_string(string, length, suffix='...'):
    return string[:length] + suffix


print(truncate_string(my_str, 3))
print(truncate_string(my_str, 5))
print(truncate_string(my_str, 7))


# Truncate a string using a formatted string literal
result = f'{my_str:.5}'
print(result)  
var1 = 'Python'
var2 = 'Magic'

result = f'{var1}{var2}'
print(result)

#use ternary operator 
result = f'{my_str:.5}{"..." if len(my_str) > 5 else ""}'
print(result)

# Truncate a string using str.rsplit()
my_str2 = 'python magic example'
new_str = my_str2.rsplit(' ', 1)[0]
print(new_str) 

print(my_str2.rsplit(' '))  # 👉️ ['python', 'magic', 'example']
print(my_str2.rsplit(' ', 1))  # ['python magic', 'example']

# 👇️ remove last word from string
result = my_str2.rsplit(' ', 1)[0]
print(result)  # 👉️ python magic

# 👇️ remove last 2 words from string
result = my_str2.rsplit(' ', 2)[0]
print(result)  # 👉️ python

#textwrap.shorten method to truncate a string
import textwrap
result_wrap = textwrap.shorten(my_str, width=4,placeholder='')
print(result_wrap)

first = 'Python'
last = 'Magic'

result = "Name: {} {}".format(first, last)
print(result)  # 👉️ "Name: Python Magic"
