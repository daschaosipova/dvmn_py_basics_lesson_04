from PIL import Image

image = Image.open("image.jpg")
red, green, blue = image.split() 

coordinates_red_left = (50, 0, red.width, red.height)
red_left = red.crop(coordinates_red_left)
coordinates_red_middle = (25, 0, 671, red.height)
red_middle = red.crop(coordinates_red_middle)
blend_red = Image.blend(red_left, red_middle, 0.5)

coordinates_blue_right = (0, 0, 646, blue.height)
blue_right = blue.crop(coordinates_blue_right)
coordinates_blue_middle = (25, 0, 671, blue.height)
blue_middle = blue.crop(coordinates_blue_middle)
blend_blue = Image.blend(blue_right, blue_middle, 0.5)

coordinates_green_middle = (25, 0, 671, green.height)
green_crop = green.crop(coordinates_green_middle)

blend_image = Image.merge("RGB", (blend_red, blend_blue, green_crop))
blend_image.save("blend_image.jpg")

blend_image.thumbnail((80, 80))
blend_image.save("blend_image_frame.jpg")



