# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 18:29:39 2019

@author: srinidhi
"""
import speech_recognition as sr
audio_file = ("audio1.wav")
r=sr.Recognizer()
with sr.AudioFile(audio_file) as source:
    audio = r.record(source)
try:
    print("Audio File contains: "+r.recognize_google(audio))
except sr.UnknownValueError:
    print("Error")
except sr.RequestError:
    print("Error")
