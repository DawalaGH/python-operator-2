height=float(input("enter height in cm:"))
weight=float(input("enter weight in kg:"))

BMI=weight/(height/100) **2
print("Your BMI is:")

if BMI<18.5:
 print("You are underweight")

elif 18.5<BMI<25:
 print("You are normal weight")

elif 25<=BMI<30:
 print("You are overweight")

else:
 print("You are obese")
