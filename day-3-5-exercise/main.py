# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lower = name1.lower()
name2_lower = name2.lower()

count_t = name1_lower.count("t") + name2_lower.count("t")
count_r = name1_lower.count("r") + name2_lower.count("r")
count_u = name1_lower.count("u") + name2_lower.count("u")
count_e = name1_lower.count("e") + name2_lower.count("e")
totaltrue = count_t + count_r + count_u + count_e

count_l = name1_lower.count("l") + name2_lower.count("l")
count_o = name1_lower.count("o") + name2_lower.count("o")
count_v = name1_lower.count("v") + name2_lower.count("v")
count_e = name1_lower.count("e") + name2_lower.count("e")
totallove = count_l + count_o + count_v + count_e

score = str(totaltrue) + str(totallove)
score = int(score)

if score<10 or score>90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif 40<=score<=50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")