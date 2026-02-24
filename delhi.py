import os
if not os.path.exists("Agra"):



    os.mkdir("Agra")

trips = ["Taj Mahal", "Red fort", "GB road"]
for f in range(0, len(trips)+1):
    

    if os.path.exists(f"Agra/{trips[f-1]}"):#f-1 = 0 -> 2

        os.rmdir(f"Agra/{trips[f-1]}")#so that 3 doesnt get count
        #it might throw error
    else:
        pass

for m in range(0, 3):
    if not os.path.exists(trips[m]):
        os.mkdir(f"Agra/{trips[m]}")


