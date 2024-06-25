import pyttsx3 as pyt

a = 1
option=int(input("enter number:"))

txt_speech = pyt.init()
if(option==a):
           answer = input("want to convert to speech??")
           txt_speech.say(answer)
else:
    with open('demo.txt','r') as file :
         lines= file.read().replace("\n","")
         txt_speech.say(lines)

txt_speech.setProperty('rate', 190)
txt_speech.setProperty('volume', 100)
txt_speech.runAndWait()
