# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 != 0:
  print("This is not a leap year.")
elif year % 100 != 0:
  print("This is a leap year.")
elif year % 400 == 0:
  print("This is a leap year.")
else:
  print("This is a not leap year.")


