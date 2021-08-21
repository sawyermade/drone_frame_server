import os, sys, requests, numpy as np, cv2, jsonpickle

def main():
	# Args

	# Camera capture
	cap = cv2.VideoCapture(0)

	# Infinite loop
	while True:
		# Read frame from cam
		ret, frame = cap.read()

		# Display
		cv2.imshow('Video', frame)
		k = cv2.waitKey(1)



if __name__ == '__main__':
	main()