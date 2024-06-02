#Program for copying an Image
try:
    with open("myimage.jpg","rb") as rp:
        with open("ragh.png","wb") as wp:
            imgdata=rp.read()
            wp.write(imgdata)
            print("Image copied---verify")
except FileNotFoundError:
    print("source image file does not exist")