from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.uic import loadUi
import numpy as np
import cv2
import imutils
import datetime
from detection_window import DetectionWindow
import time
# Manages the settings window
class SettingsWindow(QMainWindow):
	def __init__(self):
		super(SettingsWindow, self).__init__()
		loadUi('Client\\UI\\settings_window.ui', self)

		self.detection_window = DetectionWindow()
		
		self.pushButton.clicked.connect(self.startCamera)

	def displayInfo(self):
		self.show()

	# Get input and go to detection window


	def startCamera(self):
		gun_cascade = cv2.CascadeClassifier('Client\\cascade.xml')
		camera = cv2.VideoCapture(0)

		firstFrame = None
		gun_exist = None

		starting_time = time.time()
		while True:
			ret, frame = camera.read()

			frame = imutils.resize(frame, width=500)
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

			gun = gun_cascade.detectMultiScale(gray,
											1.3, 5,
											minSize=(100, 100))
			if len(gun) > 0:
				gun_exists = True
				print("Gun Detected ")
				self.save_detection(frame)
			else:
				print("Gun not detected")
			for (x, y, w, h) in gun:
				frame = cv2.rectangle(frame,
									(x, y),
									(x + w, y + h),
									(255, 0, 0), 2)
				roi_gray = gray[y : y + h, x : x + w]
				roi_color = frame[y : y + h, x : x + w]
				elapsed_time = time.time() - starting_time
				if elapsed_time >= 10:
						starting_time = time.time()
						self.save_detection(frame)
			if firstFrame is None:
				firstFrame = gray
				continue
			cv2.imshow("Security Feed", frame)
			key = cv2.waitKey(1) & 0xFF

			if key == ord('q'):
				break
	
		if gun_exists:
			print("guns detected")
		else:
			print("guns not detected")
		camera.release()
		cv2.destroyAllWindows()
	def save_detection(self, frame):
		cv2.imwrite("Client\\saved_frame\\frame.jpg", frame)
		print('Frame Saved')