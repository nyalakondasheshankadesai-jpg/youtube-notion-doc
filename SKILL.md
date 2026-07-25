---
name: youtube-notion-doc
description: |
  Create structured Notion documentation from a YouTube video URL using Notion MCP.
  Make sure to use this skill whenever the user provides a YouTube URL, link, or video file and asks to document, take notes, analyze, summarize, or create a Notion page for it.
---

# Intelligent YouTube Video Documentation with Notion MCP

This skill guides you through transforming a YouTube video (or local video file) into structured, high-quality, domain-aware study documentation in Notion. Do not just summarize the transcript; instead, integrate transcript analysis, visual content, and domain context.

## Workflow Overview

1. **Retrieve Video Metadata & Transcript**
2. **Identify Key Moments (Domain-Specific Analysis)**
3. **Capture Targeted Screenshots**
4. **Analyze Visual Elements & Context**
5. **Construct Structured Documentation**
6. **Publish to Notion via Notion MCP**

---

## Detailed Step-by-Step Instructions

### Step 1: Retrieve Video Metadata & Transcript
First, get the video's basic details (title, channel, duration) and its transcript.
- Use the script `scripts/get_youtube_data.py` in this skill folder:
  ```bash
  python youtube-notion-doc/scripts/get_youtube_data.py "<VIDEO_URL_OR_PATH>" --output-dir "./.tmp"
  ```
- This script will generate `.tmp/video_info.json` containing the metadata and transcript.
- Read this file to understand the video structure and content.

### Step 2: Identify Key Moments (Domain-Specific Analysis)
Read the transcript and determine the video's primary domain (e.g., Chess, Programming, Design, Mathematics, or Educational).
Identify **5 to 10** of the most important moments/transitions. Do not use fixed intervals. Look for:
- **Chess**: Major moves, strategic turning points, tactical threats, checkmate setup.
- **Programming**: Code introductions, file structural changes, terminal outputs, architecture explanations.
- **Design**: Figma mockups, UI changes, animation states, before/after visual frames.
- **Mathematics**: Formula derivations, graph plotting, proofs.
- **Educational/General**: Introduction of a key concept, slides, whiteboard drawings, demonstrations.

For each key moment, note the **exact timestamp** (in seconds or `HH:MM:SS` format).

### Step 3: Capture Targeted Screenshots
Use the existing workspace `screenshotskill` capture script to extract high-resolution screenshots at your selected timestamps:
```bash
python c:/Users/shash/OneDrive/Desktop/Anti_gravity_files/.agents/skills/screenshotskill/scripts/capture_video_screenshots.py "<VIDEO_URL_OR_PATH>" -t "<TIMESTAMPS_COMMA_SEPARATED>" -o "./.tmp/screenshots"
```
*Note: Timestamps should be comma-separated, e.g., `-t "00:01:23,00:03:45,00:07:12"`.*
This creates an isolated folder containing the screenshots and a `metadata.json` mapping.

### Step 4: Analyze Visual Elements & Context
Use your file viewing tools to inspect the captured screenshots (e.g. looking at code blocks, board positions, or diagrams in the images) and correlate them with the transcript around those timestamps.
Gather the details for each moment:
- **Timestamp**
- **Image path**
- **Reason for capture**
- **Description of what is happening visually**
- **Why this moment is important**
- **Key observations / nuances**

### Step 5: Construct Structured Documentation
Format the documentation strictly according to this template:

```markdown
# [Video Title]

## Video Information
- **Title**: [Title]
- **Channel**: [Channel/Uploader]
- **Duration**: [Duration in HH:MM:SS]
- **URL**: [YouTube Link]
- **Date Analysed**: [Current Date]

## Video Overview
[Concise summary of the video's purpose, main topic, intended audience, and key learning objectives.]

## Timeline Notes

### Moment 1: [Timestamp] - [Brief Scene Title]
- **Screenshot**: [Local Path to Screenshot Image]
- **Description**: [Visually describe the scene, code, chess board, or slides shown]
- **Key Concepts**: [Bullet points of concepts discussed]
- **Why Important**: [Strategic, technical, or educational value of this moment]
- **Detailed Explanation**: [Detailed notes on what is taught/demonstrated here]
- **Observations**: [Any subtle points, gotchas, or notes]

*(Repeat for each moment)*

## Summary
- **Main Ideas**: [Key takeaways]
- **Best Practices**: [Rules or guidelines mentioned]
- **Common Mistakes**: [Errors or pitfalls discussed]

## Key Concepts Glossary
- **[Term 1]**: [Definition/Explanation]
- **[Term 2]**: [Definition/Explanation]

## Action Items / Exercises
- [ ] [Action Item 1]
- [ ] [Action Item 2]

## Revision Questions
1. [Question 1]
2. [Question 2]
```

### Step 6: Publish to Notion via Notion MCP
Using the Notion MCP, create a page:
1. Search for a suitable parent page or workspace, or ask the user if needed. If none is specified, create it at the root workspace level or under an existing "Video Documentation" page.
2. Create a new Notion page. Set the page title to the video title.
3. Map the markdown sections to Notion Blocks.
   - Use Heading blocks (`heading_1`, `heading_2`, `heading_3`) for sections and moments.
   - Use Paragraph and Callout blocks for explanations and observations.
   - Use Bulleted List and Numbered List blocks for glossary and action items.
   - **IMPORTANT**: Embed the screenshot images. If the Notion MCP supports uploading local files or if the screenshots can be hosted/referenced, add them as Image blocks. If the Notion MCP cannot upload local files directly, reference the local file path clearly as text or embed them using Notion image block URLs (or point the user to the local screenshot directory).
4. Save the page and present the Notion Page URL/ID to the user.
