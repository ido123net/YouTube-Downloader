from __future__ import annotations

import argparse
import logging

from .convert import convert_to_mp3
from .download import download_urls
from .playlist import get_playlist_urls

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] | %(levelname)s | ( %(name)s ) - %(message)s",
    datefmt="%H:%M:%S",
)


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
        "-p",
        "--playlist-url",
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
    return args


def main():
    args = arg_parse()
    f_urls = urls_from_file(args.file)
    p_urls = get_playlist_urls(args.playlist_url)

    urls = f_urls + args.urls + p_urls
    videos = download_urls(urls=urls, output_path=args.output_path)
    if args.mp3:
        convert_to_mp3(videos=videos, output_path=args.output_path)

def urls_from_file(urls_file):
    try:
        with open(urls_file) as f:
            f_urls = f.read().splitlines()
    except TypeError:
        f_urls = []
    return f_urls


if __name__ == "__main__":
    raise SystemExit(main())
