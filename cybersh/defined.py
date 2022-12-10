red="\033[0;31m"          # Red

yellow="\033[0;33m"       # Yellow

green="\033[0;32m"        # Green

color_off="\033[0m"       # Text Reset

bblack="\033[1;30m"       # Black

bred="\033[1;31m"         # Red

ured="\033[4;31m"         # Red

on_green="\033[42m"       # Green

blue="\033[0;34m"         # Blue

lightblue = '\033[94m'

red = '\033[91m'

white = '\33[97m'

yellow = '\33[93m'

green = '\033[1;32m'

cyan  = "\033[96m"

end = '\033[0m'

purple="\033[0;35m"

color_off="\033[0m"       # Text Reset


rst="\033[0m"
b="\033[1;30m"
r="\033[1;31m"
g="\033[1;32m"
yl="\033[1;33m"
bl="\033[1;34m"
p="\033[1;35m"
c="\033[1;36m"
w="\033[1;37m"
def ani(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)


  
logo=(red+"""
      _____      _                  _____ _    _
     / ____|    | |                / ____| |  | |
    | |    _   _| |__   ___ _ __  | (___ | |__| |
    | |   | | | | '_ \ / _ \ '__|  \___ \|  __  |
    | |___| |_| | |_) |  __/ |     ____) | |  | |
     \_____\__, |_.__/ \___|_|    |_____/|_|  |_|
            __/ |
           |___/""")

line=(yellow+"================================================================================================================")

tv=requests.get("https://raw.githubusercontent.com/ShTasrif/cybersh/main/.version.txt").text
tversion=(cyan+"\t\t     Version : "+tv)

devoloper=(green+"\t\tDevoloped By : SH TASRIF ")

def finput():
	print("\n\t   ",cyan+"[",green+"Now Press",yellow+"Enter",green+" Key To Continue",cyan+"]")

def clear():
	os.system("clear")
