import re

image_expression = re.compile("((in |on |of )?(the |this )?(image\d*) \?)")

img_id = image_expression.findall("what is on the left side of the white oven on the floor and on right side of the blue armchair in the image1 ?")[0][3]

print(img_id)