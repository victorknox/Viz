import speech_recognition as sr


def listen_for_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #recognizer.adjust_for_ambient_noise(source, duration=1)
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)

            return query

        except sr.UnknownValueError:
            return None

