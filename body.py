# import cv2
# import mediapipe as mp
# import numpy as np
# from ultralytics import YOLO

# # Create mediapipe instance
# mp_drawing = mp.solutions.drawing_utils
# mp_drawing_styles = mp.solutions.drawing_styles
# mp_holistic = mp.solutions.holistic

# # Initialize mediapipe instance
# holistic = mp_holistic.Holistic(
#     min_detection_confidence=0.3,
#     min_tracking_confidence=0.3
# )

# # Initialize webcam
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# # Load YOLOv8 model (trained on Roboflow)
# model = YOLO("NEW FINAL.pt")  # Ensure this path is correct

# # Optional: Add class names if your model doesn't include them
# # model.names = ["A", "B", "C", ..., "Z"]  # Customize as needed

# # Draw landmarks on the image
# def draw_landmarks(image, results):
#     if results.left_hand_landmarks:
#         mp_drawing.draw_landmarks(
#             image,
#             results.left_hand_landmarks,
#             mp_holistic.HAND_CONNECTIONS,
#             mp_drawing_styles.get_default_hand_landmarks_style()
#         )
#     if results.right_hand_landmarks:
#         mp_drawing.draw_landmarks(
#             image,
#             results.right_hand_landmarks,
#             mp_holistic.HAND_CONNECTIONS,
#             mp_drawing_styles.get_default_hand_landmarks_style()
#         )
#     if results.pose_landmarks:
#         mp_drawing.draw_landmarks(
#             image,
#             results.pose_landmarks,
#             mp_holistic.POSE_CONNECTIONS,
#             mp_drawing_styles.get_default_pose_landmarks_style()
#         )
#     return image

# letter = ""
# offset = 1

# # Collect data from webcam and process using YOLOv8
# def collectData():
#     ret, frame = cap.read()
#     global letter

#     original = frame.copy()
#     crop_bg = np.zeros(frame.shape, dtype=np.uint8)
#     black = np.zeros(frame.shape, dtype=np.uint8)

#     image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     image.flags.writeable = False

#     results = holistic.process(image)

#     image.flags.writeable = True
#     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

#     draw_landmarks(image, results)
#     draw_landmarks(black, results)

#     # Run YOLOv8 inference
#     results_yolo = model(black)[0]  # First result

#     pred_img = black.copy()
#     for box in results_yolo.boxes:
#         conf = float(box.conf[0])
#         cls_id = int(box.cls[0])
#         if conf > 0.8:
#             x1, y1, x2, y2 = map(int, box.xyxy[0])
#             x1 = max(x1 - offset, 0)
#             y1 = max(y1 - offset, 0)
#             x2 = max(x2 + offset, 0)
#             y2 = max(y2 + offset, 0)

#             crop_img = black[y1:y2, x1:x2]
#             crop_bg[y1:y2, x1:x2] = crop_img

#             name = model.names[cls_id]

#             # Optionally draw box on pred_img
#             cv2.rectangle(pred_img, (x1, y1), (x2, y2), (255, 0, 0), 2)
#             cv2.putText(pred_img, name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

#             return image, pred_img, original, crop_bg, name

#     return image, pred_img, original, crop_bg, letter



import cv2
import numpy as np
from ultralytics import YOLO

# Initialize webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Load your YOLOv8 model trained on A-Z
model = YOLO("NEW FINAL.pt")  # adjust path if needed

# Define labels A-Z explicitly
labels = {i: chr(65 + i) for i in range(26)}  # 0:'A', 1:'B', ..., 25:'Z'

offset = 5  # padding for bbox

def collectData():
    ret, frame = cap.read()
    if not ret:
        return None, None, None, None, "--"
    
    results = model(frame)[0]  # get first result
    
    pred_img = frame.copy()
    detected_label = "--"
    
    for box in results.boxes:
        conf = float(box.conf[0])
        cls_id = int(box.cls[0])
        if conf > 0.6:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            # Draw bounding box and label
            cv2.rectangle(pred_img, (x1 - offset, y1 - offset), (x2 + offset, y2 + offset), (0, 255, 0), 2)
            
            # Use labels dict instead of model.names
            name = labels.get(cls_id, "--")
            
            cv2.putText(pred_img, f"{name} {conf:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
            detected_label = name
            break  # first detected object only
    
    return frame, pred_img, frame.copy(), np.zeros(frame.shape, dtype=np.uint8), detected_label

