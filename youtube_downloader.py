
"""
YouTube Downloader Script
This script allows users to download YouTube videos or audio in the best available quality.
It uses yt-dlp to handle the downloading and merging of video and audio streams.
It supports downloading both video with audio and audio only in MP3 format.
"""

import os
import yt_dlp

DOWNLOAD_DIR = "downloaded"


def download_video(url: str):
    """
    Download video from YouTube in the best available quality.
    Downloads both video and audio, merging them into a single MP4 file.
    """

    options = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegMerger',
            'preferedformat': 'mp4',
        }],
    }

    print("🎬 Downloading video (with audio, best available quality)...")
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])
    print(f"✅ Video downloaded to folder: `{DOWNLOAD_DIR}/`")

def download_audio(url: str):
    """
    Download audio from YouTube in MP3 format with maximum quality.
    """

    options = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '0',  # maksymalna jakość
        }],
    }

    print("🎧 Downloading audio (MP3, max quality)...")
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])
    print(f"✅ Audio downloaded to folder: `{DOWNLOAD_DIR}/`")


def main():
    """
    Main function to run the YouTube downloader script.
    Prompts user for video/playlist link and download choice.
    """

    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    url = input("🔗 Enter link to YouTube video or playlist: ").strip()

    print("\nWhat do you want to download?")
    print("1. 🎬 Video (video + audio)")
    print("2. 🎧 Audio only (MP3)")

    choice = input("👉 Choose [1 or 2]: ").strip()

    if choice == '1':
        download_video(url)
    elif choice == '2':
        download_audio(url)
    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()
