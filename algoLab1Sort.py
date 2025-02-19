# INSERTION SORT - w/o counting
def insertion_sort(data):
    for i in range(1,len(data)):
        curr = data[i]
        pos = i
        while pos > 0 and data[pos-1] > curr:
            data[pos] = data[pos-1]
            pos -= 1
        data[pos] = curr
    return data

# INSERTION SORT - w/ counting of no. of comparisons
def insertion_count(data):
    comparisons = 0

    for i in range(1,len(data)):
        curr = data[i]
        pos = i
        while pos > 0 and data[pos-1] > curr:
            comparisons += 1                    # compare data[pos-1] and curr
            data[pos] = data[pos-1]
            pos -= 1
        if data[pos-1] <= curr:                 # while loop stopped because of 2nd criteria
            comparisons += 1                    # comparison still made whether success/fail, so must add 1
        data[pos] = curr
    return comparisons, data

# MERGE SORT - w/o counting
def merge(list1,list2):
    i = j = 0
    newlist = []

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            newlist.append(list1[i])
            i += 1
        else:
            newlist.append(list2[j])
            j += 1

    if i < len(list1):
        newlist.extend(list1[i:])
    else:
        newlist.extend(list2[j:])

    return newlist

def merge_sort(data):
    if len(data) > 1:
        mid = len(data)//2
        lower = data[:mid]
        upper = data[mid:]
        sorted1 = merge_sort(lower)
        sorted2 = merge_sort(upper)
        return merge(sorted1, sorted2)
    return data

# MERGE SORT - w/ counting of no. of comparisons
def merge(sorted1,sorted2):
    list1 = sorted1[0]
    list2 = sorted2[0]
    i = j = 0
    newlist = []
    comparisons = sorted1[1]+sorted2[1]
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            comparisons += 1
            newlist.append(list1[i])
            i += 1
        else:
            comparisons += 1
            newlist.append(list2[j])
            j += 1

    if i < len(list1):
        newlist.extend(list1[i:])
    else:
        newlist.extend(list2[j:])

    return newlist, comparisons
    
def merge_sort(data):
    # Base Case
    if len(data) == 1:
        return data,0
    # Recursion
    elif len(data) > 1:
        mid = len(data)//2
        lower = data[:mid]
        upper = data[mid:]
        sorted1 = merge_sort(lower) #sorted 1 is a tuple (sorted lower list, number of comparisons for lower list)
        sorted2 = merge_sort(upper) #sorted 2 is a tuple (sorted upper list, number of comparisons for upper list)
        return merge(sorted1, sorted2)


    