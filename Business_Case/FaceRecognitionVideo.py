import face_recognition
import os
import numpy as np

class FaceRecognitionVideo():

	def runFaceRecognition(frame, face_locations, frame_number, total_frame_number, duration):
		list = os.listdir("Guests/")
		file_count = len(list)

		video_time = frame_number * duration / total_frame_number
		video_time = round(video_time, 4)

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

		for i in found_names:
			readFile = open("Guests/" + str(i) + "/info.txt", "r")
			info = readFile.readlines()

			infoFile = open("videoCriminal.txt", "a")
			infoFile.write(info[0] + info[1] + info[2] + "Time in video (in seconds): " + str(video_time) + "\n\n")

			readFile.close()
			infoFile.close()

		print(face_names)