colors = ['black','white']
sizes = ['S','M','L']
tshirt = [(color,size) for color in colors for size in sizes]
print(tshirt)

for color in colors:
    for size in sizes:
        print(color,size)
