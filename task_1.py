int_variable_1 = int(input())
int_variable_2 = int(input())
int_variable_3 = int(input())
maximum_variable = max(int_variable_1, int_variable_2, int_variable_3)
minimum_variable = min(int_variable_1, int_variable_2, int_variable_3)
remaining_variable = int_variable_1 + int_variable_2 + int_variable_3 - maximum_variable - minimum_variable
print(maximum_variable)
print(minimum_variable)
print(remaining_variable)