import json

lyrics = [
    "Mary had a little lamb",
    "His fleece was white as snow, yeah",
    "Everywhere the child went",
    "Your little lamb was sure to go now",
]

with open("mary.txt", "w") as outfile:
    for line in lyrics:
        outfile.write(line + "\n")

try:
    with open("mary.txt", "r") as infile:
        for line in infile:
            print(line.strip())
except FileNotFoundError:
    print("The file was not found.")


my_dict = {
    1: "William",
    2: "Patrick",
    3: "Jon",
    4: "Tom",
    5: "Peter",
    6: "Colin",
    7: "Sylvester",
    8: "Paul",
    9: "Chris",
    10: "David",
    11: "Matt",
    12: "Peter",
    13: "Jodie",
}

for key, value in my_dict.items():
    print(key, value)

with open("names.json", "w") as outfile:
    json.dump(my_dict, outfile, indent=1)

with open("names.json", "r") as infile:
    names_dict = json.load(infile)

print(names_dict)
