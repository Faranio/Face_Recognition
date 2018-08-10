import face_recognition
import cv2
from FaceRecognitionVideo import FaceRecognitionVideo
from moviepy.editor import VideoFileClip
import time


class FaceDetectionVideo():

    def faceRecognition(frame, locations, frame_number, total_frame_number, duration):
        FaceRecognitionVideo.runFaceRecognition(frame, locations, frame_number, total_frame_number, duration)

    def runFaceDetection():
        start_time = time.time()
        cap = cv2.VideoCapture('1.mp4')
        n = 0
        length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        clip = VideoFileClip("1.mp4")

        face_locations = []
        print("Running Face Detection...")

        while (cap.isOpened()):

            ret, frame = cap.read()
            if ret == False:
                break
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            line_frame = small_frame[0:200, :]
            if n % 40 == 0:
                rgb_small_frame = line_frame[:, :, ::-1]
                face_locations = face_recognition.face_locations(rgb_small_frame)
                FaceDetectionVideo.faceRecognition(rgb_small_frame, face_locations, n, length, clip.duration)

            n += 1
            for (top, right, bottom, left) in face_locations:
                cv2.rectangle(line_frame, (left, top), (right, bottom), (0, 255, 0), 2)

            cv2.imshow('Video', line_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        print("\nTotal Frame Number: " + str(length))
        print("Total Video Duration (in seconds): " + str(clip.duration))
        print("Program execution time (in seconds): " + str(round(time.time() - start_time, 2)))

        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    FaceDetectionVideo.runFaceDetection()
