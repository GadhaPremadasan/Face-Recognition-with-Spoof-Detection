# Face-Recognition-with-Spoof-Detection
This repository contains code for a simple face recognition and attendance system using OpenCV and face_recognition libraries. This system captures images from a webcam, performs face recognition, and keeps track of attendance in a CSV file.

# Prerequisites
Before running the code, make sure you have the following dependencies installed:

1. Python 3.x
2. OpenCV (pip install opencv-python)
3. face_recognition (pip install face-recognition)
4. NumPy (pip install numpy)

# Usage
1. Clone this repository to your local machine.
2. Open the pickle.py file in your text editor and make the following changes as needed:

 - Update the path variable to the folder containing the images of people for whom you want to create facial encodings. Replace '/path to folder with images' with the actual path to your image folder.

- Replace '/encodings pickle file name ' with the desired name for your pickle file. Make sure to keep the .pkl extension.

- Run the pickle.py script.
3. Open the attendance.py file in your text editor and make the following changes as needed:

 - Update the path variable to the folder containing the images of people you want to recognize. Replace '/path to the folder with faces' with the actual path to your image folder.

- Update the model_dir in the test function call with the path to your anti-spoofing model.

- Replace 'name of your pickle file' with the actual name of your pickle file containing face encodings. Make sure this file is in the same directory as attendance.py or provide the full path.

4. Run the attendance.py script.

5. The webcam feed will open, and the system will perform face recognition. Detected faces will be labeled with the corresponding person's name, and attendance will be marked in a CSV file.

6. To exit the program, press 'q' in the webcam feed window.

# Attendance Tracking
The attendance data is stored in a CSV file with a filename in the format attendance_YYYY-MM-DD.csv, where YYYY-MM-DD represents the current date when the attendance was recorded.

# Notes
- Make sure your webcam is connected and working properly.

- Ensure that the necessary Python packages are installed.

- You may need to fine-tune the face recognition parameters (e.g., tolerance) for optimal results, depending on your dataset.

# Acknowledgement
This project is built upon the foundation laid by the [Silent Face Anti-Spoofing](https://github.com/minivision-ai/Silent-Face-Anti-Spoofing) repository by MiniVision AI. I extend our gratitude to their team for their valuable work.


