size = int(input())
arr = []

for i in range(0, size):
    text = input().split()
    if text[0] == "insert":
        arr.insert(int(text[1]), int(text[2]))
    elif text[0] == "append":
        arr.append(int(text[1]))
    elif text[0] == "print":
        print(arr)
    elif text[0] == "remove":
        arr.remove(int(text[1]))
    elif text[0] == "sort":
        arr.sort()
    elif text[0] == "pop":
        arr.pop()
    elif text[0] == "reverse":
        arr.reverse()
