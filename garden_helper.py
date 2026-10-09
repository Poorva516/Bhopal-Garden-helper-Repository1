# Bhopal garden Helper
# No internet needed
print("======Welcome! To Bhopal Garden Helper======")
print("----------------------------------\n")
print("..................Made For My Mom........................\n")

#step 1: what month
month = 10
print(f"Month is {month} -> October")

#step 2:Plants 
if month == 10:
    print("step 2 .......... This plants in october.......\n")
    print("1. corinder : 20 days")
    print("2. radish = easy")
    print("3. tomato = it needs sunlight")
    print("4. spinach = fast")

#step 3:area check
area = 20
plants = area // 4
print(f" stpe 3 : Area of {plants} sq ft")
print(f"You can grow {plants} plants")

#step 4 : water check
water = input("stpe 4 : How you water plants today (yes/No): ")
if water == "yes":
    print("GOOD! Plants are Happy Now")
else:
    print("Go! give water to plants")

#step 5:Sunlight check
sunlight = int(input("stpe 5 : How many hours the plants need SUnlight : "))
if sunlight > 5:
    print("WOO its good for tomato")
else:
    print("go! grow spinach it nedds less sunlight")

#step6 : Touch grass game
steps = int(input("\nSTEP 6: How many steps walked outside today? "))
if steps > 500:
    print(f"{steps} steps! Achievement: Touched Grass!")
else:
    print(f"Only {steps}? Go outside now, close phone!")

# Final why open
print("\nWhy open? No internet, free, data at home, works in farm")

