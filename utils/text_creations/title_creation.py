from moviepy.editor import TextClip, CompositeVideoClip
from utils.text_creations.general import wrap_text
from settings import MAX_WIDTH, TITLE_FONT_SIZE,FONT_COLOR,VIDEO_W, SPACING


def create_title(title, font):
    wrapped_title = wrap_text(title, MAX_WIDTH, TITLE_FONT_SIZE)
    wrapped_title_len = len(wrapped_title) + 1

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
