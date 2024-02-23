import os
from random import choice, randint
from moviepy.editor import (
    VideoFileClip,
    ImageClip,
    ColorClip,
    TextClip,
    vfx,
    CompositeVideoClip,
    concatenate_videoclips,
)


VIDEO_ASSETS = "video"

VERTICAL_VIDEO_SIZE = (1080, 1920)
VIDEO_W, VIDEO_H = VERTICAL_VIDEO_SIZE
HALF_HEIGHT = VIDEO_H // 2
VERTICAL_RATIO = (9, 16)

FONT_COLOR = "rgb(243,244,246)"
FONTS = [
    "Ubuntu-Bold",
    "Helvetica",
    "Helvetica-bold",
    "Fira-Sans-Bold",
    "Fira-Sans-Book",
    "Ubuntu-Mono-Bold",
]
RANDOM_FONT = choice(FONTS)

DARK_BG_COLORS = [
    [40, 40, 40, 255],  # Dark Gray
    [34, 34, 34, 255],  # Charcoal
    [0, 0, 51, 255],  # Deep Blue
    [0, 51, 0, 255],  # Dark Green
    [0, 0, 128, 255],  # Navy Blue
    [51, 0, 0, 255],  # Dark Reddish-Brown
    [51, 0, 51, 255],  # Dark Purple
    [51, 25, 0, 255],  # Chocolate Brown
]
RANDOM_DARK_BG = choice(DARK_BG_COLORS)
