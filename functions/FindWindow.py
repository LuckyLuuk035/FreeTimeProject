import win32gui
import numpy as np
from PIL import ImageGrab


def find_window(width, height, colour=(60, 63, 65)):
    bounding_box = {'top': None, 'left': None, 'width': None, 'height': None}
    screen = np.zeros((1080, 1920))
    image = ImageGrab.grab()
    for y in range(0, 1080): # 270
        for x in range(0, 1920): # 430
            color = image.getpixel((x, y))
            an_array = np.where(an_array > 20, 0, an_array)
            if color == colour:
                screen[x][y] = 1
            #     bounding_box['left'] = x
            #     bounding_box['top'] = y
            #     break
    # if not bounding_box['top']:
    #     find_window(width, height, colour)
    # print(bounding_box)
    #
    # bounding_box['width'] = bounding_box['left'] + 1
    # for i in range(width):
    #     links_boven = image.getpixel((bounding_box['left'], bounding_box['top']))
    #     rechts_boven = image.getpixel((bounding_box['left']+i, bounding_box['top']))
    #     if links_boven != rechts_boven:
    #         bounding_box['width'] = i
    #         print(i)
    #         break
    print(screen)
    return bounding_box


# def search_pixel(x_range, y_range, image, colour=(55, 58, 88)):
#     for y in range(0, y_range):
#         for x in range(0, x_range):
#             color = image.getpixel((x, y))