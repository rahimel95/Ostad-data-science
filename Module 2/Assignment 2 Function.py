'''
Write a program to ascending sort the elements from the following list. (Create a function to solve it)

List = [1, 5, 2, 9, 3, 22, 13]


'''
def find_min(lst):
    mini = lst[0]
    for i in range(1,len(lst)):
        if mini > lst[i]:
            mini = lst[i]
    return mini

def sort_func(unsorted):
    sorted_list = []
    while unsorted:
        min_num = find_min(unsorted)
        sorted_list.append(min_num)
        unsorted.remove(min_num)
    return sorted_list

List = [1, 5, 2, 9, 3, 22, 13]
sorted_list = sort_func(List)
print (sorted_list)
