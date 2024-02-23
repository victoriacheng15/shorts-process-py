from settings import *
from utils.text_creations.general import wrap_text


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