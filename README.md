# python-automation
G'day fellow humans
The point of this very basic python program is to automate opening Applications and websites for you, though it's very basic
It's pretty useful and I even added some other features like a loading bar and a "hacker" looking terminal window.
(I'll leave some extra features at the bottom of the file)
Enjoy :)




here's how to add your own automation commands for my automation program

if input == "example": (this if statement says if you type 'example' it will run the code)

    os.system("open /Applications/Safari.app)
    (the os.system command lets python interact with your operating System. To change what it opens copy the path of that app)

    webbrowser.open("https://www.reddit.com")
    webbrowser.open("https://www.youtube.com")
    webbrowser.open("https://play.google.com/music/listen?u=1#/home")

    (the 'webbrowser.open' command will open whatever link you put in the ("example.com"))





if you repeat this line of code it will look like a hacker sort of thing idk (this has no real purpose and is really just a party trick)

--------------------------------------------------------------------------------
print("root%Name")
time.sleep(0.03)
--------------------------------------------------------------------------------
DON'T FORGET TO IMPORT "time"




the other thing I'll show is a quick loading bar (disclaimer i didn't write this but I couldn't find the person who did )

--------------------------------------------------------------------------------
toolbar_width = 77  #change the toolbar width to whatever suits you

# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for i in xrange(toolbar_width):
    time.sleep(0.03)
    # update the bar
    sys.stdout.write("-")
    sys.stdout.flush()

sys.stdout.write("]\n") # this ends the progress bar
--------------------------------------------------------------------------------
DON'T FORGET TO IMPORT "sys"

