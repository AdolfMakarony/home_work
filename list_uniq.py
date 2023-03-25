# check plz
list_dan = [1, 5, 4, 3, 5, 6, 7, 4, 5, 6, 7, 5, 4, 3, 5, 4, 3, 2, 5, 4, 5, 9, 0, 5, 7, 3, 4, 3, 7, 0, 9, 5, 0, 3, 5, 4,
            3, 6, 4]

check_list = list(range(0, 10))
result = []

for num in check_list:
    if num not in list_dan:
        result.append(num)

print('there is(are) no ', result, 'number(s) in list')

hw1_list = list(range(0, 400))
hw2_list = hw1_list[100:301]
print(hw2_list[5::7])