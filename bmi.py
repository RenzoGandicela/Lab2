def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height*height)

    print("BMI = ", bmi)
    if bmi<18.5:
        print("Under Weight")
        return -1
    elif bmi>= 18.5 and bmi<=25:
        print("Normal Weight")
        return 0
    else:
        print("Over weight")
        return 1

print(calculate_bmi(weight=57,height=1.73))