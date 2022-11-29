from pathlib import Path
from pytube import YouTube


def download(link: str) -> None:
    """
    Function to download a video on high resolution (without audio) from Youtube

    :param str link:
      Valid URL from the Youtube video
    """
    youtubeObj = YouTube(link)
    youtubeObj = youtubeObj.streams.get_highest_resolution()
    try:
        youtubeObj.download(Path.joinpath(Path.cwd(), "download"))
    except:
        print("An error ocurred")

    print("Download is completed")


if __name__ == "__main__":
    link = input("Enter YT video URL: ")
    download(link)
