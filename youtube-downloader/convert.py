import logging
import os

from moviepy.editor import VideoFileClip

logger = logging.getLogger(__name__)


def convert_to_mp3(videos: list[str], output_path: str = "out"):
    for video in videos:
        logger.info(f"converting {video} to mp3")
        filename = os.path.splitext(os.path.split(video)[1])[0]
        VideoFileClip(video).audio.write_audiofile(
            os.path.join(output_path, "audio", f"{filename}.mp3")
        )
