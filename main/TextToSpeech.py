# -------------------------Text To Speech with GUI-----------------------------
# author: Mohammadreza Amani
# GitHub: https://www.github.com/MohammadrezaAmani
# Linkedin: https://www.linkedin.com/in/mohammadreza-amani/
# Date: 2022/01/31 - Updated_at: Sep/14/2023

# ---------------------------------logic----------------------------------------
# get the text from the user and convert it to speech
# using gtts
# ------------------------------import libraries--------------------------------

# importing some required libraries for frontend
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.list import OneLineIconListItem

# importing some required libraries for backend
import gtts
from playsound import playsound
import os
import datetime

# seting the window size
Window.size = (360, 640)

# kv code for frontend
text = """
BoxLayout:
    orientation: 'vertical'
    MDTopAppBar:
        title: "Text to Speech"
        elevation: 10
    ScrollView:
        MDList:
            id: list
    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        height: dp(50)
        padding: dp(10)
        spacing: dp(10)
        MDTextField:
            hint_text: "Your text here"
            id: text_field
            multiline: True
        MDRaisedButton:
            text: "Clear"
            on_release: app.clear_text()
        MDRaisedButton:
            text: "Save"
            on_release: app.save()
        MDRaisedButton:
            text: "Speak"
            on_release: app.speak()
"""


# creating the class for the frontend


class MYAPP(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = "500"
        self.title = "Text to Speech"
        return Builder.load_string(text)

    # function for find the name of the file
    def name(self, text):
        return "{}{}.mp3".format(
            text, datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        )

    # function for the save button

    def save(self):
        if self.root.ids.text_field.text != "":
            print(self.root.ids.text_field.text)
            # converting the text to speech
            tts = gtts.gTTS(text=self.root.ids.text_field.text, lang="en", slow=False)
            self.root.ids.list.add_widget(
                OneLineIconListItem(text=self.root.ids.text_field.text)
            )
            # name of file :
            text = ""
            if len(self.root.ids.text_field.text) > 20:
                if len(self.root.ids.text_field.text.split()[0]) < 20:
                    text = self.root.ids.text_field.text.split()[0]
                else:
                    text = self.root.ids.text_field.text.split()[0][:20]
            else:
                text = self.root.ids.text_field.text
            text = self.name(text)
            self.root.ids.text_field.text = ""
            # saving the file
            tts.save(text)
            # playing the file
            return text

    # function for the text_validate button
    def speak(self):
        try:
            playsound(self.save())
        except:
            print("invalid text")
            self.root.ids.text_field.text = ""


# creating the instance of the class and running the app
if __name__ == "__main__":
    MYAPP().run()
