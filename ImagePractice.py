from byuimage import Image
image = Image("Vader.jpg")
def createBorder(image):
    borderImage = Image.blank(image.width + 20, image.height + 20)
    for pixel in borderImage:
        pixel.red = 150
        pixel.green = 100
        pixel.blue = 100
    borderImage.show()
createBorder(image)

