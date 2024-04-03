import os, shutil
from moviepy.editor import ImageClip, VideoFileClip, vfx, concatenate_videoclips
from settings import VIDEO_ASSETS, SHORTS_SAVE_PATH


def video_process():
    video_dirs = os.listdir(VIDEO_ASSETS)
    print(video_dirs)

    for dir in video_dirs:
        dir_path = os.path.join(f"{VIDEO_ASSETS}", dir)
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
                f"{SHORTS_SAVE_PATH}/{dir}.mp4", fps=60, audio_codec=None
            )

    print("\n=======================================================\n")
    print("==> The video operation is completed")
    print("\n=======================================================\n")


def clean_video_folder():
    entries = os.listdir(VIDEO_ASSETS)

    for entry in entries:
        entry_path = os.path.join(VIDEO_ASSETS, entry)

        if os.path.isfile(entry_path):
            os.remove(entry_path)
        elif os.path.isdir(entry_path):
            shutil.rmtree(entry_path)
    print(f"All contents of '{VIDEO_ASSETS}' have been cleared.")
