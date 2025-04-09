# 📺 YouTube Channel Video Downloader

A Python script that uses [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) to fetch and download videos from a YouTube channel by specifying individual positions, ranges, or all videos.

---

## ✨ Features

- ✅ Fetches video URLs from a YouTube channel playlist
- ✅ Download all, selected, or a range of videos
- ✅ Intelligent parsing of command-line arguments
- ✅ Supports both full video URLs and video IDs
- ✅ Uses best available video and audio quality

---

## 🧰 Requirements

- Python 3.6+
- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)

Install `yt-dlp` with:

```bash
pip install yt-dlp
```

---

## 🚀 Usage

```bash
python download_youtube_channel.py <channel_url> <positions>
```

### `<channel_url>`

The URL to the YouTube channel's `/videos` page.  
**Example**:  
```
https://www.youtube.com/@SomeChannel/videos
```

### `<positions>`

Specify which videos to download:

- `all` — Download all videos in the playlist
- A list of numbers — e.g. `1 4 14` to download specific videos
- Ranges — e.g. `1-5` to download videos 1 through 5
- Mixed — e.g. `1-3 7 10-12`

---

## ✅ Examples

Download **all** videos:

```bash
python download_youtube_channel.py https://www.youtube.com/@ChannelName/videos all
```

Download **only video 2**:

```bash
python download_youtube_channel.py https://www.youtube.com/@ChannelName/videos 2
```

Download **videos 1, 4, and 14**:

```bash
python download_youtube_channel.py https://www.youtube.com/@ChannelName/videos 1 4 14
```

Download a **range of videos** (1 to 23):

```bash
python download_youtube_channel.py https://www.youtube.com/@ChannelName/videos 1-23
```

Download a **mixed selection**:

```bash
python download_youtube_channel.py https://www.youtube.com/@ChannelName/videos 1-3 7 10-12
```

---

## ⚠️ Notes

- Video position is based on the order returned by `yt-dlp` (usually in upload order).
- Invalid or out-of-range positions will be skipped with a warning.
- This script uses `yt-dlp`'s flat playlist dump, so no video metadata is fetched before download.

---

## 🧑‍💻 License

This project is licensed under the [MIT License](LICENSE).
