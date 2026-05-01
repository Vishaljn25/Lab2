

def calculate_bmi():
    height=float(input("Enter Height :"))
    weight=float(input("Enter Weight :"))
    bmi=weight/(height* height)
    print("bmi="+str(bmi))
    if(bmi<18.5):
        print("Weight classification: Under Weight")
    elif(bmi>=18.5) & (bmi<=25.0):
        print("Weight classification: Normal Weight")
    elif(bmi>=25):
        print("Weight classification: Over weight")
calculate_bmi()