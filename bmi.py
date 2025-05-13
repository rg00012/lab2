def calculate_bmi(height,weight):
    print("height="+ str(height))
    print("weight="+ str(weight))
    bmi=weight/(height*height)
    print(bmi)

    if(bmi<18.5):
        print("underweight")
    elif(bmi<=25.0):
        print("normal weight")
    else:
        print("overweight")

calculate_bmi(1.73,57)