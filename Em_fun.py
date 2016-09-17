#=============
# Import Files
#=============
import speech_recognition as sr
import webbrowser as wb
from gtts import gTTS

#==============================
# Begin structure for responses
#==============================
def woop_woop():
	print("That's the sound of the police!")
	wb.open("https://www.youtube.com/watch?v=9ZrAYxWPN6c",0)

def where_is(location):
	#TODO:find location on google maps.
	wb.open("https://google.com/maps/place/" + location + "/&amp;",0)

def end():
	print("Have a great day sir!")
	return "done"