print="Welcome to Grade Calculator"
n=0
if n<10:
    n=n+1
    math=int(input("Please enter your maths mark:"))  
    chem=int(input("Please enter your chemistry mark:"))   
    phy=int(input("Please enter your physics mark:"))
    avg= int(((math+chem+phy)/300)*100)
    print(avg)
    percent='Your percentage score is:' + str(avg) + '%'
    print(percent)
    if avg>=70:
        grade="A"
    elif 60<=avg<70:
        grade="B"
    elif 50<=avg<60:
        grade="C"
    elif 40<=avg<50:
        grade="D"
    else:
        print("You failed")
    f"You scored a grade of {grade}"

