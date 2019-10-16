string = "hello world!"
print(len(string))

print(string[0])
print(string[len(string) - 1])
print(string[-1])

x = 0 
while x < len(string):
    print(string[x])
    x = x + 1

print(string[::-1])
print(string[0:6])