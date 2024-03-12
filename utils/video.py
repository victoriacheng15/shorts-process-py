from settings import *


def video_process(path, shorts_save_path):
    video_dirs = os.listdir(path)
    print(video_dirs)

    for dir in video_dirs:
        dir_path = os.path.join(f"{path}", dir)
        files = sorted(os.listdir(dir_path))

        clips = []
        for file in files:
            file_path = os.path.join(dir_path, file)
            if file.endswith("png"):
                clip = ImageClip(file_path, duration=4).fx(vfx.fadeout, duration=1)
            else:
                clip = VideoFileClip(file_path).fx(vfx.fadeout, duration=1)
            clips.append(clip)

            combined = concatenate_videoclips(clips, method="compose")
            combined.write_videofile(
                f"{shorts_save_path}/{dir}.mp4", fps=60, audio_codec=None
            )

    print("\n=======================================================\n")
    print("==> The video operation is completed")
    print("\n=======================================================\n")


def clean_video_folder(path):
    entries = os.listdir(path)

    for entry in entries:
        entry_path = os.path.join(path, entry)

        if os.path.isfile(entry_path):
            os.remove(entry_path)
        elif os.path.isdir(entry_path):
            shutil.rmtree(entry_path)
    print(f"All contents of '{path}' have been cleared.")
