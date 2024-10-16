'''num_one = int(input("Enter a number one: "))
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
    print("Eror") '''

#tast 3.2
num =  [12 , 3 , 4 , 10]
if len(num) > 1:
    num_last = num.pop()
    num.insert( 0 , num_last)
print(num)

