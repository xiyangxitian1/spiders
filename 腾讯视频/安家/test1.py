a1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


# 3个一组进行分
#
def get_group_by(data, split_num):
    result = []
    i = 0
    while i < len(data):
        result.append(data[i:i + split_num])
        i = i + split_num
    return result
