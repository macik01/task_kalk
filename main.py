num_one = int(input("Enter a number one: "))
num_two = int(input("Enter a number two: "))
num_oper = str(input("Enter a number operation '+' or '-' or '*' or '/':' "))

if num_oper == '+' :
    res = num_one + num_two
    print(res)
elif num_oper == '-' :
    res = num_one - num_two
    print(res)
elif num_oper == '*' :
    res = num_one * num_two
    print(res)
elif num_oper == '/' and num_two !=0 :
    res  = int (num_one / num_two)
    print(res)
else:
    print("Eror")
