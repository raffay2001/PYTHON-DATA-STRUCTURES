lst = [1, 2, 3, 4, 5]
lst_1 = []
for i in range(len(lst)-1, -1, -1):
    lst_1.append(lst[i])
print(lst_1)