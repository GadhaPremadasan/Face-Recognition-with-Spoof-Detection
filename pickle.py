import os
import cv2 as cv
import face_recognition as fr 
import pickle
from tqdm import tqdm

path = '/home/gadha/Desktop/face_recog/facesss (copy)'
images = []
encodeList = []
names = []
myList = os.listdir(path)

for persons in sorted(os.listdir(path)):
    for image in sorted(os.listdir(os.path.join(path,persons))):
      
      image_path = os.path.join(path, persons, image)
      
      curImg = cv.imread(image_path)
      
      images.append(curImg)

def find_encodings(list_of_images):
    for img in tqdm(images):

      img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
      encode = fr.face_encodings(img,known_face_locations=None, num_jitters=100)[0]

      encodeList.append(encode)
    return encodeList


# encode list for known faces, the find_encodings function is called here
encodeListKnown = find_encodings(images)

print('Encoding completed!')
with open('/encodings pickle file name in .pkl format', 'wb') as f:
    pickle.dump(encodeListKnown, f)
    print("pickled!")
