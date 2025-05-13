def calculate_bmi(height,weight):
    print("height="+ str(height))
    print("weight="+ str(weight))
    bmi=weight/(height*height)
    print(bmi)

    if(bmi<18.5):
        print("underweight")
        return -1
    elif(bmi<=25.0):
        print("normal weight")
        return 0
    else:
        print("overweight")
        return 1

calculate_bmi(1.73,57)