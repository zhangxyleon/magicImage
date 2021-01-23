import cv2 as cv
import numpy as np

# read image and return
def readImage(filename):
    return cv.imread(filename)

def rgb_to_grey(img):
    rgb_weights = [0.2989, 0.5870, 0.1140]
    return np.dot(img[...,:3], rgb_weights)

def detectFace(img):
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(img, 1.05, 5)
    return faces

def drawRecOnface(img):
    faces = detectFace(img)
    for x, y, w, h in faces:
        img = cv.rectangle(img, (x, y), (x+w, y+h), (0, 255 ,0), 3)
    cv.imshow("Face", img) 
    cv.destroyAllWindows()
    return img
def replaceByFace(origin, replacement):

    #detect face
    faces1 = detectFace(origin)
    x1, y1, w1, h1 = faces1[0]

    faces2 = detectFace(replacement)
    x2, y2, w2, h2 = faces2[0]

    #cut off face2
    replacement =  replacement[y2:y2+h2, x2:x2+w2 ]

    #resize face2

    dim = (w1,h1)
    resized = cv.resize(replacement, dim, interpolation = cv.INTER_AREA)

    #replace
    origin[y1:y1+w1, x1:x1+h1] = resized

    return origin

def replace(origin, replacement):
        #detect face
    faces = detectFace(origin)
    x, y, w, h = faces[0]

    #resize replacement
    dim = (w,h)
    resized = cv.resize(replacement, dim, interpolation = cv.INTER_AREA)

    #replace
    origin[y:y+w, x:x+h] = resized

    return origin

def save(name, img):
    cv.imwrite(name, img)

# if __name__ == "__main__":
#     img1 = readImage('photo.jpg')
#     # # if img is None:
#     # #     print("Check file path") 
#     # # newimg = rgb_to_grey(img)
#     # # print(newimg.shape)
#     # # cv.imshow('Original image', img)
#     # # cv.imwrite('lena_opencv_red.jpg', newimg)
#     # # cv.waitKey(0)
#     # # cv.destroyAllWindows() 
#     # img2 = readImage('photo.jpg')
#     # replace(img, img2)
#     # replaceByFace(img, img2)
#     img2 = readImage('anna.jpg')
#     # faces = detectFace(img)
#     # for x, y, w, h in faces:
#     #     img = cv.rectangle(img, (x, y), (x+w, y+h), (0, 255 ,0), 3)
#     #img = replace(img2, img1)
#     img = replaceByFace(img2, img1)
#     cv.imshow("Face", img) 
#     cv.destroyAllWindows()


    