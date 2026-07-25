#!/usr/bin/env python3
import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

def install_package(package_name):
    """Dynamically install python package if missing."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        return True
    except Exception as e:
        print(f"Warning: Failed to install {package_name}: {e}")
        return False

def get_video_metadata(video_url_or_path):
    """Use yt-dlp to extract video metadata."""
    print(f"Extracting metadata for: {video_url_or_path}")
    try:
        # Check if local file
        if os.path.exists(video_url_or_path):
            # Resolve duration with ffprobe if possible
            duration = 0.0
            try:
                cmd = [
                    "ffprobe", "-v", "error", "-show_entries", "format=duration",
                    "-of", "default=noprint_wrappers=1:nokey=1", video_url_or_path
                ]
                output = subprocess.check_output(cmd).decode().strip()
                duration = float(output)
            except Exception:
                pass
            return {
                "title": Path(video_url_or_path).stem,
                "channel": "Local File",
                "duration": duration,
                "duration_raw": str(int(duration)) if duration else "Unknown",
                "url": video_url_or_path,
                "is_local": True
            }

        # Otherwise assume it's a URL
        cmd = ["yt-dlp", "--dump-json", video_url_or_path]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        info = json.loads(result.stdout)
        return {
            "title": info.get("title", "Unknown Video"),
            "channel": info.get("uploader", "Unknown Channel"),
            "duration": info.get("duration", 0.0),
            "duration_raw": info.get("duration_string", "Unknown"),
            "url": video_url_or_path,
            "is_local": False
        }
    except Exception as e:
        print(f"Error fetching metadata: {e}")
        # Return fallback values
        return {
            "title": "Unknown Video",
            "channel": "Unknown Channel",
            "duration": 0.0,
            "duration_raw": "Unknown",
            "url": video_url_or_path,
            "is_local": False,
            "error": str(e)
        }

def get_youtube_transcript(video_url):
    """Attempt to retrieve the transcript for a YouTube URL."""
    try:
        # Extract video ID
        video_id = None
        if "v=" in video_url:
            video_id = video_url.split("v=")[1].split("&")[0]
        elif "youtu.be/" in video_url:
            video_id = video_url.split("youtu.be/")[1].split("?")[0]
        
        if not video_id:
            print("Could not parse YouTube video ID, skipping transcript-api.")
            return None

        try:
            import youtube_transcript_api
        except ImportError:
            print("youtube_transcript_api not installed. Installing...")
            if not install_package("youtube-transcript-api"):
                return None
            import youtube_transcript_api
        
        from youtube_transcript_api import YouTubeTranscriptApi
        
        print(f"Fetching transcript using YouTubeTranscriptApi for ID: {video_id}")
        transcript_list = YouTubeTranscriptApi().fetch(video_id)
        
        # Format transcript
        formatted_transcript = []
        full_text = []
        for entry in transcript_list:
            start = entry.start
            duration = entry.duration
            text = entry.text
            end = start + duration
            formatted_transcript.append({
                "start": start,
                "end": end,
                "text": text
            })
            full_text.append(text)
            
        return {
            "transcript": formatted_transcript,
            "full_text": " ".join(full_text)
        }
    except Exception as e:
        print(f"Failed to fetch transcript with youtube_transcript_api: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Fetch YouTube Metadata and Transcript.")
    parser.add_argument("video", help="YouTube URL or local video path")
    parser.add_argument("-o", "--output-dir", default="./.tmp", help="Output directory")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    metadata = get_video_metadata(args.video)
    
    transcript_data = None
    if not metadata.get("is_local"):
        transcript_data = get_youtube_transcript(args.video)

    output_data = {
        "metadata": metadata,
        "transcript": transcript_data.get("transcript") if transcript_data else [],
        "full_text": transcript_data.get("full_text") if transcript_data else ""
    }

    output_file = output_dir / "video_info.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print(f"Saved video info to: {output_file.resolve()}")

if __name__ == "__main__":
    main()
