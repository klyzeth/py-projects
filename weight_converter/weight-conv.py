weight = float(input("Enter weight: "))
unit = input("Enter unit (K for kg or L for lb): ")


if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"

elif unit == "L":
    weight = weight / 2.205
    unit = "kgs"

print(f"Weight is: {weight} {unit}")
    


