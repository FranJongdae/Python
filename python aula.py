print("Hello World")

def school_age_calculator(age,name):
    if age < 5:
        print("Enjoy!", name, "is only", age)
    elif age == 5:
        print("Enjoy kindergaten,", name)
    else:
        print("They grow up so fast")

school_age_calculator(20,"Fran")