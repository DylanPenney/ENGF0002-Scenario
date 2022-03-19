import random

# Let A and B be events such that P(A) = 0.35, P(B) = 0.5 and P(A ∪ B) = 0.65.
# # Find P(A | B).

print("Let A and B be events such that P(A) = 0.35, P(B) = 0.5 and P(A ∪ B) = 0.65.")
print("Find P(A | B)")

prob_a = float("{0:.2f}".format(random.random()))
prob_b = float("{0:.2f}".format(random.random()))
prob_a_or_b = float("{0:.2f}".format(random.random()))
prob_a_and_b = prob_a + prob_b - prob_a_or_b
solution = "{:.2f}".format(prob_a_and_b / prob_b)
# print(prob_a, prob_b ,prob_a_or_b)
print(solution)

while (True):
    user_answer = "{:.2f}".format(float(input("Give it a try: ")))
    if user_answer == solution:
        print("You got it right!")
        break
    else:
        print("Not quite right, try one more time.")
        continue







