from settings import *


def video_process(path):
  video_dirs = os.listdir(path)
  print(video_dirs)

  for dir in video_dirs:
    dir_path = os.path.join(f"{path}", dir)
    files = sorted(os.listdir(dir_path))
    print(dir)

    clips = []
    for file in files:
        file_path = os.path.join(dir_path, file)
        if file.endswith("png"):
           clip = ImageClip(file_path, duration=4).fx(vfx.fadeout, duration=1)
        else:
           clip = VideoFileClip(file_path).fx(vfx.fadeout, duration=1, audio=False)
        clips.append(clip)

        save_path = "./"
        combined = concatenate_videoclips(clips, method="compose")
        combined.write_videofile(f"{save_path}/{dir}.mp4", fps=60, audio_codec=None)
    
  print("\n=======================================================\n")
  print("==> The video operation is completed")
  print("\n=======================================================\n")
