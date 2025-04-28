# Vehicle Detection Project

## Overview
This project demonstrates real-time vehicle detection on highway footage using CPU-only processing. It processes high-resolution videos efficiently with lightweight models and optimization techniques.

---

## Hardware Configuration
- **CPU**: 2.3 GHz 14-Core/20-Thread
- **GPU**: Not available
- **RAM**: 16.8 GB

---

## Video Properties
- **Resolution**: 3840×2160
- **Original FPS**: 25.0
- **Achieved FPS**: 1.8 (real-time CPU performance)

---

## Output Video
- Output video link: [Watch Here](https://drive.google.com/file/d/1qZcWAqJpBeISLzZo16vsE7zF7itbEfFx/view?usp=sharing)

---

## Sample Output Frames
- [Frame 1](https://drive.google.com/file/d/1OFNoGLfRGZpZSwreDWuRWg_oeHboy0fP/view?usp=drive_link)
- [Frame 2](https://drive.google.com/file/d/1s9ghXfxhE_tWF-9i3NoGBg4YFpzkuHUA/view?usp=drive_link)

---

## Optimizations and Techniques
- Used a **lightweight model** optimized for **CPU inference**.
- **Batch Size = 1** to enable **real-time, frame-by-frame** processing.
- **Input Resolution resized to 384×640** (maintains aspect ratio) for **faster processing**.
- **Post-processing** with **OpenCV**: drawing bounding boxes around detected vehicles.
- **No dedicated GPU** was used — purely CPU optimized.


---

## Setup and Requirements
```bash
pip install -r requirements.txt
python main.py
