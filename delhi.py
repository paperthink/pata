import os
if not os.path.exists("Agra"):


    os.mkdir("Agra")

trips = ["Taj Mahal", "Red fort", "GB road"]
for f in range(0, len(trips)+1):
    

    if os.path.exists(f"Agra/{trips[f-1]}"):

        os.rmdir(f"Agra/{trips[f-1]}")

#for m in range(0, 3):
   # if not os.path.exists(trips[m]):
    #    os.mkdir(f"Agra/{trips[m]}")


