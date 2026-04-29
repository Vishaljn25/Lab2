

def calculate_bmi(height, weight,):
    print("Height="+str(height))
    print("Weight="+str(weight))
    bmi=weight/(height**2)
    print("bmi="+str(bmi))
    if(bmi<18.5):
        print("Weight classification: Under Weight")
    elif(bmi>=18.5) & (bmi<=25.0):
        print("Weight classification: Normal Weight")
    elif(bmi>=25):
        print("Weight classification: Over weight")
calculate_bmi(weight=53,height=1.73)