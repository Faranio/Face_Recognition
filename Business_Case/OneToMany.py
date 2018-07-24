import face_recognition
import cv2
import os
import pytz
import datetime

class OneToMany():

	def runOneToMany(self):
		self.n = 200

		list = os.listdir("Guests/")
		file_count = len(list)

		self.video_capture = cv2.VideoCapture(0)
		self.video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
		self.video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

		known_face_encodings = []
		known_face_names = []

		for i in range(1, file_count + 1):
			file_directory = "Guests/" + str(i) + "/photo.jpg"
			face_image = face_recognition.load_image_file(file_directory)
			face_encoding = face_recognition.face_encodings(face_image)[0]

			known_face_encodings.append(face_encoding)
			known_face_names.append(str(i))

		face_locations = []
		face_encodings = []
		face_names = []
		found_names = []
		found_dates = []
		print("Checking...")

		while True:
			ret, frame = self.video_capture.read()
			small_frame = cv2.resize(frame, (0, 0), fx = 0.25, fy = 0.25)
			rgb_small_frame = small_frame[:, :, ::-1]
			face_locations = face_recognition.face_locations(rgb_small_frame)

			if self.n % 20 == 0:
				face_encodings = face_recognition.face_encodings(rgb_small_frame)

				face_names = []

				for face_encoding in face_encodings:
					matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance = 0.43)
					name = "Unknown"

					if True in matches:
						first_match_index = matches.index(True)
						name = known_face_names[first_match_index]

					face_names.append(name)

			for (top, right, bottom, left), name in zip(face_locations, face_names):
				font = cv2.FONT_HERSHEY_DUPLEX

				top *= 4
				right *= 4
				bottom *= 4
				left *= 4

				if name != "Unknown":
					self.found = False
					if len(found_names) == 0:
						self.then = datetime.datetime.now(pytz.utc)
						
						status = open("Guests/" + name + "/status.txt", "w")
						status.write("Accept")
						status.close()

						found_names.append(name)
						found_dates.append(self.then)
					else:
						for i in found_names:
							if i == name:
								self.found = True
								break
						
						if self.found == False:
							self.then = datetime.datetime.now(pytz.utc)
				
							status = open("Guests/" + name + "/status.txt", "w")
							status.write("Accept")
							status.close()

							found_names.append(name)
							found_dates.append(self.then)

					cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
					cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
					cv2.putText(frame, "RECOGNIZED", (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
				else:
					cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
					cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
					cv2.putText(frame, "NOT RECOGNIZED", (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

				self.n -= 1

			cv2.imshow('Video', frame)

			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

		for time, name in zip(found_dates, found_names):
			time = time.astimezone(pytz.timezone('Asia/Almaty'))
			time = str(time.strftime("%Y-%m-%d %H:%M:%S"))
			infoFile = open("Guests/" + name + "/info.txt", "a")
			infoFile.write("\nArrived Time: " + time)												#TODO: Add current time
			infoFile.close()

		print(found_dates)
		print(found_names)

		self.video_capture.release()
		cv2.destroyAllWindows()