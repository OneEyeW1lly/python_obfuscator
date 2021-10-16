from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from helper.Confuser_functions import Confuser

class Misc():
    def __init__(self):
        self.file = None
        self.colors = {
            "Black": "\u001b[30m",
            "Red": "\u001b[31m",
            "Green": "\u001b[32m",
            "Yellow": "\u001b[33m",
            "Blue": "\u001b[34m",
            "Magenta": "\u001b[35m",
            "Cyan": "\u001b[36m",
            "White": "\u001b[37m",
            "Reset": "\u001b[0m"
        }

        self.title = self.colors["Magenta"] + '''
                      /$$$$$$                       /$$$$$$
                     /$$__  $$                     /$$__  $$
  /$$$$$$  /$$   /$$| $$  \\__/  /$$$$$$  /$$$$$$$ | $$  \\__//$$   /$$  /$$$$$$$  /$$$$$$   /$$$$$$
 /$$__  $$| $$  | $$| $$       /$$__  $$| $$__  $$| $$$$   | $$  | $$ /$$_____/ /$$__  $$ /$$__  $$
| $$  \\ $$| $$  | $$| $$      | $$  \\ $$| $$  \\ $$| $$_/   | $$  | $$|  $$$$$$ | $$$$$$$$| $$  \\__/
| $$  | $$| $$  | $$| $$    $$| $$  | $$| $$  | $$| $$     | $$  | $$ \\____  $$| $$_____/| $$
| $$$$$$$/|  $$$$$$$|  $$$$$$/|  $$$$$$/| $$  | $$| $$     |  $$$$$$/ /$$$$$$$/|  $$$$$$$| $$
| $$____/  \\____  $$ \\______/  \\______/ |__/  |__/|__/      \\______/ |_______/  \\_______/|__/
| $$       /$$  | $$
| $$      |  $$$$$$/
|__/       \\______/
''' + self.colors["Reset"]

        self.author = self.colors["Green"] + "https://github.com/toastedwaffless" + self.colors["Reset"]
        self.options = self.colors['Cyan'] + "\tChoose type of obfuscation:\n\t\t1 > Base64 Encryption\n\t\t2 > String XOR encryption (Will ERROR on f-strings, format-strings and unicode escape codes)\n\t\t3 > Variable rename\n\t\t4 > All of the obove"

    def PrintScreen(self):
        print(f'{self.title}\n\t\t\t\t{self.author}\n\n\n{self.colors["Reset"]}')
        print(f'{self.colors["Yellow"]}\tChoose a file to Confuse{self.colors["Reset"]}')
        self.choose_file()
        choice = int(input(f'{self.options}\n\n>{self.colors["Reset"]}'))
        if not choice > 4 and not choice < 1:
            if choice == 1:
                rec = int(input(f"{self.colors['Cyan']}Amount of recursions to preform >{self.colors['Reset']}"))
                CON.use_base64_encyption(self.file, rec)
            if choice == 2:
                xor_key = int(input(f"{self.colors['Cyan']}String XOR encryption key >{self.colors['Reset']}"))
                CON.use_random_obfuscation(self.file, xor_key)
            if choice == 3:
                CON.use_variable_obfuscation(self.file)
            if choice == 4:
                xor_key = int(input(f"{self.colors['Cyan']}String XOR encryption key >{self.colors['Reset']}"))
                rec = int(input(f"{self.colors['Cyan']}Amount of base64 recursions to preform >{self.colors['Reset']}"))
                CON.use_all_encryption(self.file, rec, xor_key)
        else:
            print(f"{self.colors['Red']}Please input a valid option{self.colors['Reset']}")


    def choose_file(self):
        self.file = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        print(self.file)

    def loading_bar(self):
        pass

if __name__ == '__main__':
    Tk().withdraw()
    MISC = Misc()
    CON = Confuser()

    MISC.PrintScreen()

