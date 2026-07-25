<p align="center">
  <img src="assets/readme/hero.svg" alt="YouTube Notion Doc Banner" width="100%" />
</p>

<p align="center">
  <a href="https://github.com/nyalakondasheshankadesai-jpg/youtube-notion-doc"><img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python" alt="Python 3.10+" /></a>
  <a href="https://www.notion.so"><img src="https://img.shields.io/badge/Notion-MCP%20Integration-000000?style=flat-square&logo=notion" alt="Notion Integration" /></a>
  <a href="https://youtube.com"><img src="https://img.shields.io/badge/YouTube-Transcript%20Api-FF0000?style=flat-square&logo=youtube" alt="YouTube API" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License MIT" /></a>
</p>

---

## 💡 Overview

**YouTube Notion Doc** is an AI Agent Skill designed to transform YouTube videos and transcripts into comprehensive, domain-aware study documentation in **Notion**. 

Instead of generating generic summary paragraphs, it combines **transcript breakdown**, **targeted timestamp analysis**, and **high-resolution screenshot extraction** to produce structured Notion pages complete with visual evidence, interactive glossaries, action items, and revision questions.

---

## ✨ Key Features

- 🧠 **Domain-Aware Key Moment Identification**: Detects pivotal strategic moves (Chess), structural code shifts (Programming), formula derivations (Mathematics), or slide transitions (Lectures).
- 📸 **Automated High-Res Screenshot Capture**: Extracts exact visual frames at key timestamps using `ffmpeg` & `yt-dlp`.
- 📝 **Rich Notion Page Generation**: Constructs formatted Notion blocks including Callout headers, Image blocks, Checklists, Glossaries, and Quiz questions.
- ⚡ **Seamless Agent Workflow**: Designed for pair-programming agents and automated scripts with minimal setup.

---

## 🛠️ Pipeline Architecture

```text
┌─────────────────┐      ┌─────────────────────────┐      ┌─────────────────────────┐
│  YouTube Video  │ ───► │  Metadata & Subtitles   │ ───► │  Key Moment Selection   │
└─────────────────┘      └─────────────────────────┘      └─────────────────────────┘
                                                                       │
┌─────────────────┐      ┌─────────────────────────┐                   ▼
│   Notion Page   │ ◄─── │  Notion API / MCP Sync │ ◄─── │  Targeted Screenshots   │
└─────────────────┘      └─────────────────────────┘      └─────────────────────────┘
```

---

## 🚀 Quick Start

### 1. Prerequisites
Ensure Python 3.10+ and standard dependencies are installed:
```bash
pip install youtube-transcript-api requests yt-dlp
```

### 2. Extract Transcript & Metadata
Run the metadata extraction script with your YouTube URL:
```bash
python scripts/get_youtube_data.py "https://youtu.be/oIlD1REf6a8" --output-dir "./.tmp"
```
This generates `.tmp/video_info.json` containing structured transcript blocks and video metadata.

### 3. Generate Notion Documentation
Use your Notion Integration Key or Notion MCP server to publish the page:
```bash
python .tmp/upload_screenshots_and_update_notion.py
```

---

## 📂 Directory Structure

```text
youtube-notion-doc/
├── SKILL.md                 # Core AI Agent instructions & documentation template
├── README.md                # Repository overview & setup guide
├── assets/
│   └── readme/
│       └── hero.svg         # SVG hero banner
├── scripts/
│   └── get_youtube_data.py  # Transcript & metadata extraction script
└── evals/
    └── evals.json           # Evaluation test cases
```

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
