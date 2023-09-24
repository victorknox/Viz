import cv2 as cv
import datetime
import time
import baseline_pic2text
import tts
import blip
import speech2text

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

    #question = input("enter prompt:")
    question = speech2text.listen_for_text()
    while not question:
        question = speech2text.listen_for_text()
        
    print(question)
    
    text2read = blip.talk_to_img(image, question=question)
    if text2read.replace("\n","").replace(" ","") == "":
        text2read = "I'm sorry, I didn't understand the question."
        
    print(text2read)
    print("\n"*10)
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
