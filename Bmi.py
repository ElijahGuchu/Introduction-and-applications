height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = round(weight / height ** 2)
print("Your BMI is ",bmi)
if bmi < 18.5:
  print("You are underweight")

elif bmi < 24.9:
  print("You are healthy")

elif bmi < 29.9:
  print("You are overweight")

elif bmi < 35:
  print("You are obese")  
else:
  print("You are clinically obese")