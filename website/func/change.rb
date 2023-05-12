require 'chunky_png'

image = ChunkyPNG::Image.from_file('input_image.jpg')
image.save('output_image.png')