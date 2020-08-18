import os
import pyperclip

class MyScripts:
    def __init__(self, home, work):
        self.home = home
        self.work = work
    def ChangeDir(self):
        message = "Immediately paste into the command line."
        try:
            os.chdir(self.work)
            pyperclip.copy('cd ' + self.work)
        except:
            os.chdir(self.home)
            pyperclip.copy('cd ' + self.home)
        print(message)
        return None
if __name__ == "__main__":
    home = r"C:\MyScripts"
    work = r"C:\CustomOfficeTemplates\current_code\MyScripts"
    MyScripts(home,work).ChangeDir()