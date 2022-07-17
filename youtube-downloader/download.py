import logging
import os
from pytube import YouTube

logger = logging.getLogger(__name__)

def download_youtube(youtube: YouTube, output_path: str = "out") -> str:
    logger.info(f"downloading: {youtube.title}")
    stream = youtube.streams.get_highest_resolution()
    output_path = os.path.join(output_path, "video")

    return stream.download(output_path=output_path)


def download_urls(urls: list[str], output_path: str = "out"):
    dowloads = [
        download_youtube(youtube=YouTube(url), output_path=output_path) for url in urls
    ]
    logger.debug(f"downloads: {dowloads}")
    return dowloads