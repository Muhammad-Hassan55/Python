file = open("youtube.txt", "w")

try:
    file.write("chai au code")

finally:
    file.close()

with open("youtube,txt", "w") as file:
    file.write("Mian Hassan")
