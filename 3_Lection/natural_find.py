answer = str('y')
for i in range(1000):
    if answer != 'y':
        break
    else:
        for tries in range(3):
            try:
                end_num = int(input('Enter the end number\n'))
                num_list = list(range(1, end_num + 1))
                summ_list = 0
                for num in num_list:
                    if num % 3 == 0:
                        summ_list += num
                    if num % 5 == 0:
                        summ_list += num
                print(summ_list)

            except Exception:
                print('Its not a number!')

        answer=str(input('Another try?\n'))