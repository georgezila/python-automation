import os
import webbrowser
# import time and sys for the loading bar and hacker thing
#-------------------------------------------------------------------------------

prompt = ">"

input = raw_input (prompt)

if input == "coding": # so if i type 'coding' it will do the thing
    os.system("open /System/Applications/Utilities/Terminal.app")
    os.system("open /Applications/Atom.app")

if input == "C#":
    os.system("open /Applications/Visual Studio.app")

if input == "app dev":
    os.system("open /Applications/Xcode.app")

if input == "bored":
    os.system("open /Applications/Safari.app")
    webbrowser.open("https://www.reddit.com")
    webbrowser.open("https://www.youtube.com")
    webbrowser.open("https://play.google.com/music/listen?u=1#/home")
