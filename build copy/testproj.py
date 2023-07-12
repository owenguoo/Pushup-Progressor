from pathlib import Path
from tkinter import Tk, Canvas, Text, PhotoImage, Button
from tkinter import *
from tkvideo import tkvideo

from pathlib import Path
from PIL import Image, ImageTk
from tkinter import Tk, Canvas, Label
import cv2
import numpy as np
from mediapipe.python import solutions as mp
from mediapipe.python.solutions import drawing_utils as mp_drawing
from mediapipe.python.solutions import pose as mp_pose

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH_1 = OUTPUT_PATH / Path(r"/Users/owen_guo/pushup/build/assets/frame6")
ASSETS_PATH_2 = OUTPUT_PATH / Path(r"/Users/owen_guo/pushup/build/assets/frame5")

NAVIGATION_BAR_HEIGHT = 50
PAGE_BACKGROUND_COLORS = ["#FFD700", "#00BFFF", "#90EE90", "#FFA07A"]


def relative_to_assets(path: str, assets_path: Path) -> Path:
    return assets_path / Path(path)


class MultipageApplication:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1680x1050")
        self.window.configure(bg="#FFFFFF")

        self.pages = []
        self.current_page = 0

        self.navigation_bar = Canvas(
            self.window,
            bg="#FFFFFF",
            height=NAVIGATION_BAR_HEIGHT,
            width=1680,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        self.navigation_bar.place(x=0, y=0)

        home_button = Button(
            self.navigation_bar,
            text="Home",
            font=("RalewayRoman Bold", 14),
            command=self.show_home_page,
        )
        home_button.place(x=20, y=10)

        workout_button = Button(
            self.navigation_bar,
            text="Workout",
            font=("RalewayRoman Bold", 14),
            command=self.show_workout_page,
        )
        workout_button.place(x=100, y=10)

        statistics_button = Button(
            self.navigation_bar,
            text="Statistics",
            font=("RalewayRoman Bold", 14),
            command=self.show_statistics_page,
        )
        statistics_button.place(x=200, y=10)

        progressions_button = Button(
            self.navigation_bar,
            text="Progressions",
            font=("RalewayRoman Bold", 14),
            command=self.show_progressions_page,
        )
        progressions_button.place(x=320, y=10)

        self.load_pages()

    def load_pages(self):
        # Load page 1
        canvas_1 = Canvas(
            self.window,
            bg=PAGE_BACKGROUND_COLORS[0],
            height=1050 - NAVIGATION_BAR_HEIGHT,
            width=1680,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        canvas_1.place(x=0, y=NAVIGATION_BAR_HEIGHT)
        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png", ASSETS_PATH_1)
        )
        image_1 = canvas_1.create_image(960.0, 525.0, image=image_image_1)
        page_1_header = Text(
            canvas_1,
            bd=0,
            bg=PAGE_BACKGROUND_COLORS[0],
            fg="#000000",
            font=("RalewayRoman Bold", 30),
            height=1,
            width=20,
        )

        # My shit
        canvas_1.create_rectangle(
            801.0, 839.0, 1229.0, 928.0, fill="#C74747", outline=""
        )

        canvas_1.create_text(
            849.0,
            860.0,
            anchor="nw",
            text="Start Form Check",
            fill="#FFFFFF",
            font=("RalewayRoman Bold", 40 * -1),
        )

        canvas_1.create_rectangle(
            469.0, 199.0, 480.17822265625, 804.0, fill="#FFFFFF", outline=""
        )

        canvas_1.create_rectangle(
            1526.81005859375,
            199.0,
            1537.9988403320312,
            803.9999389648438,
            fill="#FFFFFF",
            outline="",
        )

        canvas_1.create_rectangle(
            470.0,
            792.2178344726562,
            1548.0,
            802.2178344726562,
            fill="#FFFFFF",
            outline="",
        )

        canvas_1.create_rectangle(
            471.188720703125,
            199.0,
            1537.998779296875,
            209.0,
            fill="#FFFFFF",
            outline="",
        )

        canvas_1.create_rectangle(481.0, 81.0, 796.0, 156.0, fill="#938383", outline="")

        canvas_1.create_rectangle(
            857.0, 81.0, 1172.0, 156.0, fill="#EE7D7D", outline=""
        )

        canvas_1.create_text(
            589.0,
            95.0,
            anchor="nw",
            text="Knee",
            fill="#FFFFFF",
            font=("RalewayRoman Bold", 40 * -1),
        )

        canvas_1.create_text(
            943.0,
            95.0,
            anchor="nw",
            text="Normal",
            fill="#FFFFFF",
            font=("RalewayRoman Bold", 40 * -1),
        )

        canvas_1.create_rectangle(
            1233.0, 81.0, 1548.0, 156.0, fill="#938383", outline=""
        )

        canvas_1.create_text(
            1304.0,
            92.0,
            anchor="nw",
            text="Clapping",
            fill="#FFFFFF",
            font=("RalewayRoman Bold", 40 * -1),
        )

        canvas_1.create_rectangle(0.0, 0.0, 349.0, 1050.0, fill="#EE7C7C", outline="")

        canvas_1.create_rectangle(0.0, 202.0, 349.0, 285.0, fill="#C74747", outline="")

        canvas_1.create_rectangle(0.0, 285.0, 349.0, 368.0, fill="#C74747", outline="")

        canvas_1.create_rectangle(0.0, 368.0, 349.0, 451.0, fill="#C74747", outline="")

        canvas_1.create_rectangle(0.0, 452.0, 349.0, 535.0, fill="#C74747", outline="")

        canvas_1.create_text(
            51.0,
            469.0,
            anchor="nw",
            text="Progressions",
            fill="#FFFFFF",
            font=("RalewayRoman Bold", 40 * -1),
        )

        canvas_1.create_text(
            86.0,
            386.0,
            anchor="nw",
            text="Statistics",
            fill="#FFFFFF",
            font=("RalewayRoman Bold", 40 * -1),
        )

        canvas_1.create_text(
            92.0,
            303.0,
            anchor="nw",
            text="Workout",
            fill="#FFFFFF",
            font=("RalewayRoman Bold", 40 * -1),
        )

        canvas_1.create_text(
            117.0,
            220.0,
            anchor="nw",
            text="Home",
            fill="#FFFFFF",
            font=("RalewayRoman Bold", 40 * -1),
        )

        canvas_1.create_text(
            32.0,
            40.0,
            anchor="nw",
            text="Pushup \nProgressor",
            fill="#FFFFFF",
            font=("RalewayRoman Bold", 55 * -1),
        )

        canvas_1.create_rectangle(
            -4.99981689453125,
            193.9786376953125,
            349.0,
            205.02142333984375,
            fill="#FFFFFF",
            outline="",
        )
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

        video_label = Label(canvas_1)
        video_label.place(
            x=481, y=220, width=1057, height=583
        )  # Adjust the width and height as needed

        cap = cv2.VideoCapture(0)
        counter = 0
        check = 0
        legsBent = False
        backBent = False

        ## Setup mediapipe instance
        with mp_pose.Pose(
            min_detection_confidence=0.5, min_tracking_confidence=0.5
        ) as pose:
            while cap.isOpened():
                ret, frame = cap.read()

                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Make detection
                results = pose.process(image)

                # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

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
                        image,
                        str(angle),
                        tuple(np.multiply(elbow, [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (255, 255, 255),
                        2,
                        cv2.LINE_AA,
                    )
                    cv2.putText(
                        image,
                        str(angle2),
                        tuple(np.multiply(knee, [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (255, 255, 255),
                        2,
                        cv2.LINE_4,
                    )
                    cv2.putText(
                        image,
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
                    if angle < 100 and stage == "down" and counter < 5:
                        stage = "up"
                        counter += 1
                        print(counter)

                    if angle2 > 140:
                        legsBent = True
                        check += 1
                    if angle3 > 140:
                        backBent = True
                        check += 1
                    else:
                        check += 0

                except:
                    pass
                    if counter == 5:
                        print("Score: " + 5 - check + "/5")  # Change screens
                        if legsBent == True:
                            print("No bend legs")
                        if backBent == True:
                            print("No bend back")
                        if legsBent != True and backBent != True:
                            print("Good job")

                if check == 1:
                    cv2.rectangle(image, (0, 0), (225, 73), (255, 0, 0), -1)
                if check == 0:
                    cv2.rectangle(image, (0, 0), (225, 73), (0, 0, 255), -1)

                # Rep data
                cv2.putText(
                    image,
                    "REPS",
                    (15, 12),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 0, 0),
                    1,
                    cv2.LINE_AA,
                )
                cv2.putText(
                    image,
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
                    image,
                    results.pose_landmarks,
                    mp_pose.POSE_CONNECTIONS,
                    mp_drawing.DrawingSpec(
                        color=(245, 117, 66), thickness=2, circle_radius=2
                    ),
                    mp_drawing.DrawingSpec(
                        color=(245, 66, 230), thickness=2, circle_radius=2
                    ),
                )

                cv2.imshow("Mediapipe Feed", image)
                if cv2.waitKey(10) & 0xFF == ord("q"):
                    break

        self.window.mainloop()
        presshome_button = Button(
            text="Home",
            font=("RalewayRoman Bold", 50),
            fg="#FFFFFF",
            highlightbackground="#D9D9D9",
            command=self.show_home_page,
        )
        presshome_button.place(x=80, y=260)

        pressworkout_button = Button(
            text="Workout",
            font=("RalewayRoman Bold", 50),
            fg="#FFFFFF",
            highlightbackground="#D9D9D9",
            command=self.show_workout_page,
        )
        pressworkout_button.place(x=60, y=340)

        pressstats_button = Button(
            text="Statistics",
            font=("RalewayRoman Bold", 50),
            fg="#FFFFFF",
            highlightbackground="#D9D9D9",
            command=self.show_workout_page,
        )
        pressstats_button.place(x=55, y=420)

        presslog_button = Button(
            text="Progressions",
            font=("RalewayRoman Bold", 50),
            fg="#FFFFFF",
            highlightbackground="#D9D9D9",
            command=self.show_progressions_page,
        )
        presslog_button.place(x=10, y=500)

        start_button = Button(
            text="Start Form Check",
            font=("RalewayRoman Bold", 50),
            fg="#FFFFFF",
            highlightbackground="#D9D9D9",
            command=self.show_workout_page,
        )
        start_button.place(x=800, y=875)

        self.pages.append(canvas_1)

        # Load page 2
        canvas_2 = Canvas(
            self.window,
            bg=PAGE_BACKGROUND_COLORS[1],
            height=1050 - NAVIGATION_BAR_HEIGHT,
            width=1680,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        canvas_2.place(x=0, y=NAVIGATION_BAR_HEIGHT)

        page_2_header = Text(
            canvas_2,
            bd=0,
            bg=PAGE_BACKGROUND_COLORS[1],
            fg="#000000",
            font=("RalewayRoman Bold", 30),
            height=1,
            width=20,
        )

        canvas_2.create_rectangle(
            743.0, 716.0, 1460.0, 767.0, fill="#D9D9D9", outline=""
        )

        canvas_2.create_rectangle(
            743.0, 716.0, 1280.0, 767.0, fill="#C74747", outline=""
        )

        canvas_2.create_text(
            562.0,
            712.0,
            anchor="nw",
            text="Rating: ",
            fill="#FFFFFF",
            font=("RalewayRoman Bold", 50 * -1),
        )

        canvas_2.create_rectangle(
            499.0, 88.0, 1504.0, 652.0, fill="#000000", outline=""
        )

        canvas_2.create_rectangle(
            487.0, 67.0, 498.1405944824219, 653.0, fill="#FFFFFF", outline=""
        )

        canvas_2.create_rectangle(
            1493.10009765625,
            67.0,
            1504.2261962890625,
            653.0,
            fill="#FFFFFF",
            outline="",
        )

        presshome_button = Button(
            text="Home",
            font=("RalewayRoman Bold", 50),
            fg="#FFFFFF",
            highlightbackground="#D9D9D9",
            command=self.show_home_page,
        )
        presshome_button.place(x=80, y=260)

        pressworkout_button = Button(
            text="Workout",
            font=("RalewayRoman Bold", 50),
            fg="#FFFFFF",
            highlightbackground="#D9D9D9",
            command=self.show_workout_page,
        )
        pressworkout_button.place(x=60, y=340)

        pressstats_button = Button(
            text="Statistics",
            font=("RalewayRoman Bold", 50),
            fg="#FFFFFF",
            highlightbackground="#D9D9D9",
            command=self.show_workout_page,
        )
        pressstats_button.place(x=55, y=420)

        presslog_button = Button(
            text="Progressions",
            font=("RalewayRoman Bold", 50),
            fg="#FFFFFF",
            highlightbackground="#D9D9D9",
            command=self.show_progressions_page,
        )
        presslog_button.place(x=10, y=500)

        canvas_2.create_rectangle(
            488.0, 641.0, 1516.0, 651.0, fill="#FFFFFF", outline=""
        )

        canvas_2.create_rectangle(489.0, 67.0, 1504.0, 77.0, fill="#FFFFFF", outline="")

        canvas_2.create_rectangle(0.0, 0.0, 349.0, 1050.0, fill="#EE7C7C", outline="")

        canvas_2.create_rectangle(0.0, 202.0, 349.0, 285.0, fill="#C74747", outline="")

        canvas_2.create_text(
            51.0,
            469.0,
            anchor="nw",
            text="Progressions",
            fill="#FFFFFF",
            font=("RalewayRoman Bold", 40 * -1),
        )

        canvas_2.create_text(
            86.0,
            386.0,
            anchor="nw",
            text="Statistics",
            fill="#FFFFFF",
            font=("RalewayRoman Bold", 40 * -1),
        )

        canvas_2.create_text(
            117.0,
            220.0,
            anchor="nw",
            text="Home",
            fill="#FFFFFF",
            font=("RalewayRoman Bold", 40 * -1),
        )

        canvas_2.create_text(
            32.0,
            40.0,
            anchor="nw",
            text="Pushup \nProgressor",
            fill="#FFFFFF",
            font=("RalewayRoman Bold", 55 * -1),
        )

        canvas_2.create_rectangle(
            -4.99981689453125,
            193.9786376953125,
            349.0,
            205.0213623046875,
            fill="#FFFFFF",
            outline="",
        )

        canvas_2.create_text(
            32.0,
            40.0,
            anchor="nw",
            text="Pushup \nProgressor",
            fill="#FFFFFF",
            font=("RalewayRoman Bold", 55 * -1),
        )

        canvas_2.create_rectangle(
            -4.99981689453125,
            193.9786376953125,
            349.0,
            205.0213623046875,
            fill="#FFFFFF",
            outline="",
        )

        self.pages.append(canvas_2)

        # Load page 3
        canvas_3 = Canvas(
            self.window,
            bg=PAGE_BACKGROUND_COLORS[2],
            height=1050 - NAVIGATION_BAR_HEIGHT,
            width=1680,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        canvas_3.place(x=0, y=NAVIGATION_BAR_HEIGHT)
        page_3_header = Text(
            canvas_3,
            bd=0,
            bg=PAGE_BACKGROUND_COLORS[2],
            fg="#000000",
            font=("RalewayRoman Bold", 30),
            height=1,
            width=20,
        )

        canvas_3.create_text(
            795.0,
            89.0,
            anchor="nw",
            text="Statistics",
            fill="#FFFFFF",
            font=("RalewayRoman Bold", 100 * -1),
        )

        canvas_3.create_text(
            439.0,
            208.0,
            anchor="nw",
            text="Workout Log",
            fill="#FFFFFF",
            font=("RalewayRoman Bold", 70 * -1),
        )

        canvas_3.create_text(
            32.0,
            40.0,
            anchor="nw",
            text="Pushup \nProgressor",
            fill="#FFFFFF",
            font=("RalewayRoman Bold", 55 * -1),
        )

        canvas_3.create_rectangle(
            -4.99981689453125,
            193.978515625,
            349.0,
            205.021484375,
            fill="#FFFFFF",
            outline="",
        )

        canvas_3.create_rectangle(0.0, 0.0, 349.0, 1050.0, fill="#EE7C7C", outline="")

        canvas_3.create_rectangle(0.0, 493.0, 349.0, 576.0, fill="#C74747", outline="")

        canvas_3.create_rectangle(
            0.0, 402.5, 349.0, 493.28125, fill="#C74747", outline=""
        )

        presshome_button = Button(
            text="Home",
            font=("RalewayRoman Bold", 50),
            fg="#FFFFFF",
            highlightbackground="#D9D9D9",
            command=self.show_home_page,
        )
        presshome_button.place(x=80, y=260)

        pressworkout_button = Button(
            text="Workout",
            font=("RalewayRoman Bold", 50),
            fg="#FFFFFF",
            highlightbackground="#D9D9D9",
            command=self.show_workout_page,
        )
        pressworkout_button.place(x=60, y=340)

        pressstats_button = Button(
            text="Statistics",
            font=("RalewayRoman Bold", 50),
            fg="#FFFFFF",
            highlightbackground="#D9D9D9",
            command=self.show_workout_page,
        )
        pressstats_button.place(x=55, y=420)

        presslog_button = Button(
            text="Progressions",
            font=("RalewayRoman Bold", 50),
            fg="#FFFFFF",
            highlightbackground="#D9D9D9",
            command=self.show_progressions_page,
        )
        presslog_button.place(x=10, y=500)

        canvas_3.create_text(
            51.0,
            512.96875,
            anchor="nw",
            text="Progressions",
            fill="#FFFFFF",
            font=("RalewayRoman Bold", 40 * -1),
        )

        canvas_3.create_text(
            117.0,
            240.625,
            anchor="nw",
            text="Home",
            fill="#FFFFFF",
            font=("RalewayRoman Bold", 40 * -1),
        )

        canvas_3.create_text(
            86.0,
            422.1875,
            anchor="nw",
            text="Statistics",
            fill="#FFFFFF",
            font=("RalewayRoman Bold", 40 * -1),
        )

        canvas_3.create_rectangle(1.0, 320.0, 350.0, 403.0, fill="#C74747", outline="")

        canvas_3.create_rectangle(0.0, 232.0, 349.0, 315.0, fill="#C74747", outline="")

        canvas_3.create_rectangle(
            434.0, 298.0, 872.0, 308.0, fill="#FFFFFF", outline=""
        )

        canvas_3.create_text(
            1505.7750244140625,
            791.70703125,
            anchor="nw",
            text="Date",
            fill="#FFFFFF",
            font=("RalewayRoman Bold", 40 * -1),
        )

        canvas_3.create_text(
            1015.0,
            303.0,
            anchor="nw",
            text="Reps",
            fill="#FFFFFF",
            font=("RalewayRoman Bold", 40 * -1),
        )

        canvas_3.create_rectangle(
            1063.8910675048828,
            690.326171875,
            1131.153564453125,
            818.92041015625,
            fill="#EE7D7D",
            outline="",
        )

        canvas_3.create_rectangle(
            1364.7393188476562,
            404.5859375,
            1448.221435546875,
            532.04638671875,
            fill="#EE7D7D",
            outline="",
        )

        canvas_3.create_rectangle(
            1132.4321594238281,
            650.64013671875,
            1268.2357177734375,
            687.38916015625,
            fill="#EE7D7D",
            outline="",
        )

        canvas_3.create_rectangle(
            1266.3749694824219,
            523.64453125,
            1369.7392578125,
            655.64013671875,
            fill="#EE7D7D",
            outline="",
        )

        canvas_3.create_rectangle(
            1048.949951171875,
            350.82861328125,
            1058.949951171875,
            829.12548828125,
            fill="#FFFFFF",
            outline="",
        )

        canvas_3.create_rectangle(
            1048.949951171875,
            819.12548828125,
            1491.1249389648438,
            829.12548828125,
            fill="#FFFFFF",
            outline="",
        )

        canvas_3.create_text(
            32.0,
            40.0,
            anchor="nw",
            text="Pushup \nProgressor",
            fill="#FFFFFF",
            font=("RalewayRoman Bold", 55 * -1),
        )

        canvas_3.create_rectangle(
            -4.99981689453125,
            193.978515625,
            349.0,
            205.021484375,
            fill="#FFFFFF",
            outline="",
        )

        self.pages.append(canvas_3)

        # Load page 4
        canvas_4 = Canvas(
            self.window,
            bg=PAGE_BACKGROUND_COLORS[3],
            height=1050 - NAVIGATION_BAR_HEIGHT,
            width=1680,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        canvas_4.place(x=0, y=NAVIGATION_BAR_HEIGHT)

        canvas_4.create_text(
            799.0,
            72.0,
            anchor="nw",
            text="Progressions",
            fill="#FFFFFF",
            font=("RalewayRoman Bold", 70 * -1),
        )

        presshome_button = Button(
            text="Home",
            font=("RalewayRoman Bold", 50),
            fg="#FFFFFF",
            highlightbackground="#D9D9D9",
            command=self.show_home_page,
        )
        presshome_button.place(x=80, y=260)

        pressworkout_button = Button(
            text="Workout",
            font=("RalewayRoman Bold", 50),
            fg="#FFFFFF",
            highlightbackground="#D9D9D9",
            command=self.show_workout_page,
        )
        pressworkout_button.place(x=60, y=340)

        pressstats_button = Button(
            text="Statistics",
            font=("RalewayRoman Bold", 50),
            fg="#FFFFFF",
            highlightbackground="#D9D9D9",
            command=self.show_workout_page,
        )
        pressstats_button.place(x=55, y=420)

        presslog_button = Button(
            text="Progressions",
            font=("RalewayRoman Bold", 50),
            fg="#FFFFFF",
            highlightbackground="#D9D9D9",
            command=self.show_progressions_page,
        )
        presslog_button.place(x=10, y=500)

        canvas_4.create_rectangle(
            557.7156372070312,
            311.48583984375,
            1464.4219360351562,
            779.228515625,
            fill="#000000",
            outline="",
        )

        canvas_4.create_rectangle(
            546.0, 311.0, 556.9089050292969, 780.0, fill="#FFFFFF", outline=""
        )

        canvas_4.create_rectangle(
            1453.401123046875,
            311.0,
            1464.4208374023438,
            780.0,
            fill="#FFFFFF",
            outline="",
        )

        canvas_4.create_rectangle(
            546.8578491210938, 768.625, 1473.0, 778.625, fill="#FFFFFF", outline=""
        )

        canvas_4.create_rectangle(
            547.8775634765625, 311.0, 1464.4208984375, 321.0, fill="#FFFFFF", outline=""
        )

        canvas_4.create_rectangle(
            1238.0, 199.0, 1553.0, 274.0, fill="#938383", outline=""
        )

        canvas_4.create_rectangle(
            477.0, 202.0, 792.0, 277.0, fill="#938383", outline=""
        )

        canvas_4.create_rectangle(
            862.0, 202.0, 1177.0, 277.0, fill="#EE7D7D", outline=""
        )

        canvas_4.create_text(
            979.0,
            213.0,
            anchor="nw",
            text="Pike",
            fill="#FFFFFF",
            font=("RalewayRoman Bold", 40 * -1),
        )

        canvas_4.create_text(
            1291.0,
            213.0,
            anchor="nw",
            text="Handstand",
            fill="#FFFFFF",
            font=("RalewayRoman Bold", 40 * -1),
        )

        canvas_4.create_text(
            556.0,
            213.0,
            anchor="nw",
            text="Diamond",
            fill="#FFFFFF",
            font=("RalewayRoman Bold", 40 * -1),
        )

        canvas_4.create_rectangle(0.0, 0.0, 349.0, 1050.0, fill="#EE7C7C", outline="")

        canvas_4.create_rectangle(
            0.0, 494.0, 349.0, 584.78125, fill="#C74747", outline=""
        )

        canvas_4.create_text(
            32.0,
            40.0,
            anchor="nw",
            text="Pushup \nProgressor",
            fill="#FFFFFF",
            font=("RalewayRoman Bold", 55 * -1),
        )

        canvas_4.create_rectangle(
            -4.99981689453125,
            193.978515625,
            349.0,
            205.021484375,
            fill="#FFFFFF",
            outline="",
        )

        self.pages.append(canvas_4)

    def show_page(self, page_index):
        if 0 <= page_index < len(self.pages):
            if self.current_page != page_index:
                self.pages[self.current_page].place_forget()
                self.current_page = page_index
                self.pages[self.current_page].place(x=0, y=NAVIGATION_BAR_HEIGHT)

    def show_home_page(self):
        self.show_page(0)

    def show_workout_page(self):
        self.show_page(1)

    def show_statistics_page(self):
        self.show_page(2)

    def show_progressions_page(self):
        self.show_page(3)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = MultipageApplication()
    app.run()
