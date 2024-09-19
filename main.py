from PIL import Image
from math import *

pixelWidth = 5

'''colors = [((232, 18, 36), '🟥'), ((247, 99, 12), '🟧'), ((255, 241, 0), '🟨'), ((22, 198, 12), '🟩'),
          ((0, 120, 215), '🟦'), ((136, 108, 228), '🟪'), ((142, 86, 46), '🟫'), ((0, 0, 0), '⬛'),
          ((255, 255, 255), '⬜'), ((240, 58, 43), '🍁'), ((244, 149, 191), '🌸'), ((232, 71, 87), '💗'),
          ((19, 161, 14), '🍀'), ((117, 117, 117), '🌑'), ((244, 149, 191), '🌸'), ((244, 149, 191), '🌸'),
          ((244, 149, 191), '🌸'), ((244, 149, 191), '🌸'), ((244, 149, 191), '🌸'), ((244, 149, 191), '🌸'),
          ((244, 149, 191), '🌸'), ((244, 149, 191), '🌸'), ((244, 149, 191), '🌸'), ((244, 149, 191), '🌸'),
          ((244, 149, 191), '🌸'), ((244, 149, 191), '🌸'), ((244, 149, 191), '🌸'), ((244, 149, 191), '🌸')]'''

colors = [((184, 217, 72), '🍈'), ((72, 209, 65), '💚'), ((93, 188, 90), '📗'), ((22, 198, 12), '🟩'),
          ((0, 120, 215), '🟦'), ((136, 108, 228), '🟪'), ((142, 86, 46), '🟫'), ((0, 0, 0), '⬛'),
          ((255, 255, 255), '⬜'), ((240, 58, 43), '🍁'), ((244, 149, 191), '🌸'), ((232, 71, 87), '💗'),
          ((19, 161, 14), '🍀'), ((117, 117, 117), '🌑'), ((244, 149, 191), '🌸'), ((244, 149, 191), '🌸'),
          ((244, 149, 191), '🌸'), ((244, 149, 191), '🌸'), ((244, 149, 191), '🌸'), ((244, 149, 191), '🌸'),
          ((244, 149, 191), '🌸'), ((244, 149, 191), '🌸'), ((244, 149, 191), '🌸'), ((244, 149, 191), '🌸'),
          ((244, 149, 191), '🌸'), ((244, 149, 191), '🌸'), ((244, 149, 191), '🌸'), ((244, 149, 191), '🌸')]

# colors = [((0, 0, 0), '⬛'), ((255, 255, 255), '⬜')]

image = Image.open("test_image.jpg", "r")
pixels = image.load()

for resultHeight in range(int(image.size[1] / pixelWidth)):

    line = ""

    for resultWidth in range(int(image.size[0] / pixelWidth)):

        r = 0
        g = 0
        b = 0

        for i in range(pixelWidth):
            for k in range(pixelWidth):
                r += pixels[i + resultWidth * pixelWidth, k + resultHeight * pixelWidth][0]
                g += pixels[i + resultWidth * pixelWidth, k + resultHeight * pixelWidth][1]
                b += pixels[i + resultWidth * pixelWidth, k + resultHeight * pixelWidth][2]

        r /= pixelWidth * pixelWidth
        g /= pixelWidth * pixelWidth
        b /= pixelWidth * pixelWidth

        er = 255
        eg = 255
        eb = 255
        emoji = ""
        distance = 1000

        for c in colors:
            new_distance = sqrt((r - c[0][0]) * (r - c[0][0]) + (r - c[0][1]) * (r - c[0][1]) + (r - c[0][2]) * (r - c[0][2]))
            if new_distance < distance:
                distance = new_distance
                emoji = c[1]

        line += emoji

    print(line)
