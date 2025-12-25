from PIL import Image

image = Image.open("image.jpg")
red, green, blue = image.split() 

coordinates_left_red = (50, 0, red.width, red.height)
left_red = red.crop(coordinates_left_red)
coordinates_middle_red = (25, 0, 671, red.height)
middle_red = red.crop(coordinates_middle_red)
blend_red = Image.blend(left_red, middle_red, 0.5)

coordinates_right_blue = (0, 0, 646, blue.height)
right_blue = blue.crop(coordinates_right_blue)
coordinates_middle_blue = (25, 0, 671, blue.height)
middle_blue = blue.crop(coordinates_middle_blue)
blend_blue = Image.blend(right_blue, middle_blue, 0.5)

coordinates_middle_green = (25, 0, 671, green.height)
middle_green = green.crop(coordinates_middle_green)

blend_image = Image.merge("RGB", (blend_red, middle_green, blend_blue))
blend_image.save("blend_image.jpg")

blend_image.thumbnail((80, 80))
blend_image.save("blend_framed_image.jpg")



