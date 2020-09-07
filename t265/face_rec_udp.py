from __future__ import division
from imutils.video import FPS
import face_recognition
import cv2
import numpy as np
import socket
import struct

BASE_DIR = "C:/dev/Mafat/t265"
IMAGE_SHRINK_RATIO = 0.5 #how much to shrink the image frame, the more we shrink the more FPS we can process BUT the face must be closer to the camera!

MAX_DGRAM = 2**16
SERVER_PORT = 12345

def dump_buffer(s):
    """ Emptying buffer frame """
    while True:
        seg, addr = s.recvfrom(MAX_DGRAM)
        print(seg[0])
        if struct.unpack("B", seg[0:1])[0] == 1:
            print("finish emptying buffer")
            break


""" Getting image udp frame &
concate before decode and output image """

# Set up socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', SERVER_PORT))
dat = b''
dump_buffer(s)
fps = FPS().start()


# Load a wanted picture and learn how to recognize it. You can load more wanted pictures as needed
wanted_image = face_recognition.load_image_file(BASE_DIR +"/wanted.jpg")
wanted_face_encoding = face_recognition.face_encodings(wanted_image)[0]

# wanted_mask_image = face_recognition.load_image_file(BASE_DIR +"/wanted_mask.jpg")
# wanted_mask_face_encoding = face_recognition.face_encodings(wanted_mask_image)[0]
# Create arrays of known face encodings and their names
known_face_encodings = [
    wanted_face_encoding
    # ,wanted_mask_face_encoding
]
known_face_names = [
    "Wanted"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True


while True:
    seg, addr = s.recvfrom(MAX_DGRAM)
    if struct.unpack("B", seg[0:1])[0] > 1:
        dat += seg[1:]
        continue

    dat += seg[1:]
    frame = cv2.imdecode(np.fromstring(dat, dtype=np.uint8), 1)
    dat = b''
    #print(np.size(frame, 0),np.size(frame, 1)) # prints image resultion
    #quit()
    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=IMAGE_SHRINK_RATIO, fy=IMAGE_SHRINK_RATIO)
    #print(small_frame)
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]
    
    # Only process every other frame of video to save time
    if process_this_frame:
        fps.update()
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame, model="cnn") # model="cnn" or model="hog" (faster but less accurate)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= int(1/IMAGE_SHRINK_RATIO)
        right *= int(1/IMAGE_SHRINK_RATIO)
        bottom *= int(1/IMAGE_SHRINK_RATIO)
        left *= int(1/IMAGE_SHRINK_RATIO)

        if (name=="Wanted"):
            color = (0, 0, 255)
        else:
            color = (0, 255, 0)
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), color, cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# cap.release()
cv2.destroyAllWindows()
s.close()

# Release handle to the webcam
fps.stop()
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
