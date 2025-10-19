# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())

############################################

# Formula
BMI= float(weight)/(float(height)**2)

if BMI <18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI>=18.5 and BMI<25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI >= 25 and BMI <30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI >=30 and BMI <35:
    print(f"Your BMI is {BMI}, you are obese.")
elif BMI>=35:
    print(f"Your BMI is {BMI}, you are clinically obese.")
