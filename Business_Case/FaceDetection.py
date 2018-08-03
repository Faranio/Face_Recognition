import face_recognition
import cv2
import pytz
import datetime
from FaceRecognition import FaceRecognition

class FaceDetection():

	def faceRecognition(frame, locations, date):
		FaceRecognition.runFaceRecognition(frame, locations, date)

	def runFaceDetection(self):
		self.video_capture = cv2.VideoCapture(0)
		self.video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
		self.video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
		n = 0

		face_locations = []
		print("Running Face Detection...")

		while True:
			ret, frame = self.video_capture.read()
			small_frame = cv2.resize(frame, (0, 0), fx = 0.25, fy = 0.25)
			if n % 40 == 0:
				rgb_small_frame = small_frame[:, :, ::-1]
				face_locations = face_recognition.face_locations(rgb_small_frame)
				then = datetime.datetime.now(pytz.utc)
				FaceDetection.faceRecognition(rgb_small_frame, face_locations, then)

			n += 1

			cv2.imshow('Video', frame)

			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

		self.video_capture.release()
		cv2.destroyAllWindows()