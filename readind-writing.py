import cv2
import os

# #readinf an image

# image_path = os.path.join(os.getcwd(), 'schoolBus.png')
# img = cv2.imread(image_path)

# #write image
# cv2.imwrite(os.path.join(os.getcwd(), 'schoolBus_out.png'),img)

# #to visualize
# cv2.imshow('image',img)
# cv2.waitKey(0)

# video_path = os.path.join('.','video2467529850.mp4')
# video = cv2.VideoCapture(video_path)

# ret = True

# while ret:
#     ret, frame = video.read()

#     if ret:
#         cv2.imshow('frame',frame)
#         cv2.waitKey(40)

# video.release()
# cv2.destroyAllWindows()

webcam = cv2.VideoCapture(0)

while True:
    ret, frame = webcam.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()