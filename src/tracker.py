from deep_sort_realtime.deepsort_tracker import DeepSort

class Tracker:
    def __init__(self, max_age=30, n_init=3, max_iou=0.7):
        # Initialize DeepSORT with default parameters
        self.tracker = DeepSort(max_age=max_age, n_init=n_init, max_iou_distance=max_iou)
    
    def update(self, detections, frame=None):
        # Convert detections to DeepSORT format: [left, top, width, height, confidence, class_id]
        bbs = []
        for det in detections:
            x1, y1, x2, y2, conf, cls = det
            w = x2 - x1
            h = y2 - y1
            bbs.append(([int(x1), int(y1), int(w), int(h)], conf, int(cls)))

        # Update tracks with the current frame detections
        tracks = self.tracker.update_tracks(bbs, frame=frame)
        results = []
        for track in tracks:
            if not track.is_confirmed():
                continue
            track_id = track.track_id
            ltrb = track.to_ltrb()  # (left, top, right, bottom)
            results.append({
                'track_id': track_id,
                'ltrb': ltrb,
                'class_id': track.get_det_class()
            })
        return results
