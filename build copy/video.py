from pathlib import Path
from PIL import Image, ImageTk
from tkinter import Tk, Canvas, Label
import cv2
from mediapipe.python import solutions as mp
from mediapipe.python.solutions import drawing_utils as mp_drawing

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/owen_guo/pushup/build/assets/frame6")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def calculate_angle(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(
        a[1] - b[1], a[0] - b[0]
    )
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle


window = Tk()
window.geometry("1680x1050")
window.configure(bg="#FFFFFF")


canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=1050,
    width=1680,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(960.0, 525.0, image=image_image_1)

canvas.create_rectangle(801.0, 839.0, 1229.0, 928.0, fill="#C74747", outline="")

canvas.create_text(
    849.0,
    860.0,
    anchor="nw",
    text="Start Form Check",
    fill="#FFFFFF",
    font=("RalewayRoman Bold", 40 * -1),
)

canvas.create_rectangle(
    469.0, 199.0, 480.17822265625, 804.0, fill="#FFFFFF", outline=""
)

canvas.create_rectangle(
    1526.81005859375,
    199.0,
    1537.9988403320312,
    803.9999389648438,
    fill="#FFFFFF",
    outline="",
)

canvas.create_rectangle(
    470.0, 792.2178344726562, 1548.0, 802.2178344726562, fill="#FFFFFF", outline=""
)

canvas.create_rectangle(
    471.188720703125, 199.0, 1537.998779296875, 209.0, fill="#FFFFFF", outline=""
)

canvas.create_rectangle(481.0, 81.0, 796.0, 156.0, fill="#938383", outline="")

canvas.create_rectangle(857.0, 81.0, 1172.0, 156.0, fill="#EE7D7D", outline="")

canvas.create_text(
    589.0,
    95.0,
    anchor="nw",
    text="Knee",
    fill="#FFFFFF",
    font=("RalewayRoman Bold", 40 * -1),
)

canvas.create_text(
    943.0,
    95.0,
    anchor="nw",
    text="Normal",
    fill="#FFFFFF",
    font=("RalewayRoman Bold", 40 * -1),
)

canvas.create_rectangle(1233.0, 81.0, 1548.0, 156.0, fill="#938383", outline="")

canvas.create_text(
    1304.0,
    92.0,
    anchor="nw",
    text="Clapping",
    fill="#FFFFFF",
    font=("RalewayRoman Bold", 40 * -1),
)

canvas.create_rectangle(0.0, 0.0, 349.0, 1050.0, fill="#EE7C7C", outline="")

canvas.create_rectangle(0.0, 202.0, 349.0, 285.0, fill="#C74747", outline="")

canvas.create_rectangle(0.0, 285.0, 349.0, 368.0, fill="#C74747", outline="")

canvas.create_rectangle(0.0, 368.0, 349.0, 451.0, fill="#C74747", outline="")

canvas.create_rectangle(0.0, 452.0, 349.0, 535.0, fill="#C74747", outline="")

canvas.create_text(
    51.0,
    469.0,
    anchor="nw",
    text="Progressions",
    fill="#FFFFFF",
    font=("RalewayRoman Bold", 40 * -1),
)

canvas.create_text(
    86.0,
    386.0,
    anchor="nw",
    text="Statistics",
    fill="#FFFFFF",
    font=("RalewayRoman Bold", 40 * -1),
)

canvas.create_text(
    92.0,
    303.0,
    anchor="nw",
    text="Workout",
    fill="#FFFFFF",
    font=("RalewayRoman Bold", 40 * -1),
)

canvas.create_text(
    117.0,
    220.0,
    anchor="nw",
    text="Home",
    fill="#FFFFFF",
    font=("RalewayRoman Bold", 40 * -1),
)

canvas.create_text(
    32.0,
    40.0,
    anchor="nw",
    text="Pushup \nProgressor",
    fill="#FFFFFF",
    font=("RalewayRoman Bold", 55 * -1),
)

canvas.create_rectangle(
    -4.99981689453125,
    193.9786376953125,
    349.0,
    205.02142333984375,
    fill="#FFFFFF",
    outline="",
)
window.resizable(False, False)

video_label = Label(canvas)
video_label.place(
    x=481, y=220, width=1057, height=583
)  # Adjust the width and height as needed

cap = cv2.VideoCapture(0)
counter = 0
check = 0
backbent = False
legsbent = False

## Setup mediapipe instance
with mp.pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:

    def update_video_feed():
        global check, counter
        ret, frame = cap.read()
        if ret:
            # Recolor image to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame.flags.writeable = False

            # Make detection
            results = pose.process(frame)

            # Recolor back to BGR
            frame.flags.writeable = True
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            # Extract landmarks
            try:
                landmarks = results.pose_landmarks.landmark

                # Get coordinates
                shoulder = [
                    landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                    landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y,
                ]
                elbow = [
                    landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                    landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y,
                ]
                wrist = [
                    landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                    landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y,
                ]

                hip = [
                    landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                    landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y,
                ]
                knee = [
                    landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                    landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y,
                ]
                ankle = [
                    landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                    landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y,
                ]

                shoulder = [
                    landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                    landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y,
                ]
                hip = [
                    landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                    landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y,
                ]
                knee = [
                    landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                    landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y,
                ]

                # Calculate angle
                angle = calculate_angle(shoulder, elbow, wrist)
                angle2 = calculate_angle(hip, knee, ankle)
                angle3 = calculate_angle(shoulder, hip, knee)

                # Visualize angle
                cv2.putText(
                    frame,
                    str(angle),
                    tuple(np.multiply(elbow, [640, 480]).astype(int)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (255, 255, 255),
                    2,
                    cv2.LINE_AA,
                )
                cv2.putText(
                    frame,
                    str(angle2),
                    tuple(np.multiply(knee, [640, 480]).astype(int)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (255, 255, 255),
                    2,
                    cv2.LINE_4,
                )
                cv2.putText(
                    frame,
                    str(angle3),
                    tuple(np.multiply(hip, [640, 480]).astype(int)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (255, 255, 255),
                    2,
                    cv2.LINE_8,
                )

                # Counter
                if angle > 160:
                    stage = "down"
                if angle < 100 and stage == "down":
                    stage = "up"
                    counter += 1
                    print(counter)

                # Checking form
                if angle2 > 140:
                    legsbent = True
                elif angle3 > 140:
                    backbent = True
                else:
                    check = 0

                if counter == 5:
                    print("hi")  # Change screens

            except:
                pass

            if check == 1:
                cv2.rectangle(frame, (0, 0), (225, 73), (255, 0, 0), -1)
            if check == 0:
                cv2.rectangle(frame, (0, 0), (225, 73), (0, 0, 255), -1)

            # Rep data
            cv2.putText(
                frame,
                "REPS",
                (15, 12),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 0, 0),
                1,
                cv2.LINE_AA,
            )
            cv2.putText(
                frame,
                str(counter),
                (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX,
                2,
                (255, 255, 255),
                2,
                cv2.LINE_AA,
            )

            # Render detections
            mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp.pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(
                    color=(245, 117, 66), thickness=2, circle_radius=2
                ),
                mp_drawing.DrawingSpec(
                    color=(245, 66, 230), thickness=2, circle_radius=2
                ),
            )

            # Convert image to PIL format
            image = Image.fromarray(frame)

            # Resize image
            image = image.resize(
                (1057, 583), Image.ANTIALIAS
            )  # Adjust the size as needed

            # Convert image to PhotoImage
            photo = ImageTk.PhotoImage(image)

            # Update label with the new image
            video_label.configure(image=photo)
            video_label.image = photo
        else:
            print("Failed to read frame from webcam")
        # Schedule the next update
        video_label.after(10, update_video_feed)

    # Start the video feed update loop
    update_video_feed()

window.mainloop()
