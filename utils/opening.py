from settings import *
from utils.text_creations.general import create_bgs
from utils.text_creations.title_creation import create_title
from utils.text_creations.contents_creation import create_contents


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
