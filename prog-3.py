# print the list a recursively
def Recursively(lis):
    for item in lis:
        if isinstance(item,(list)):
            Recursively(item)
        else:
            print(item)


lis = [16,29,33,48,51,63,74]
Recursively(lis)