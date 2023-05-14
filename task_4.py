len_sequence = int(input())
list_num = ''
for i in range(len_sequence + 1):
    list_num += (str(i) + ' ') * i
print(list_num[:(len_sequence * 2 - 1)])