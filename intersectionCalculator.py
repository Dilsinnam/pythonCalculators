lineOne = float(input("Enter m for line 1: "))
lineOneB = float(input("Enter b for line 1: "))
lineTwo = float(input("Enter m for line 2: "))
lineTwoB = float(input("Enter b for line 2: "))

intersection = (lineTwoB - lineOneB) / (lineOne - lineTwo)
intersectionTwo = lineOne * intersection + lineOneB

print(
    f"The intersection point is ({round(intersection, 2)}"
    f",{round(intersectionTwo, 2)})",
)
