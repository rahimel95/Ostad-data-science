my_list = [1, 5, 6, 5, 1, 2, 3]

duplicate = []

for i in my_list:
    if (my_list.count(i)>1):
        duplicate.append(i)

print(set(duplicate))