list = []

for y in range(1,2001):
    for x in range(1,2001):
        if x <= y:
            if isinstance(int(y)/int(x) ,int):
                list.append(y)

print (list)
