import face_recognition
import os
import numpy as np

list = os.listdir("Guests/")
file_count = len(list)

for i in range(1, file_count + 1):
	file_directory = "Guests/" + str(i) + "/photo.jpg"
	face_image = face_recognition.load_image_file(file_directory)
	face_encoding = face_recognition.face_encodings(face_image)[0]

	np.save("Guests/" + str(i) + "/encoding.npy", face_encoding)