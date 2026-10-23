from pathlib import Path
import os
import sys

# Dynamically locate the video file
video_path = Path(__file__).parent / "MyLife.mp4"
 
if sys.platform == "win32":
    os.startfile(video_path)
elif sys.platform == "darwin":  # macOS
    os.system(f'open "{video_path}"')
else:  # Linux
    os.system(f'xdg-open "{video_path}"')
