print("welcome to the calculator")

option =int =0

while option!=5:
    print("1.- suma\n"+ "4.-resta\n"+"3.-multiplicion\n""4.-divicion\n"+"5.-salir")
    option=input()

    one = int
    one=input(" insert the first dato ")
    second_d=int
    second_d= input (" insert the second dato ")
    result=float
    
    
    if option == 1:
        result =one + second_d
        print (result)
    elif option==2:
        result=one - second_d
        print(result)
    elif option==3:
        result=one*second_d
        print(result)
    elif option ==4:
        result=one/second_d
        print(result)
    elif option==5:
        print("thenk for service")
    else:
        print("option don't exist")
