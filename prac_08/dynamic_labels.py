"""
CP1404 - Simple Kivy app to dynamically create labels from a list of names
Your Name, IT@JCU
Date Started
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

__author__ = 'Your Name'

class DynamicLabelsApp(App):
    """ Kivy app to dynamically display a list of names as labels """

    def __init__(self, **kwargs):
        """ Initialize the app with a list of names """
        super().__init__(**kwargs)
        # Data model: list of names
        self.names = ["Emma", "Liam", "Olivia", "Noah"]

    def build(self):
        """ Build the GUI and populate it with labels """
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in self.names:
            label = Label(text=name, font_size=20)
            self.root.ids.main.add_widget(label)
        return self.root

DynamicLabelsApp().run()