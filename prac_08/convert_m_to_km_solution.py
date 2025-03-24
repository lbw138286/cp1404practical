"""
CP1404 Week 11 Workshop - GUI program to convert miles to kilometres
Your Name, IT@JCU
Date Started
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window

__author__ = 'Your Name'

MILES_TO_KM = 1.60934

class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """
    output_text = StringProperty("0.0")
    def build(self):
        """ Build the Kivy app from the kv file """
        Window.size = (300, 200)  # Adjusted for layout
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """ Handle calculation and update output_text """
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.output_text = str(result)

    def handle_increment(self, change):
        """ Handle up/down button press, update text input, and calculate """
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        """ Get and validate miles from text input, return 0 if invalid """
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

MilesConverterApp().run()