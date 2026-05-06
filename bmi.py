

def calculate_bmi():
    height=float(input("Enter Height :"))
    weight=float(input("Enter Weight :"))
    bmi=weight/(height**2)
    print("bmi="+str(bmi))
    if(bmi<18.5):
        x=-1
    elif(bmi>=18.5) & (bmi<=25.0):
        x=0
    elif(bmi>=25):
        x=1
    return x       
calculate_bmi()