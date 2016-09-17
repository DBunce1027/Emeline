#==================================================================
# *** Emeline Butler 0.1 ***
# The goal of this program is to make an integrated service AI that 
# interacts and responds with the users voice. Commands will get 
# increasingly complex as the program evolves which may or may not
# include machine learning. 
# ***					 ***
# Property of Devin Bunce & Vishwa Shah
# Created September 14th 2016
#==================================================================

#=============
# Import Files
#=============
import speech_recognition as sr
import webbrowser as wb
from gtts import gTTS

import Em_fun.py

#==========================
# Check if Emeline is there
#==========================
obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
     print("Check if Emeline is there.")
     audio = r.listen(source)

call = r.recognize_google(audio)
print(call)

#===============================
# Begin interaction with Emeline
#===============================
call = "Emma"
command = "open"

while "done" not in command:
	if "Emma" in call:

		if "woop woop" in call:
			woop_woop()

		elif "where is" in call:
			#TODO: eed a way to grab the word after where is
			where_is("England")

		elif "done" in call:
			command = end()

		else:
			#new command
			print("Yes Master Bunce. What can I do for you?")
			with sr.Microphone() as source:
			command_audio = r.listen(source)
			call = "Emma" + r.recognize_google(command_audio)

		#Check for updated commands
		print("Will that be all sir?")
		with sr.Microphone() as source:
		command_audio = r.listen(source)
		call = "Emma" + r.recognize_google(command_audio)
#===============================================
# You have successfully interacted with Emeline!
#===============================================