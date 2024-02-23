from settings import *
from utils.random_generator import color_generator

PADDING = 10
MAX_WIDTH = 1040


def calc_vertical_position(text_height, content_length, index):
    return HALF_HEIGHT - (text_height * len(content_length) + 1) + index * 100


def create_bgs():
    random_color = list(color_generator()) + [255]

    bg = ColorClip(size=VERTICAL_VIDEO_SIZE, color=RANDOM_DARK_BG)
    bgs = [bg]

    for index in range(1, 5):
        is_random = RANDOM_DARK_BG if not index % 2 else random_color
        calc_w = VIDEO_W - index * PADDING
        calc_h = VIDEO_H - index * PADDING
        # print("check width and height", calc_h, calc_w)

        bg = ColorClip(size=(calc_w, calc_h), color=is_random)
        bg = bg.set_position("center")
        bgs.append(bg)

    combined_bg = CompositeVideoClip(bgs)

    return [combined_bg]


def wrap_text(text, width):
    words = text.split(" ")
    lines = []
    current_line = ""
    for word in words:
        if TextClip(f"{current_line} {word}", fontsize=70).w <= width:
            current_line += " " + word if current_line else word
        else:
            lines.append(current_line.strip())
            current_line = word
    lines.append(current_line.strip())
    return lines


def create_title(title):
    wrapped_title = wrap_text(title, MAX_WIDTH)
    wrapped_title_len = len(wrapped_title) + 1
    SPACING = 100

    title_clips = []

    for index, line in enumerate(wrapped_title):
        print(index, line)
        temp_clip = TextClip(line, fontsize=70, color=FONT_COLOR)
        text_height = temp_clip.h
        SIZE = (VIDEO_W, (text_height + SPACING) * wrapped_title_len)

        line = TextClip(
            line, fontsize=70, font=RANDOM_FONT, color=FONT_COLOR, kerning=3, size=SIZE
        )
        line = line.set_position(("center", index * SPACING))

        title_clips.append(line)
    combined = CompositeVideoClip(title_clips)
    return combined


def create_contents(contents):
    wrapped_contents = wrap_text(contents, MAX_WIDTH)
    print(wrapped_contents)
    wrapped_contents_len = len(wrapped_contents) + 1
    SPACING = 100

    contents_clips = []

    for index, line in enumerate(wrapped_contents):
        print(index, line)
        temp_clip = TextClip(line, fontsize=50, color=FONT_COLOR)
        text_height = temp_clip.h
        print(text_height)
        SIZE = (VIDEO_W, (text_height + SPACING) * wrapped_contents_len)
        # SIZE =(VIDEO_W, 526)

        line = TextClip(
            line, fontsize=50, font=RANDOM_FONT, color=FONT_COLOR, kerning=2, size=SIZE
        )
        line = line.set_position(("center", index * SPACING))

        contents_clips.append(line)
    combined = CompositeVideoClip(contents_clips)
    return combined


def create_opening(openings, output_folder):
    bg = create_bgs()
    display = bg
    # print(openings, output_folder)

    for item in openings.items():
        folder_name = item[0]
        title = item[1]["title"]
        contents = item[1]["content"]

        title = create_title(title)
        title = title.set_position(("center", 200))
        display.append(title)
        print("completed title clips")

        contents = create_contents(contents)
        contents = contents.set_position(("center", 500))
        display.append(contents)
        print("completed contents clips")

        if not os.path.exists(f"{output_folder}/{folder_name}"):
            os.mkdir(f"{output_folder}/{folder_name}")

        combined = CompositeVideoClip(display)
        folder_path = os.path.join(
            f"{output_folder}/{folder_name}", f"{folder_name}.png"
        )
        combined.save_frame(folder_path)
