from PIL import Image
from math import *

pw = 10

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

image = Image.open("im1.jpg", "r")
pixels = image.load()

for h in range(int(image.size[1] / pw)):

    line = ""

    for w in range(int(image.size[0] / pw)):

        r = 0
        g = 0
        b = 0

        for i in range(pw):
            for k in range(pw):
                r += pixels[i + w * pw, k + h * pw][0]
                g += pixels[i + w * pw, k + h * pw][1]
                b += pixels[i + w * pw, k + h * pw][2]

        r /= pw * pw
        g /= pw * pw
        b /= pw * pw

        er = 255
        eg = 255
        eb = 255
        color = ""
        distance = 1000

        for c in colors:
            new_distance = sqrt((r - c[0][0]) * (r - c[0][0]) + (r - c[0][1]) * (r - c[0][1]) + (r - c[0][2]) * (r - c[0][2]))
            if new_distance < distance:
                distance = new_distance
                color = c[1]

        line += color

    print(line)
