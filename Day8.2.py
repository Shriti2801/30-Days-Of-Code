# solution2 for dictionaries and mappings

n = int(input())
entries = {}

for i in range(0,n):
    text = input().split()
    entries[text[0]] = text[1]

while True:
    try:
        name = input()
        if name in entries:
            print(name + "=" + entries[name])
        else:
            print("Not found")
    except:
        break