
import cv2 as cv
import face_recognition as fr
import numpy as np
import os
import pickle
from datetime import datetime
import csv
from test import test

path = '/path to the folder with faces '
names = []
myList = os.listdir(path)
images = []
fr_counter = 0
cap = cv.VideoCapture(0)

for persons in sorted(os.listdir(path)):
    for image in sorted(os.listdir(os.path.join(path, persons))):
        names.append(os.path.splitext(image)[0])

def create_new_attendance_file(attendance_file):
    with open(attendance_file, 'w', newline='') as f:
        fieldnames = ['Name', 'Check-in', 'Check-out']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

def mark_attendance(name_from_face_recognition, attendance_file):
    now = datetime.now().strftime('%H:%M:%S')
    checkout_time = now
    records = []
    if os.path.exists(attendance_file):
        with open(attendance_file, 'r') as f:
            reader = csv.DictReader(f)
            records = list(reader)

    for record in records:
        if record['Name'] == name_from_face_recognition:
            record['Check-out'] = checkout_time
            break
    else:
        records.append({
            'Name': name_from_face_recognition,
            'Check-in': now,
            'Check-out': None
        })

    with open(attendance_file, 'w', newline='') as f:
        fieldnames = ['Name', 'Check-in', 'Check-out']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

while True :
    
        ret, img = cap.read()
        label = test(
            image=img,
            model_dir='/home/gadha/Desktop/face_recog/resources/anti_spoof_models',
            device_id=1
        )
        if label == 1:
            imgS = cv.resize(img, (0, 0), None, 0.5, 0.5)
            imgS = cv.cvtColor(imgS, cv.COLOR_BGR2RGB)
            face_cur_frame = fr.face_locations(imgS)
            encodes_cur_frame = fr.face_encodings(imgS, face_cur_frame)

            for encodeFace, faceLoc in zip(encodes_cur_frame, face_cur_frame):
                with open('name of your pickle file', 'rb') as f:
                    encodeListKnown = pickle.load(f)
                matches = fr.compare_faces(encodeListKnown, encodeFace, tolerance=0.42)
                faceDis = fr.face_distance(encodeListKnown, encodeFace)
                
                if matches[np.argmin(faceDis)]:
                    best_match_index = np.argmin(faceDis)
                    name_from_face_recognition = names[best_match_index]
                    print(name_from_face_recognition)
                    y1,x2,y2,x1 = faceLoc
                    y1,x2,y2,x1 = y1*2,x2*2,y2*2,x1*2
                    cv.rectangle(img,(x1,y1),(x2,y2),(0,255,0),1)
                    cv.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0))
                    cv.putText(img,name_from_face_recognition,(x1-6,y2-6),cv.FONT_HERSHEY_COMPLEX,1,(255,255,255),)
                    attendance_file = f'attendance_{datetime.now().strftime("%Y-%m-%d")}.csv'
                    if not os.path.exists(attendance_file):
                        create_new_attendance_file(attendance_file)

                    mark_attendance(name_from_face_recognition, attendance_file)
        else:
            print("spoof detected!")    
            

        cv.imshow('webcam', img)
        if cv.waitKey(1) & 0xFF == ord("q"):
         break
    
cap.release()
cv.destroyAllWindows()
