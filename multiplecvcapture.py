import cv2 as cv
import datetime
import time
import baseline_pic2text
import tts


# Initialize the camera
cam_port = 0
cam = cv.VideoCapture(cam_port)

showing_video = True
counter = 0

def take_photo(image):
    print (image)
    global counter
    timestamp = datetime.datetime.now().strftime("capture")
    filename = f"Viz_{timestamp}_" + str(counter) + ".png"
    cv.imwrite(filename, image)
    counter += 1
    text2read = baseline_pic2text.describe_img(image)
    tts.read_str(text2read) 
    


while True:
    result, image = cam.read()

    if result:
        
        cv.imshow("Viz", image)
        

    key = cv.waitKey(1)
    if key == 113:
        print(key)
        break
    elif key == 32:
        take_photo(image)

        time.sleep(1)

cam.release()
cv.destroyWindow("Viz")
