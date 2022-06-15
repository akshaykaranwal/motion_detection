import cv2
import glob
images = glob.glob('*.jpg')
for image in images:
    img = cv2.imread(image,0)
    resized = cv2.resize(img,(100,100))
    cv2.imshow("img1",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("img1_"+image,resized)
