import os
from datetime import datetime
import pyperclip
import re

class SqlScriptDeployment:
    def __init__(self, abs_dir):
        self.abs_dir = abs_dir
    def create_deployment(self):
        os.chdir(self.abs_dir)
        for i in os.listdir():
            print(i)
        print("Which folder would you like to make a new case (match folder name exactly)? Enter 'new' or 'n' if it's a new folder.")
        response = input(prompt)
        if response == 'new' or response == 'n':
            print("What will be the name of the new folder?")
            new_directory = input(prompt)
            os.mkdir(new_directory)
            os.chdir(new_directory)
        else:
            
            result = re.search(response, str(os.listdir(self.abs_dir)), re.I)
            # Second try
            while bool(result) == False:
                for i in os.listdir(self.abs_dir):
                    print(i)
                print('Please type the folder again.')
                response = input(prompt)
                result = re.search(response, str(os.listdir(self.abs_dir)), re.I)
            os.chdir(os.path.join(self.abs_dir, response))
        date_now = datetime.now().strftime("%d_%m_%Y")
        os.mkdir(date_now)
        new_path = os.path.join(os.getcwd(), date_now)
        print("\n\nThe following path has been copied to your clipboard. Paste this path.\n\n")
        print(new_path)
        pyperclip.copy(new_path)
        return True

if __name__ == "__main__":
    default = r"C:\Deployment"
    question1 = "Would you like to create your script in the default location? If not, paste the script location."
    prompt = '>'
    print(question1)
    answer = input(prompt)
    if bool(answer) == False:
        answer = default
    SqlScriptDeployment(answer).create_deployment()