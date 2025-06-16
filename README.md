# 🎬 YouTube Downloader - ridiculously simple :)

This is a **super simple YouTube downloader** built with [`yt-dlp`](https://github.com/yt-dlp/yt-dlp).
No fluff, no fancy GUI - just run it, paste a link, choose what you want (video+audio or just audio), and boom 💥 - downloaded.

Honestly, there’s not much more to say.

---

## 🛠️ Installation

1. Make sure you have Python (tested on 3.13)
2. Install required packages:

```bash
pip install -r requirements.txt
# or
pip install yt-dlp
```

3. Also make sure ffmpeg is installed and available in your PATH (used for merging video/audio or converting audio) -> https://ffmpeg.org/download.html

---

## ▶️ Usage

```bash
python youtube_downloader.py
```

You'll be asked to:
- Paste a YouTube link (video or playlist)
- Choose if you want to download 🎬 video+audio or 🎧 audio only (as MP3)
- The file(s) will be saved in the `downloaded/` folder automatically

---

## ✅ Features

- Downloads full videos (best quality available)
- Extracts high-quality MP3 audio
- Supports playlists (one by one)
- Creates output folder if it doesn't exist
- Uses the awesome power of yt-dlp

---

## 🧼 That's it!

It's not a rocket launcher. It's just a clean little script that gets the job done.

Enjoy! 😎
