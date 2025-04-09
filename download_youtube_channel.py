import subprocess
import json
import sys
import re

def get_video_urls(channel_url):
    try:
        result = subprocess.run(
            ['yt-dlp', '--flat-playlist', '--dump-json', channel_url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode != 0:
            print("❌ yt-dlp failed:\n", result.stderr)
            return []

        urls = []
        for line in result.stdout.strip().split('\n'):
            try:
                data = json.loads(line)
                if data.get('_type') == 'url' and data.get('url'):
                    video_url = data['url']
                    # Only prepend if it's not already a full URL
                    if not video_url.startswith("http"):
                        video_url = f"https://www.youtube.com/watch?v={video_url}"
                    urls.append(video_url)
            except json.JSONDecodeError:
                continue

        print(f"✅ Found {len(urls)} video(s).")
        return urls

    except Exception as e:
        print(f"❌ Error while extracting video URLs: {e}")
        return []

def parse_positions(args):
    positions = set()

    for arg in args:
        if '-' in arg:
            match = re.match(r'^(\d+)-(\d+)$', arg)
            if match:
                start, end = map(int, match.groups())
                if start <= end:
                    positions.update(range(start, end + 1))
        elif arg.isdigit():
            positions.add(int(arg))

    return sorted(positions)

def download_videos(urls, positions):
    for pos in positions:
        index = pos - 1  # Convert to 0-based index
        if 0 <= index < len(urls):
            url = urls[index]
            print(f"\n⬇️  Downloading video {pos}: {url}")
            try:
                subprocess.run(['yt-dlp', '-f', 'bestvideo+bestaudio/best', url])
            except Exception as e:
                print(f"❌ Failed to download {url}: {e}")
        else:
            print(f"⚠️  Skipping invalid position: {pos}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python download_youtube_channel.py <channel_url> <positions: all | 1 4 14 | 1-23>")
        sys.exit(1)

    channel_url = sys.argv[1]
    args = sys.argv[2:]

    video_urls = get_video_urls(channel_url)

    if not video_urls:
        sys.exit(1)

    if args[0].lower() == "all":
        positions = list(range(1, len(video_urls) + 1))
    else:
        positions = parse_positions(args)

    if not positions:
        print("❌ No valid positions provided.")
        sys.exit(1)

    download_videos(video_urls, positions)
