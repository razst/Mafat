import face_recognition
import cv2
import numpy as np
from imutils.video import FPS
import pyrealsense2 as rs

IMAGE_SHRINK_RATIO = 0.25 #how much to shrink the image frame, the more we shrink the more FPS we can process BUT the face must be closer to the camera!

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.


# Configure depth and color streams
pipeline = rs.pipeline()
config = rs.config()
#config.enable_stream(rs.stream.fisheye)

# Start streaming
pipeline.start(config)

fps = FPS().start()

# Load a sample picture and learn how to recognize it.
obama_image = face_recognition.load_image_file("raz1.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Load a second sample picture and learn how to recognize it.
biden_image = face_recognition.load_image_file("uk.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    obama_face_encoding,
    biden_face_encoding
]
known_face_names = [
    "Raz",
    "NA"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Wait for a coherent pair of frames: depth and color
    frames = pipeline.wait_for_frames()
    fish_eye_frame = frames.get_fisheye_frame()
    if not fish_eye_frame:
        continue

    # Convert images to numpy arrays
    grayFrame = np.asanyarray(fish_eye_frame.get_data())
    frame = cv2.cvtColor(grayFrame,cv2.COLOR_GRAY2RGB)
    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=IMAGE_SHRINK_RATIO, fy=IMAGE_SHRINK_RATIO)
    #print(small_frame[100,100]) # prints image resultion
    #print(small_frame)
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]   
    #print(rgb_small_frame[100,100]) # prints image resultion
    #quit()
    #print(np.size(rgb_small_frame, 0),np.size(rgb_small_frame, 1)) # prints image resultion
    #quit()

    # Only process every other frame of video to save time
    if process_this_frame:
        fps.update()
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame, model="cnn") # model="cnn" or model="hog" (faster but less accurate)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        # for face_location in face_locations:
        #     face_names.append("NA")
        
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "NA"

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
        # Scale back up face locations since the frame we detected in was scaled
        top *= int(1/IMAGE_SHRINK_RATIO)
        right *= int(1/IMAGE_SHRINK_RATIO)
        bottom *= int(1/IMAGE_SHRINK_RATIO)
        left *= int(1/IMAGE_SHRINK_RATIO)

        # Draw a box around the face
        cv2.rectangle(frame, (right, top), (left, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
fps.stop()
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
pipeline.stop()
cv2.destroyAllWindows()