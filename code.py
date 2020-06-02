import os 
import wolframalpha
import wikipedia
from tkinter import *
import tkinter.messagebox
import speech_recognition as sr
import time

while True:
	r = sr.Recognizer()

	with sr.Microphone() as source:
		print("speak something...")
		audio = r.listen(source)
		try:
			print("Recognizing...")
			text = r.recognize_google(audio)
			print('You said ' + text)
			if text =="stop":
				print("Program will exit.")
				break

			else:
				window = Tk()
				window.geometry("700x600")
				try:
					app_id = "YOUR API ID HERE"
					client = wolframalpha.Client(app_id)
					res = client.query(text)
					answer = next(res.results).text
					print("Answer from Wolfram|Alpha: ")
					print(answer)
					label1 = Label(window, justify=LEFT, wraplenght=650, compound=CENTER, padx=10, text=answer, font="times 15 bold")
					label1.pack()
					window.after(500000,lambda: window.destroy())
					minloop() 
				except Exception as e:
					print("No results from Wolfram|Alpha: ")
					answer = wikipedia.summary(text)
					print("Answer from wikipedia: ")
					print(answer)
					label1 = Label(window, justify=LEFT, wraplenght=650, compound=CENTER, padx=10, text=answer, font="times 15 bold")
					label1.pack()
					window.after(500000,lambda: window.destroy())
					minloop()

		except Exception as e:
			print(e)
			answer = "sorry we cannt hear you"
			print(answer)
