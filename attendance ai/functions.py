## ================= FUNCTIONS.PY =================

import tkinter as tk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd

import cv2
import os
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time

# GUI VARIABLES
window = None
clock = None
message = None
message1 = None
tv = None

txt = None
txt2 = None

course_var = None
year_var = None

# ================= PATH =================

def assure_path_exists(path):

    dir = os.path.dirname(path)

    if not os.path.exists(dir):
        os.makedirs(dir)

# ================= CLOCK =================

def tick():

    time_string = time.strftime('%H:%M:%S')

    clock.config(text=time_string)

    clock.after(200, tick)

# ================= CONTACT =================

def contact():

    mess._show(
        title='Contact us',
        message="Please contact us on : 'mohdzaman9899@gmail.com'"
    )

# ================= CHECK XML =================

def check_haarcascadefile():

    exists = os.path.isfile(
        "haarcascade_frontalface_default.xml"
    )

    if not exists:

        mess._show(
            title='File Missing',
            message='haarcascade_frontalface_default.xml missing'
        )

        window.destroy()

# ================= PASSWORD =================

def save_pass():

    assure_path_exists("TrainingImageLabel/")

    exists1 = os.path.isfile(
        "TrainingImageLabel/psd.txt"
    )

    if exists1:

        tf = open(
            "TrainingImageLabel/psd.txt",
            "r"
        )

        key = tf.read()

    else:

        master.destroy()

        new_pas = tsd.askstring(
            'Old Password not found',
            'Please enter a new password below',
            show='*'
        )

        if new_pas is None:

            mess._show(
                title='No Password Entered',
                message='Password not set'
            )

        else:

            tf = open(
                "TrainingImageLabel/psd.txt",
                "w"
            )

            tf.write(new_pas)

            mess._show(
                title='Password Registered',
                message='New password registered'
            )

            return

    op = old.get()
    newp = new.get()
    nnewp = nnew.get()

    if op == key:

        if newp == nnewp:

            txf = open(
                "TrainingImageLabel/psd.txt",
                "w"
            )

            txf.write(newp)

        else:

            mess._show(
                title='Error',
                message='Confirm new password again'
            )

            return

    else:

        mess._show(
            title='Wrong Password',
            message='Please enter correct old password'
        )

        return

    mess._show(
        title='Password Changed',
        message='Password changed successfully'
    )

    master.destroy()

# ================= CHANGE PASSWORD =================

def change_pass():

    global master
    global old
    global new
    global nnew

    master = tk.Tk()

    master.geometry("400x160")

    master.resizable(False, False)

    master.title("Change Password")

    master.configure(background="white")

    lbl4 = tk.Label(
        master,
        text='Enter Old Password',
        bg='white',
        font=('comic', 12, 'bold')
    )

    lbl4.place(x=10, y=10)

    old = tk.Entry(
        master,
        width=25,
        fg="black",
        relief='solid',
        font=('comic', 12, 'bold'),
        show='*'
    )

    old.place(x=180, y=10)

    lbl5 = tk.Label(
        master,
        text='Enter New Password',
        bg='white',
        font=('comic', 12, 'bold')
    )

    lbl5.place(x=10, y=45)

    new = tk.Entry(
        master,
        width=25,
        fg="black",
        relief='solid',
        font=('comic', 12, 'bold'),
        show='*'
    )

    new.place(x=180, y=45)

    lbl6 = tk.Label(
        master,
        text='Confirm New Password',
        bg='white',
        font=('comic', 12, 'bold')
    )

    lbl6.place(x=10, y=80)

    nnew = tk.Entry(
        master,
        width=25,
        fg="black",
        relief='solid',
        font=('comic', 12, 'bold'),
        show='*'
    )

    nnew.place(x=180, y=80)

    cancel = tk.Button(
        master,
        text="Cancel",
        command=master.destroy,
        fg="black",
        bg="red",
        height=1,
        width=25
    )

    cancel.place(x=200, y=120)

    save1 = tk.Button(
        master,
        text="Save",
        command=save_pass,
        fg="black",
        bg="#00fcca",
        height=1,
        width=25
    )

    save1.place(x=10, y=120)

    master.mainloop()

# ================= PASSWORD CHECK =================

def psw():

    assure_path_exists("TrainingImageLabel/")

    exists1 = os.path.isfile(
        "TrainingImageLabel/psd.txt"
    )

    if exists1:

        tf = open(
            "TrainingImageLabel/psd.txt",
            "r"
        )

        key = tf.read()

    else:

        new_pas = tsd.askstring(
            'Old Password not found',
            'Please enter a new password below',
            show='*'
        )

        if new_pas is None:

            mess._show(
                title='No Password Entered',
                message='Password not set'
            )

        else:

            tf = open(
                "TrainingImageLabel/psd.txt",
                "w"
            )

            tf.write(new_pas)

            mess._show(
                title='Password Registered',
                message='New password registered'
            )

            return

    password = tsd.askstring(
        'Password',
        'Enter Password',
        show='*'
    )

    if password == key:

        TrainImages()

    elif password is None:

        pass

    else:

        mess._show(
            title='Wrong Password',
            message='Wrong password entered'
        )


# ================= TAKE IMAGES =================

def TakeImages():

    check_haarcascadefile()

    assure_path_exists("StudentDetails/")
    assure_path_exists("TrainingImage/")

    file_path = "StudentDetails/StudentDetails.csv"

    # ================= CREATE FILE IF NOT EXISTS =================

    if not os.path.exists(file_path):

        with open(file_path, "w", newline="") as f:

            writer = csv.writer(f)

            writer.writerow([
                "SERIAL NO.",
                "ID",
                "NAME",
                "COURSE",
                "YEAR"
            ])

        serial = 1

    else:

        with open(file_path, "r") as f:

            rows = list(csv.reader(f))

            serial = len(rows)

    # ================= GET INPUT =================

    Id = txt.get().strip()
    name = txt2.get().strip()
    course = course_var.get()
    year = year_var.get()

    # ================= VALIDATION =================

    if Id == "" or name == "":

        mess._show(
            title='Missing Details',
            message='Please fill all details'
        )
        return

    if not (name.replace(" ", "").isalpha()):

        message.configure(text="Enter Correct Name")
        return

    # ================= CAMERA =================

    cam = cv2.VideoCapture(0)

    detector = cv2.CascadeClassifier(
        "haarcascade_frontalface_default.xml"
    )

    sampleNum = 0

    while True:

        ret, img = cam.read()

        if not ret:
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:

            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

            sampleNum += 1

            cv2.imwrite(
                "TrainingImage/" +
                name + "." +
                str(serial) + "." +
                str(Id) + "." +
                str(sampleNum) + ".jpg",
                gray[y:y+h, x:x+w]
            )

            cv2.imshow("Taking Images", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        elif sampleNum >= 100:
            break

    cam.release()
    cv2.destroyAllWindows()

    # ================= SAVE STUDENT DATA =================

    row = [
        serial,
        Id,
        name,
        course,
        year
    ]

    with open(file_path, "a", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)
        writer.writerow(row)

    # ================= UI UPDATE =================

    message1.configure(text="Images Taken Successfully")
    message.configure(text=f"Student Saved: {name}")

    mess._show(
        title='Success',
        message='Student Data Saved Successfully'
    )
# ================= TRAIN IMAGES =================

def TrainImages():

    check_haarcascadefile()

    assure_path_exists(
        "TrainingImageLabel/"
    )

    try:

        recognizer = cv2.face.LBPHFaceRecognizer_create()

    except:

        mess._show(
            title='OpenCV Error',
            message='Install opencv-contrib-python'
        )

        return

    faces, IDs = getImagesAndLabels(
        "TrainingImage"
    )

    if len(faces) == 0:

        mess._show(
            title='No Images',
            message='Please capture images first'
        )

        return

    recognizer.train(
        faces,
        np.array(IDs)
    )

    recognizer.save(
        "TrainingImageLabel/Trainner.yml"
    )

    message1.configure(
        text="Profile Saved Successfully"
    )

    message.configure(
        text=f"Total Registrations : {len(set(IDs))}"
    )

    mess._show(
        title='Success',
        message='Model Trained Successfully'
    )


# ================= GET IMAGES =================

def getImagesAndLabels(path):

    imagePaths = [
        os.path.join(path, f)
        for f in os.listdir(path)
    ]

    faces = []

    Ids = []

    for imagePath in imagePaths:

        try:

            pilImage = Image.open(
                imagePath
            ).convert('L')

            imageNp = np.array(
                pilImage,
                'uint8'
            )

            ID = int(
                os.path.split(imagePath)[-1].split(".")[1]
            )

            faces.append(imageNp)

            Ids.append(ID)

        except:
            pass

    return faces, Ids
def TrackImages():

    check_haarcascadefile()

    assure_path_exists("Attendance/")
    assure_path_exists("StudentDetails/")

    # CLEAR TABLE
    for k in tv.get_children():
        tv.delete(k)

    try:

        recognizer = cv2.face.LBPHFaceRecognizer_create()

    except:

        mess._show(
            title='OpenCV Error',
            message='Install opencv-contrib-python'
        )

        return

    model_path = "TrainingImageLabel/Trainner.yml"

    if not os.path.isfile(model_path):

        mess._show(
            title='Data Missing',
            message='Please train model first'
        )

        return

    recognizer.read(model_path)

    faceCascade = cv2.CascadeClassifier(
        "haarcascade_frontalface_default.xml"
    )

    cam = cv2.VideoCapture(0)

    font = cv2.FONT_HERSHEY_SIMPLEX

    student_file = "StudentDetails/StudentDetails.csv"

    if not os.path.isfile(student_file):

        mess._show(
            title='Details Missing',
            message='StudentDetails.csv missing'
        )

        return

    df = pd.read_csv(student_file)

    # DATE
    ts = time.time()

    date = datetime.datetime.fromtimestamp(
        ts
    ).strftime('%d-%m-%Y')

    attendance_file = (
        "Attendance/Attendance_" +
        date +
        ".csv"
    )

    # ================= CREATE FILE =================

    if not os.path.isfile(attendance_file):

        with open(
            attendance_file,
            'w',
            newline=''
        ) as f:

            writer = csv.writer(f)

            writer.writerow([
                'Id',
                'Name',
                'Course',
                'Year',
                'Date',
                'Time'
            ])

    # ================= LOAD OLD ATTENDANCE =================

    marked_ids = set()

    with open(
        attendance_file,
        'r'
    ) as csvFile1:

        reader = csv.reader(csvFile1)

        next(reader, None)

        for row in reader:

            if len(row) >= 6:

                # STORE IDS
                marked_ids.add(str(row[0]))

                # SHOW IN TABLE
                tv.insert(
                    '',
                    0,
                    text=row[0],
                    values=(
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5]
                    )
                )

    # ================= CAMERA LOOP =================

    while True:

        ret, im = cam.read()

        if not ret:

            print("❌ Camera Error")

            break

        gray = cv2.cvtColor(
            im,
            cv2.COLOR_BGR2GRAY
        )

        faces = faceCascade.detectMultiScale(
            gray,
            1.2,
            5
        )

        for (x, y, w, h) in faces:

            # BLUE BOX
            cv2.rectangle(
                im,
                (x, y),
                (x+w, y+h),
                (255, 0, 0),
                2
            )

            serial, conf = recognizer.predict(
                gray[y:y+h, x:x+w]
            )

            if conf < 50:

                row = df.loc[
                    df['SERIAL NO.'] == serial
                ]

                if len(row) > 0:

                    student_id = str(
                        row['ID'].values[0]
                    )

                    name = str(
                        row['NAME'].values[0]
                    )

                    course = str(
                        row['COURSE'].values[0]
                    )

                    year = str(
                        row['YEAR'].values[0]
                    )

                    # SHOW NAME
                    cv2.putText(
                        im,
                        name,
                        (x, y+h),
                        font,
                        1,
                        (255,255,255),
                        2
                    )

                    # SAVE ONLY IF NOT PRESENT
                    if student_id not in marked_ids:

                        marked_ids.add(student_id)

                        current_time = datetime.datetime.fromtimestamp(
                            time.time()
                        ).strftime('%H:%M:%S')

                        attendance = [
                            student_id,
                            name,
                            course,
                            year,
                            date,
                            current_time
                        ]

                        # SAVE CSV
                        with open(
                            attendance_file,
                            'a',
                            newline=''
                        ) as f:

                            writer = csv.writer(f)

                            writer.writerow(attendance)

                        # SHOW IN TABLE
                        tv.insert(
                            '',
                            0,
                            text=student_id,
                            values=(
                                name,
                                course,
                                year,
                                date,
                                current_time
                            )
                        )

            else:

                cv2.putText(
                    im,
                    "Unknown",
                    (x, y+h),
                    font,
                    1,
                    (0,0,255),
                    2
                )

        cv2.imshow(
            'Taking Attendance',
            im
        )

        # PRESS Q TO EXIT
        if cv2.waitKey(1) & 0xFF == ord('q'):

            break

    cam.release()

    cv2.destroyAllWindows()