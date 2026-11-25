#Weight on different planets using a function 
#Take the mass in kg and a planet name (Earth, Moon, Mars, Jupiter). Use a function to print the weight in newtons up to 2 decimals.


def calculate_weight(mass, planet):
    if planet.lower() == "earth":
        gravity = 9.81
    elif planet.lower() == "moon":
        gravity = 1.62
    elif planet.lower() == "mars":
        gravity = 3.71
    elif planet.lower() == "jupiter":
        gravity = 24.79
    else:
        return None

    weight = mass * gravity
    return weight

mass = float(input("Enter the mass in kilograms: "))
planet= input("Enter the name of planet:")
weight = calculate_weight(mass, planet)

if weight is not None:
    print(f"Weight on {planet} is: {weight:.2f} N")
else:
    print("Invalid planet name.")
