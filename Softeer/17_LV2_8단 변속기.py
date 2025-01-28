import sys

lst = input()

lst=lst.replace(" ","")

if lst == "12345678":
    print("ascending")
elif lst=="87654321":
    print("descending")
else:
    print("mixed")