import face_recognition
import os
import pytz
import numpy as np

class FaceRecognition():

	def runFaceRecognition(frame, face_locations, date):
		list = os.listdir("Guests/")
		file_count = len(list)

		known_face_encodings = []
		known_face_names = []

		for i in range(1, file_count + 1):
			face_encoding = np.load("Guests/" + str(i) + "/encoding.npy")

			known_face_encodings.append(face_encoding)
			known_face_names.append(str(i))

		face_encodings = []
		face_names = []
		found_names = []
		print("Running Face Recognition...")

		face_encodings = face_recognition.face_encodings(frame, known_face_locations = face_locations)

		for face_encoding in face_encodings:
			matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance = 0.49)
			name = "Unknown"

			if True in matches:
				first_match_index = matches.index(True)
				name = known_face_names[first_match_index]

			face_names.append(name)

		for name in face_names:

			if name != "Unknown":

				found = False

				if len(found_names) == 0:
					found_names.append(name)
				else:
					for i in found_names:
						if i == name:
							found = True
							break
					
				if found == False:
					found_names.append(name)

				time = date.astimezone(pytz.timezone('Asia/Almaty'))
				time = str(time.strftime("%Y-%m-%d %H:%M:%S"))

		for i in found_names:
			readFile = open("Guests/" + str(i) + "/info.txt", "r")
			info = readFile.readlines()

			infoFile = open("webCriminal.txt", "a")
			infoFile.write(info[0] + info[1] + info[2] + "Found Time: " + time + "\n\n")

			readFile.close()
			infoFile.close()

		print(face_names)