from enum import IntEnum

from PIL import Image, ImageFont, ImageDraw
from statistics import mean, median, mode
from math import *

font = ImageFont.truetype("NotoColorEmoji.ttf", 109)


def get_center_color(emoji: str, measure: int) -> tuple:
    """
    Converts text to image and gets median color of it

    :param emoji: Text emoji
    :param measure: Measure mode MEAN MEDIAN or MODE
    :return: Three RGB values in a tuple
    """

    # Create new image
    text_image = Image.new("RGBA", (136, 128), (0, 0, 0, 0))

    # Add emoji on image
    draw = ImageDraw.Draw(text_image)
    draw.text((0, 0), emoji, font=font, embedded_color=True)

    # Resize image for faster calculations
    text_image = text_image.resize((32, 32), resample=Image.Resampling.BOX)

    # Collect all pixel values in list
    pixels = [text_image.getpixel((i, k)) for i in range(32) for k in range(32)]

    # Sort and remove transparent pixels
    pixels.sort()
    pixels = list(filter(lambda a: a != (0, 0, 0, 0), pixels))

    result = (0, 0, 0)

    # Calculate mean color value
    def color_mean(color: int) -> float:
        return round(mean([x[color] for x in pixels]))

    # MEAN
    if measure == 0:
        result = (color_mean(0), color_mean(1), color_mean(2))

    # MEDIAN
    elif measure == 1:
        result = median(pixels)[:3]

    # MODE
    elif measure == 2:
        result = mode(pixels)[:3]

    return result


class MeasureMode(IntEnum):
    MEAN = 0
    MEDIAN = 1
    MODE = 2


print(get_center_color("🌑", MeasureMode.MODE))

pixelWidth = 5

# image = Image.open("test_image.jpg", "r")
# pixels = image.load()
#
# for resultHeight in range(int(image.size[1] / pixelWidth)):
#
#     line = ""
#
#     for resultWidth in range(int(image.size[0] / pixelWidth)):
#
#         r = 0
#         g = 0
#         b = 0
#
#         for i in range(pixelWidth):
#             for k in range(pixelWidth):
#                 r += pixels[i + resultWidth * pixelWidth, k + resultHeight * pixelWidth][0]
#                 g += pixels[i + resultWidth * pixelWidth, k + resultHeight * pixelWidth][1]
#                 b += pixels[i + resultWidth * pixelWidth, k + resultHeight * pixelWidth][2]
#
#         r /= pixelWidth * pixelWidth
#         g /= pixelWidth * pixelWidth
#         b /= pixelWidth * pixelWidth
#
#         er = 255
#         eg = 255
#         eb = 255
#         emoji = ""
#         distance = 1000
#
#         for c in colors:
#             new_distance = sqrt((r - c[0][0]) * (r - c[0][0]) + (r - c[0][1]) * (r - c[0][1]) + (r - c[0][2]) * (r - c[0][2]))
#             if new_distance < distance:
#                 distance = new_distance
#                 emoji = c[1]
#
#         line += emoji
#
#     # print(line)
