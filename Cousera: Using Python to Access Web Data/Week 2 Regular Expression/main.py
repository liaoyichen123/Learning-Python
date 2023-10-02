import re

file_name_str = "regex_sum_1895394.txt"
file_handle = open(file_name_str)
sum_int = 0
for line in file_handle:
    int_lst = re.findall("([0-9]+)", line)
    if len(int_lst) is not 0:
        for i in int_lst:
            sum_int = sum_int + int(i)
print(sum_int)