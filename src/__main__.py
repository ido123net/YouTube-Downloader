from __future__ import annotations

import argparse
import logging
import os

from moviepy.editor import VideoFileClip
from pytube import YouTube

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] | %(levelname)s | ( %(name)s ) - %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "urls",
        nargs="*",
    )
    parser.add_argument(
        "-f",
        "--file",
        type=str,
        default=None,
    )
    parser.add_argument(
        "--mp3",
        action="store_true",
    )
    parser.add_argument(
        "-o",
        "--output-path",
        type=str,
        default="out",
    )
    args = parser.parse_args()
    logger.debug(args)
    return args


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


def convert_to_mp3(videos: list[str], output_path: str = "out"):
    for video in videos:
        filename = os.path.splitext(os.path.split(video)[1])[0]
        VideoFileClip(video).audio.write_audiofile(
            os.path.join(output_path, "audio", f"{filename}.mp3")
        )


def main():
    args = arg_parse()
    try:
        with open(args.file) as f:
            f_urls = f.read().splitlines()
    except TypeError:
        f_urls = []

    urls = f_urls + args.urls
    videos = download_urls(urls=urls, output_path=args.output_path)
    if args.mp3:
        convert_to_mp3(videos=videos, output_path=args.output_path)


if __name__ == "__main__":
    raise SystemExit(main())
