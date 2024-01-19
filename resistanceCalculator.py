resistanceOne = float(input("What is the value of R1? "))
resistanceTwo = float(input("What is the value of R2? "))
resistanceThree = float(input("What is the value of R3? "))

denominator = (1 / resistanceOne) + (1 / resistanceTwo) + (1 / resistanceThree)
answer = 1 / denominator

print("The equivalent resistance is", round(answer, 2), "ohms")
