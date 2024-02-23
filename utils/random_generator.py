from settings import *


def color_generator():
    darkness_threshold = choice([100, 125, 150, 175])
    while True:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)

        brightness = r * 0.299 + g * 0.587 + b * 0.114

        if brightness > darkness_threshold:
            return (r, g, b)
