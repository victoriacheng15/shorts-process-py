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

    # combined_bg = CompositeVideoClip(bgs)

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


def create_title(title, font):
    wrapped_title = wrap_text(title, MAX_WIDTH, TITLE_FONT_SIZE)
    wrapped_title_len = len(wrapped_title) + 1
    print(font)

    title_clips = []

    for index, line in enumerate(wrapped_title):
        temp_clip = TextClip(
            line, fontsize=TITLE_FONT_SIZE, font=font, color=FONT_COLOR
        )
        text_height = temp_clip.h
        SIZE = (VIDEO_W, (text_height + SPACING) * wrapped_title_len)

        line = TextClip(
            line,
            fontsize=TITLE_FONT_SIZE,
            font=font,
            color=FONT_COLOR,
            kerning=3,
            size=SIZE,
        )
        line = line.set_position(("center", index * SPACING))

        title_clips.append(line)
    combined = CompositeVideoClip(title_clips)
    return combined


def create_contents(contents, font):
    wrapped_contents = wrap_text(contents, MAX_WIDTH, CONTENT_FONT_SIZE)
    wrapped_contents_len = len(wrapped_contents) + 1

    contents_clips = []

    for index, line in enumerate(wrapped_contents):
        temp_clip = TextClip(
            line, fontsize=CONTENT_FONT_SIZE, font=font, color=FONT_COLOR
        )
        text_height = temp_clip.h
        SIZE = (VIDEO_W, (text_height + SPACING) * wrapped_contents_len)

        line = TextClip(
            line,
            fontsize=CONTENT_FONT_SIZE,
            font=font,
            color=FONT_COLOR,
            kerning=2,
            size=SIZE,
        )
        line = line.set_position(("center", index * SPACING))

        contents_clips.append(line)
    combined = CompositeVideoClip(contents_clips)
    return combined


def create_opening(openings, output_folder):
    display_clips = []

    for item in openings.items():
        random_font = choice(FONTS)
        display = create_bgs()
        display_clips.extend(display)

        folder_name = item[0]
        title = item[1]["title"]
        contents = item[1]["content"]

        title = create_title(title, random_font)
        title = title.set_position(("center", SPACING * 2))
        display_clips.append(title)

        contents = create_contents(contents, random_font)
        contents = contents.set_position(("center", SPACING * (2 + 3)))
        display_clips.append(contents)
        print(f"completed contents clips for {folder_name}")

        if not os.path.exists(f"{output_folder}/{folder_name}"):
            os.mkdir(f"{output_folder}/{folder_name}")

        combined = CompositeVideoClip(display_clips)
        folder_path = os.path.join(
            f"{output_folder}/{folder_name}", f"{folder_name}.png"
        )
        combined.save_frame(folder_path)
