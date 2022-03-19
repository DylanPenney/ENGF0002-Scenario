import random

# A box contains 8 green and 4 blue marbles. Two marbles are selected at random
# (without replacement). Find the probability that selected marbles are:
# 	(a) of the same colour;
# 	(b) of different colours.

green = int(random.randint(1,10))
blue = int(random.randint(1,10))
# print(green, blue)

print("A box contains %i green and %i blue marbles. Two marbles are selected at random without replacement." % (green,blue))
print("Find the probability that selected marbles are:")
print("(a) of the same colour;")
print("(b) of different colours.")

#Calculation of part (a)
both_blue = (blue/(blue+green)) * ((blue-1)/(blue+green-1))
both_green = (green/(blue+green)) * ((green-1)/(blue+green-1))
solution_a = "{:.2f}".format(both_blue + both_green)
print(solution_a)

while (True):
    user_answer = "{:.2f}".format(float(input("Give part A a try: ")))
    if user_answer == solution_a:
        print("You got part A right!")
        break
    else:
        print("Not quite right, try one more time.")
        continue

#Calculation of part (b)
blue_before_green = (blue/(blue+green)) * (green/(blue+green-1))
green_before_blue = (green/(blue+green)) * (blue/(blue+green-1))
solution_b = "{:.2f}".format(blue_before_green + green_before_blue)
print(solution_b)

while (True):
    user_answer = "{:.2f}".format(float(input("Give part B a try: ")))
    if user_answer == solution_b:
        print("Well done! You got both parts right!")
        break
    else:
        print("Not quite right, try one more time.")
        continue







