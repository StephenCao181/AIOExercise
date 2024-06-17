num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
sub_list = []
result = []

for i in num_list:
    sub_list.append(i)

    if len(sub_list) == k:
        result.append(max(sub_list))
        del sub_list[0]

print(result)
