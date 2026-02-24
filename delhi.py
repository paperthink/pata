import os
if not os.path.exists("Agra"):


    os.mkdir("Agra")

trips = ["Taj Mahal", "Red fort", "GB road"]

for m in range(0, 3):
    os.mkdir(f"Agra/{trips[m]}")


