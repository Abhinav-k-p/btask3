# Write a Python program to find the intersection of two lists

def find_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)
    return list(intersection)

def main():
    list1 = [5, 10, 55, 1, 6]
    list2 = [8, 14, 16, 11, 10]
    intersection = find_intersection(list1, list2)
    print("Intersection of the lists: ", intersection)
    
if __name__ == "__main__":
    main()



