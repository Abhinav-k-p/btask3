# Write a Python program to remove duplicates from a list

def remove_duplicates(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list

original_list = [10,20,10,50,20]
deduplicated_list = remove_duplicates(original_list)
print("Deduplicated list:", deduplicated_list)


    