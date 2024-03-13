import os, csv
from sys import argv, exit
from utils.opening import create_opening
from utils.video import video_process, clean_video_folder
from settings import VIDEO_ASSETS, SHORTS_SAVE_PATH

def read_csv(openings):
    with open("./contents_idea - shorts.csv") as f:
        reader = csv.reader(f)
        for row in list(reader)[1:4]:
            filename = row[0]
            title = row[1]
            content = row[2]
            entry = {"title": title, "content": content}
            openings[filename] = entry


def main():
    if not os.path.exists(VIDEO_ASSETS):
        os.makedirs(VIDEO_ASSETS)

    if len(argv) < 2:
        print("Usage: python3 main.py [option], opening or video")
        exit(1)

    action = argv[1]

    openings = {}
    read_csv(openings)

    if action == "opening":
        print("Creating opening image")
        create_opening(openings)
    elif action == "video":
        print("Processing video")
        video_process(SHORTS_SAVE_PATH)
    elif action == "clean":
        print("Cleaning the folder")
        clean_video_folder()
    else:
        print("Unknown action: {action}")


if __name__ == "__main__":
    main()
