img = open("image.ppm", "w")
img.write("P3 500 500 255 ")

#if you view this as .ppm, you can get a different result than when you convert to .png or even .tiff (which theoretically should not even be compressed)
for x in range(0, 500):
    for y in range(0, 500):
        a = (abs(x - 256))
        b = (abs(y - 256))
        c = (abs(x * y - 256))
        final_str = "{} {} {} ".format(a, b, c)
        img.write(final_str)
        
print("Name of image: \"image.ppm\"")






