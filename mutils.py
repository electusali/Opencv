# import the necessary packages
import cv2
import imutils

# load the tic-tac-toe image and convert it to grayscale
image = cv2.imread("tictactoe.png",3)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret,thr=cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
img=image.copy()
# find all contours on the tic-tac-toe board
cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# loop over the contours
#for (i, c) in enumerate(cnts):
	# compute the area of the contour along with the bounding box
	# to compute the aspect ratio
#	area = cv2.contourArea(c)
#	(x, y, w, h) = cv2.boundingRect(c)

	# compute the convex hull of the contour, then use the area of the
	# original contour and the area of the convex hull to compute the
	# solidity
#	hull = cv2.convexHull(c)
#	hullArea = cv2.contourArea(hull)
#	solidity = area / float(hullArea)

cv2.imshow('org',image)
cv2.waitKey(0)
cv2.destroyAllWindows()