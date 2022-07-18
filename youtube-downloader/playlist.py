from pytube import Playlist


def get_playlist_urls(playlist_url: str):
    try:
        playlist = Playlist(playlist_url)
        return [p for p in playlist]
    except KeyError:
        return []
