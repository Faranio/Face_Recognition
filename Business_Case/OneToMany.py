import face_recognition
import cv2
import time
import os

class OneToMany():

    def runOneToMany(self):
        self.accepted = False
        self.n = 200

        dir = "Guests/"
        list = os.listdir(dir) # dir is your directory path
        file_count = len(list)
        
        # Get a reference to webcam #0 (the default one)
        self.video_capture = cv2.VideoCapture(0)
        self.video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        self.video_capture.set(cv2.CAP_PROP_FPS, 30)
        
        known_face_encodings = []
        known_face_names = []

        for i in range(1, file_count + 1):

            file_directory = "Guests/" + str(i) + "/photo.jpg";
            face_image = face_recognition.load_image_file(file_directory)
            face_encoding = face_recognition.face_encodings(face_image)[0]
            
            known_face_encodings.append(face_encoding)
            known_face_names.append(str(i))

        # Initialize some variables
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True
        print("Checking...")
        while self.n>0:
            print (self.n)
            # Grab a single frame of video
       	    ret, frame = self.video_capture.read()

            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]
            face_locations = face_recognition.face_locations(rgb_small_frame)
            # Only process every other frame of video to save time
            if self.n%10==0:
            	face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            	face_names = []

                # Find all the faces and face encodings in the current frame of
            	for face_encoding in face_encodings:
                    
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance = 0.43)
                    name = "Unknown"

                    # If a match was found in known_face_encodings, just use the first one.
                    if True in matches:
                        first_match_index = matches.index(True)
                        name = known_face_names[first_match_index]

                    face_names.append(name)
            	#process_this_frame = not process_this_frame
            print (self.video_capture.get(cv2.CAP_PROP_FPS))
            # Display the results
                
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, str(self.n), (0, 30), font, 1.0, (255, 255, 255), 1)
                    
                if name != "Unknown":
                    
                    status = open("Guests/" + name + "/status.txt", "w")
                    status.write("Accept")
                    status.close()

                    infoFile = open("Guests/" + name + "/info.txt", "r")
                    info = infoFile.read()
                    idNumber = info.rsplit('\n', 2)[0]
                    staffName = info.rsplit('\n', 2)[1]
                    staffSurname = info.rsplit('\n', 2)[2]
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                    self.accepted = True
                    top *= 4
                    right *= 4
                    bottom *= 4
                    left *= 4

                    # Draw a box around the face
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

                    # Draw a label with a name below the face
                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame, "RECOGNIZED", (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
                    cv2.putText(frame, idNumber, (0, 650), font, 1.0, (255, 255, 255), 1)
                    cv2.putText(frame, staffName, (0, 680), font, 1.0, (255, 255, 255), 1)
                    cv2.putText(frame, staffSurname, (0, 710), font, 1.0, (255, 255, 255), 1)
                    infoFile.close()

                else:
                    
                    top *= 4
                    right *= 4
                    bottom *= 4
                    left *= 4

                    # Draw a box around the face
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                    # Draw a label with a name below the face
                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame, "NOT RECOGNIZED", (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
                    
            if self.n == 0 and self.accepted == False:
                cv2.putText(frame, "BOOOOOOOOOOM", (300, 310), font, 1.0, (255, 255, 255), 1)
                status = open("Guests/" + name + "/status.txt", "w")
                status.write("Reject")
                status.close()
                break;
            else:
                if self.accepted == True:
                    self.n = self.n
                    #break;
                self.n -= 1

            # Display the resulting image
            cv2.imshow('Video', frame)

            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release handle to the webcam
        self.video_capture.release()
        cv2.destroyAllWindows()
