def merge(lst1, lst2):
    # Initialize list
    merged_list = []

    i = j = 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged_list.append(lst1[i])
            i += 1
        else:
            merged_list.append(lst2[j])
            j += 1

    merged_list.extend(lst1[i:])
    merged_list.extend(lst2[j:])

    return merged_list

# Test 
list1 = [1, 3, 4, 7, 8]
list2 = [2, 3, 5, 6, 9, 10]
merged_list = merge(list1, list2)
print(merged_list)  # [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
