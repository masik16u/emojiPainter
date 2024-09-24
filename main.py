from enum import IntEnum

from PIL import Image, ImageFont, ImageDraw
from emoji import unicode_codes

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
    text_image = text_image.resize((32, 32))

    # Collect all pixel values in list
    pixels = [text_image.getpixel((x, y)) for x in range(32) for y in range(32)]

    # Sort and remove transparent pixels
    pixels.sort()
    pixels = list(filter(lambda pixel: pixel != (0, 0, 0, 0), pixels))

    result = (0, 0, 0)

    # MEAN
    if measure == 0:
        result = tuple(round(mean([pixel[rgb] for pixel in pixels])) for rgb in [0, 1, 2])

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


# def get_text_from_file(file_name: str) -> str:
#     """
#     Get all text from the file and put into one string
#
#     :param file_name: Name of the file
#     :return: Whole text in string
#     """
#
#     file = open(file_name)
#     text = ''.join(line for line in file)
#     file.close()
#
#     return text


def get_distance_between_colors(color1: tuple, color2: tuple) -> float:

    return sqrt(sum([pow((color1[rgb] - color2[rgb]) * weight, 2) for (rgb, weight) in [(0, 0.3), (1, 0.59), (2, 0.11)]]))


# # Get emojis list from file
# emojis = get_text_from_file("emojis.txt")

emojis = "🟥🟪🟦🟩🟨🟧🔴🟠🟡🟢🔵🟣❤️🧡💛💚💙💜💙💎🧊💎💙🤍🪽☁︎🐻‍❄️🫧💭🎮🕹️👾💗🎀🌸💖💗🥰💞💚🍵🤍💿🖤📢❗🚨⬜⚪⚫⬛💚✅🎄🍀🌲🐍🌻🍯🐝💛"

# Convert emojis to colors
colors = [(get_center_color(x, MeasureMode.MEAN), x) for x in emojis if x in unicode_codes.EMOJI_DATA]

print(colors)

# Get image to convert to emojis
image = Image.open("test_image_2.png", "r")

# Resize image to the size in emojis
image = image.resize((20, 20))

# Convert each image pixel to RGB values
image_pixels = [[image.getpixel((x, y))[:3] for x in range(20)] for y in range(20)]

# Find the best match for each pixel of the image in available colors
for image_pixel_row in image_pixels:
    for image_pixel in range(len(image_pixel_row)):

        best_match_color = colors[0][0]
        best_match_distance = get_distance_between_colors(image_pixel_row[image_pixel][:3], colors[0][0])

        for color in colors[1:]:

            selected_color_distance = get_distance_between_colors(image_pixel_row[image_pixel][:3], color[0])

            if selected_color_distance < best_match_distance:

                best_match_distance = selected_color_distance
                best_match_color = color

        image_pixel_row[image_pixel] = best_match_color[1]

    print("".join(image_pixel_row))

# old stinky code

# pixelWidth = 1
#
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
#         distance = 500
#
#         for c in colors:
#             new_distance = sqrt((r - c[0][0]) * (r - c[0][0]) + (r - c[0][1]) * (r - c[0][1]) + (r - c[0][2]) * (r - c[0][2]))
#             if new_distance < distance:
#                 distance = new_distance
#                 emoji = c[1]
#
#         line += emoji
#
#     print(line)
