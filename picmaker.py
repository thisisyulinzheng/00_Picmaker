img = open("image.ppm", "w")
img.write("P3 500 500 255 ")

#tried a bunch of more complicated things with if statements and whatnot, but who knew something this simple could create such an awesome effect 
for x in range(0, 500):
    for y in range(0, 500):
        a = (abs(x - 256))
        b = (abs(y - 256))
        c = (abs(x * y - 256))
        final_str = "{} {} {} ".format(a, b, c)
        img.write(final_str)
        
print("Name of image: \"image.ppm\"")






