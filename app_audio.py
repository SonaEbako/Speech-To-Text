import speech_recognition as sr

recognizer = sr.Recognizer()

''' Recording sound '''

with sr.AudioFile("./sample_audio/speech.wav") as source:
    recorded_audio = recognizer.listen(source)
    print("Done Recording")

''' Reorganizing Audio '''
try:
    print("Recognizing the text")
    text = recognizer.recognize_google(
            recorded_audio, 
            language="en-US"
        )
    print("Decoded Text : {}".format(text))

except Exception as ex:
    print(ex)