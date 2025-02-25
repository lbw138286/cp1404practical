HEX_COLOURS = {
    "AliceBlue": "#F0F8FF",
    "AntiqueWhite": "#FAEBD7",
    "Aqua": "#00FFFF",
    "Aquamarine": "#7FFFD4",
    "Azure": "#F0FFFF",
    "Beige": "#F5F5DC",
    "Bisque": "#FFE4C4",
    "Black": "#000000",
    "BlanchedAlmond": "#FFEBCD",
    "Blue": "#0000FF",
}
print("Hex Colour Lookup")
colour_name = input("Enter a colour name: ").strip()
while colour_name:
    colour_key = colour_name.replace(" ", "").title()
    if colour_key in HEX_COLOURS:
        print(f"The hex code for {colour_key} is {HEX_COLOURS[colour_key]}")
    else:
        print("Invalid colour name. Try again.")
    colour_name = input("Enter a colour name: ").strip()
print("Goodbye!")