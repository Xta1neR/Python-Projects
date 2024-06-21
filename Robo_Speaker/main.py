from gtts import gTTS
import os

language = 'en'

while True:
    myText = input("Enter text to convert to speech (or 'exit' to quit): ")
    
    if myText.lower() == 'exit':
        print("Exiting...")
        break
    
    myobj = gTTS(text=myText, lang=language, slow=False)
    myobj.save("output.mp3")
    
    print(f"Text '{myText}' converted to speech. Playing...")
    os.system("start output.mp3")
