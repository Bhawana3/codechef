def find_number(list,k):
    diff_value = []
    i = 0
    while i < len(list):
        for element in list:
            diff = (element - list[i])
            if (diff > 0) and (diff <= k):
                diff_value.append([list[i],element])
                print diff_value
        i += 1
    return diff_value

values = find_number([1,2,3,4],2)
print values

def get_path(list):
    path = []
    start = list[0][1]
    end = list[-1][1]
    print start
    print end
    for i in list[1:]:
        print i
        if i[0] == start:
            path.append([list[0],i])
    return path

#print get_path(values)
