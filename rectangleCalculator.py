length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

perimeter = length * 2 + width * 2
area = length * width
diagonal = (width**2 + length**2) ** 0.5

print(
    "Rectangle perimeter: ",
    perimeter,
    "\nRectangle area: ",
    area,
    "\nRectangle diagonal: ",
    round(diagonal, 2),
)
