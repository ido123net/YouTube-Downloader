import logging
import os

from moviepy.editor import VideoFileClip

logger = logging.getLogger(__name__)


def convert_to_mp3(videos: list[str], output_path: str = "out"):
    output_folder = os.path.join(output_path, "audio")
    os.makedirs(output_folder, exist_ok=True)
    for video in videos:
        logger.info(f"converting {video} to mp3")
        filename = os.path.splitext(os.path.split(video)[1])[0]
        VideoFileClip(video).audio.write_audiofile(
            os.path.join(output_folder, f"{filename}.mp3")
        )
