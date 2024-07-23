x = []
f_x = []
first_divided_differences = []
second_divided_differences = []
third_divided_differences = []
fourth_divided_differences = []
degree = int(input("enter number of degree:"))
print("enter the numbers of x")
for i in range(degree + 1):
    x.append(float(input()))
print("enter the numbers of f-x")
for i in range(degree + 1):
    f_x.append(float(input()))
for i in range(degree):
    first_divided = (f_x[i + 1] - f_x[i]) / (x[i + 1] - x[i])
    first_divided_differences.append(first_divided)
for i in range(degree - 1):
    second_divided = (first_divided_differences[i + 1] - first_divided_differences[i]) / (x[i + 2] - x[i])
    second_divided_differences.append(second_divided)
for i in range(degree - 2):
    third_divided = (second_divided_differences[i + 1] - second_divided_differences[i]) / (x[i + 3] - x[i])
    third_divided_differences.append(second_divided)
for i in range(degree - 3):
    fourth_divided = (third_divided_differences[i + 1] - third_divided_differences[i]) / (x[i + 4] - x[i])
    fourth_divided_differences.append(fourth_divided)
print("first_divided_differences", first_divided_differences)
print("second_divided_differences", second_divided_differences)
print("third_divided_differences", third_divided_differences)
print("fourth_divided_differences", fourth_divided_differences)
p_x = float(input("enter number of p of x:"))
p1 = f_x[0] + first_divided_differences[0] * (p_x - x[0])
p2 = second_divided_differences[0] * (p_x - x[0]) * (p_x - x[1])
p3 = third_divided_differences[0] * (p_x - x[0]) * (p_x - x[1]) * (p_x - x[2])
p4 = fourth_divided_differences[0] * (p_x - x[0]) * (p_x - x[1]) * (p_x - x[2]) * (p_x - x[3])
p_final = p1 + p2 + p3 + p4
print("p of", p_x,"is", p_final)
