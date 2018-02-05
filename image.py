import random

# r+ = read and write
img = open("image.ppm", 'w')

# write ppm header
img.write("P3\n500 500\n255\n")

for row in range(500):
    for col in range(500):
        r = random.randint(0,256)
        if (r % 2 == 0):
            r = 100
        g = random.randint(0,256)
        if (g % 2 == 0):
            g = 100
        b = random.randint(0,256)
        if (b % 2 == 0):
            b = 100
        img.write(str(r) + " " + str(g) + " " + str(b) + "  ")

img.close()
