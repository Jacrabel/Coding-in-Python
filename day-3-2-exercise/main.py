# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = round(weight / (height ** 2))
print (BMI)

if BMI <18.5:
  print(f"Your bmi is {BMI},they are underweight.")
elif BMI < 25:
  print("they have a normal weight.")
elif BMI < 30:
  print("they are slightly overweight.")
elif BMI > 30 and BMI < 35:
  print("they are obese.")
else:
  print("they are clinically obese.")


