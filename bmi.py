


def calculate_bmi(weight, height):
    print("Entered Height :" + str(height))
    print("Entered Weight :"+ str(weight))
    bmi=weight/(height**2)
    print("bmi="+str(bmi))
    if(bmi<18.5):
        x=-1
    elif(bmi>=18.5) and (bmi<=25.0):
        x=0
    else:
        x=1
    return x 
calculate_bmi(70,1.74)