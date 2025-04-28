import cv2
from detector import Detector
from tracker import Tracker
from detection_logic import update_tracking_events
from video_utils import setup_environment

def main():
    # Setup environment: create dirs, download model & video if needed
    VIDEO_ID = "1pz68D1Gsx80MoPg-_q-IbEdESEmyVLm-"
    setup_environment(video_id=VIDEO_ID)

    # Input video path (downloaded from Google Drive)
    video_path = "videos/input_video.mp4"

    # Initialize detector and tracker
    detector = Detector(model_path='models/yolov8n.pt', conf_threshold=0.5)
    tracker = Tracker()

    # OpenCV video capture
    cap = cv2.VideoCapture(video_path)

    # Check if video opened successfully
    if not cap.isOpened():
        print(f"Error: Cannot open video file {video_path}")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Detect objects in the frame
        detections = detector.detect(frame)

        # Update tracker with current detections
        tracks = tracker.update(detections, frame)

        # Draw bounding boxes and track IDs
        current_ids = []
        for trk in tracks:
            track_id = trk['track_id']
            l, t, r, b = trk['ltrb']
            current_ids.append(track_id)
            # Draw bounding box
            cv2.rectangle(frame, (int(l), int(t)), (int(r), int(b)), (0, 255, 0), 2)
            # Display track ID
            cv2.putText(frame, str(track_id), (int(l), int(t) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Update and log events (new and missing objects)
        update_tracking_events(current_ids)

        # Display the annotated frame
        cv2.imshow("Object Tracking", frame)
        # Break loop on 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
