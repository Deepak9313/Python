import pyttsx3 as pt
engine = pt.init()
""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)  
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
while True:
    inp = input("Enter the sentence to speak : \n")
    if inp == 'q':
        break
    else:
        engine.say(inp)
        engine.save_to_file(inp, 'test.mp3')
        engine.runAndWait()