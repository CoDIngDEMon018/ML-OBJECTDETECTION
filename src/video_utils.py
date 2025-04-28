import os
import gdown

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def setup_environment(model_dir='models', video_dir='videos', log_dir='logs', video_id=None):
    
    # Create directories if they don't exist
    ensure_dir(model_dir)
    ensure_dir(video_dir)
    ensure_dir(log_dir)

    # Path for the YOLOv8n model
    model_path = os.path.join(model_dir, 'yolov8n.pt')
    # Download YOLOv8n model if not present
    if not os.path.exists(model_path):
        print(f"Downloading YOLOv8 Nano model to {model_path}...")
        try:
            from ultralytics import YOLO
            # Load model (downloads weights)
            model = YOLO('yolov8n.pt')
            # Save weights to the model path
            model.save(model_path)
            print("YOLOv8 model downloaded and saved successfully.")
        except Exception as e:
            print(f"Failed to download YOLOv8n model: {e}")

    # Download video from Google Drive if ID is provided
    if video_id:
        video_path = os.path.join(video_dir, 'input_video.mp4')
        if not os.path.exists(video_path):
            print(f"Downloading video from Google Drive ID {video_id} to {video_path}...")
            url = f'https://drive.google.com/uc?id={video_id}'
            try:
                gdown.download(url, video_path, quiet=False)
                print("Video downloaded successfully.")
            except Exception as e:
                print(f"Failed to download video: {e}")

    # Create events.csv log file with header if not present
    events_path = os.path.join(log_dir, 'events.csv')
    if not os.path.exists(events_path):
        with open(events_path, 'w') as f:
            f.write('timestamp,event,object_id\n')
        print(f"Created log file {events_path}.")
