# Dictionaries and maps

# solution1
n = int(input())
dict = {}

for i in range(0, n):
    name, number = input().split()
    dict[name] = number

for i in range(0, n):
    name = input()
    if name in dict:
        print(f'{name}={dict[name]}')
    else:
        print("Not found")













