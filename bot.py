import speech_recognition as sr
import pyttsx3
import pywhatkit


listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say("Hey there")
engine.runAndWait()
def talk(text):
	engine.say(text)
	engine.runAndWait()
	print(text)
def takecommands():
	try:
		with sr.Microphone() as source:
			print("Hey there I am listening")
			voice = listener.listen(source)
			command = listener.recognize_google(voice)
			if "dude" in command:
				command = command.replace("dude",'')
				talk(command)
	except:
		pass

	return command

def run_dude():
	xyz=takecommands()
	song=xyz.replace("play","")
	if "play" in xyz.lower():
		talk("Playing " + song)
		pywhatkit.playonyt(song)
	if "send message" in xyz.lower():
		pywhatkit.sendwhatmsg("","",11,40)

	if "search" in xyz.lower():
		pywhatkit.search(xyz)


run_dude()