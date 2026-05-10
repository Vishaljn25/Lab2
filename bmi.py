

<<<<<<< HEAD
def calculate_bmi(weight, height):
    print("Enter Height :" + str(height))
    print("Enter Weight :"+ str(weight))
=======

def calculate_bmi(weight, height):
    print("Entered Height :" + str(height))
    print("Entered Weight :"+ str(weight))
>>>>>>> 9e302ffdf32aa39129e2e425d6fa212b58ccce36
    bmi=weight/(height**2)
    print("bmi="+str(bmi))
    if(bmi<18.5):
        x=-1
    elif(bmi>=18.5) and (bmi<=25.0):
        x=0
    else:
        x=1
<<<<<<< HEAD
    return x     

=======
    return x 
>>>>>>> 9e302ffdf32aa39129e2e425d6fa212b58ccce36
