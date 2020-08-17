import os
# import shutil
import re
from createtree import Solution


class CreateCase:
    def __init__(self, absolute_path, cdd_path, list_directories, prompt,path):
        self.absolute_path = absolute_path
        self.cdd_path = cdd_path
        self.list_directories = list_directories
        self.prompt = prompt
        self.path = path
    def dir_matcher(self,folder):
        print(self.list_directories)
        print("Which folder would you like to make a new case? Enter 'new' or 'n' if it's a new folder.")
        response = input(prompt)
        if response == 'new' or response == 'n':
            os.chdir(self.absolute_path)
            print("What will be the name of the new folder?")
            next_directory = input(prompt)
            os.mkdir(next_directory)
        else:
            self.list_directories = os.listdir(absolute_path)
            result = re.search(response, str(self.list_directories), re.I)
            # Second try
            if result == None:
                self.list_directories = os.listdir(absolute_path)
                print(self.list_directories)
                print('Please type the folder again.')
                response = input(prompt)
                if response == None:
                    print('The script has ended. Type the client folder correctly next time.')
                    return None
                result = re.search(response, str(self.list_directories), re.I)   
            next_directory = result.group()
        rabbit_hole = os.path.join(self.absolute_path,next_directory)
        os.chdir(rabbit_hole)
        self.case_creator(os.getcwd())
    def case_creator(self, working_dir):
        print('What is the case number')
        case_number = input(prompt)
        if case_number == '' or case_number == None:
            print('The script has ended. Get the case number first.')
            return None
        print('What is the case description? This is optional.')
        description = input(prompt)
        if description == '\n' or description == '' or description == None:
            new_folder = case_number
        else:
            new_folder = case_number + ' - ' + description
        # Case folder creation
        os.mkdir(new_folder)
        case_folder = os.path.join(working_dir,new_folder)
        os.chdir(case_folder)
        os.mkdir('Deployment')
        os.mkdir('Code')
        os.mkdir('Documentation')
        os.chdir(os.path.join(case_folder, 'Code'))
        open(case_number + '_scratch.sql','w')
        # permission denied for copying files on this computer
        # shutil.copy2(self.cdd_path, os.path.join(case_folder, 'Documentation'))
        self.path = case_folder
        Solution.list_files(self)
        print('Copy and paste the following path into File Explorer')
        print(case_folder)

if __name__ == "__main__":
    absolute_path = r'C:\Users\tfrancis\OneDrive - Hearst\Cases'
    cdd_path = r'C:\Users\tfrancis\OneDrive - Hearst\Templates'
    list_directories = os.listdir(absolute_path)
    prompt = '>'
    path = ''
    CreateCase(absolute_path, cdd_path, list_directories, prompt,path).dir_matcher(absolute_path)