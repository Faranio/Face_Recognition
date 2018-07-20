import face_recognition
import cv2
import time

class OneToOne():

	def runOneToOne(self, id):
		self.accepted = False
		self.n = 150
		self.video_capture = cv2.VideoCapture(0)
		id = str(id)

		file_directory = "C:/Users/Farkhad/Desktop/methodpro/Business_Case/Staff/" + id + "/photo.jpg";
		face_image = face_recognition.load_image_file(file_directory)
		face_encoding = face_recognition.face_encodings(face_image)[0]

		textfile = open("C:/Users/Farkhad/Desktop/methodpro/Business_Case/Staff/" + id + "/info.txt", "r")
		name = textfile.read()

		# Create arrays of known face encodings and their names
		known_face_encodings = [
		    face_encoding
		]
		known_face_names = [
		    name
		]

		# Initialize some variables
		face_locations = []
		face_encodings = []
		face_names = []
		process_this_frame = True
		print ("Checking...")
		while self.n > 0:
		    # Grab a single frame of video
		    ret, frame = self.video_capture.read()

		    # Resize frame of video to 1/4 size for faster face recognition processing
		    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

		    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
		    rgb_small_frame = small_frame[:, :, ::-1]

		    # Only process every other frame of video to save time
		    if process_this_frame:
		        # Find all the faces and face encodings in the current frame of video
		        face_locations = face_recognition.face_locations(rgb_small_frame)
		        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

		        face_names = []
		        for face_encoding in face_encodings:
		            # See if the face is a match for the known face(s)
		            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance = 0.43)
		            name = "Unknown"

		            # If a match was found in known_face_encodings, just use the first one.
		            if True in matches:
		                first_match_index = matches.index(True)
		                name = known_face_names[first_match_index]

		            face_names.append(name)

		    process_this_frame = not process_this_frame


		    # Display the results

		    for (top, right, bottom, left), name in zip(face_locations, face_names):

		        font = cv2.FONT_HERSHEY_DUPLEX
		        cv2.putText(frame, str(self.n), (0, 30), font, 1.0, (255, 255, 255), 1)

		        if name != "Unknown":

		        	status = open("C:/Users/Farkhad/Desktop/methodpro/Business_Case/Staff/" + id + "/status.txt", "w")
		        	status.write("Accept")
		        	status.close()

		        	infoFile = open("C:/Users/Farkhad/Desktop/methodpro/Business_Case/Staff/" + id + "/info.txt", "r")
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
		        	cv2.putText(frame, idNumber, (0, 415), font, 1.0, (255, 255, 255), 1)
		        	cv2.putText(frame, staffName, (0, 445), font, 1.0, (255, 255, 255), 1)
		        	cv2.putText(frame, staffSurname, (0, 475), font, 1.0, (255, 255, 255), 1)
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

		            cv2.putText(frame, "BOOOOOOOOOOM", (300, 300), font, 1.0, (255, 255, 255), 1)
		            status = open("C:/Users/Farkhad/Desktop/methodpro/Business_Case/Staff/" + id + "/status.txt", "w")
		            status.write("Reject")
		            status.close()
		            break;

		        else:

		            if self.accepted == True:
		                #self.n = 0
		                break;
		            self.n -= 1

		    # Display the resulting image
		    cv2.imshow('Video', frame)

		    # Hit 'q' on the keyboard to quit!
		    if cv2.waitKey(1) & 0xFF == ord('q'):
		        break

		self.video_capture.release()
		cv2.destroyAllWindows()