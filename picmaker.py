img = open("image.ppm", "w")
img.write("P3 500 500 255 ")

for x in range(0, 500):
    for y in range(0, 500):
        a = (abs(x - 256)) % 256
        b = (abs(y - 256)) % 256
        c = (abs(x * y - 256)) % 256
        final_str = "{} {} {} ".format(a, b, c)
        img.write(final_str)
        
print("Name of image: \"image.ppm\"")






