from settings import *
from utils.random_generator import color_generator


def calc_vertical_position(text_height, content_length, index):
    return HALF_HEIGHT - (text_height * len(content_length) + 1) + index * 100


def create_bgs():
    bgs = []

    for index in range(0, 5):
        random_color = list(color_generator()) + [255]
        is_random = choice(DARK_BG_COLORS) if not index % 2 else random_color
        calc_w = VIDEO_W - index * PADDING
        calc_h = VIDEO_H - index * PADDING

        bg = ColorClip(size=(calc_w, calc_h), color=is_random)
        bg = bg.set_position("center")
        bgs.append(bg)
    return bgs


def wrap_text(text, width, font_size):
    words = text.split(" ")
    lines = []
    current_line = ""
    for word in words:
        if TextClip(f"{current_line} {word}", fontsize=font_size).w <= width:
            current_line += " " + word if current_line else word
        else:
            lines.append(current_line.strip())
            current_line = word
    lines.append(current_line.strip())
    return lines
