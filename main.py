from settings import *
from utils.opening import create_opening
from utils.video import video_process, clean_video_folder


def main():
    if not os.path.exists(VIDEO_ASSETS):
        os.makedirs(VIDEO_ASSETS)

    if len(argv) < 2:
        print("Usage: python3 main.py [option], opening or video")
        exit(1)

    action = argv[1]

    openings = {
        "lorem": {
            "title": "Title Placeolder something",
            "content": "Lorem ipsum dolor sit amet consectetur adipiscing elit",
        },
    }

    if action == "opening":
        print("Creating opening image")
        create_opening(openings, VIDEO_ASSETS)
    elif action == "video":
        print("Processing video")
        video_process(VIDEO_ASSETS)
    elif action == "clean":
        print("Cleaning the folder")
        clean_video_folder(VIDEO_ASSETS)
    else:
        print("Unknown action: {action}")


if __name__ == "__main__":
    main()
