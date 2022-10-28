# our main file.

import speech_recognition as sr

# criar um reconhecedor
r = sr.recognizer()

# abrir o microfone para captura
with  sr.microfone() as source:
 while True:
    áudio = r.listen(source) # define microfone como fonte de áudio

    print(r.recognize_google(áudio, language='pt'))