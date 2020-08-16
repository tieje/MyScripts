import os
from createtree import Solution

class CreateScript():
    def __init__(self, absolute_path,prompt, custom_path):
        self.path = absolute_path
        self.prompt = prompt
        self.custom_path = custom_path
    def starterquestions(self):
        question1 = "Would you like to create your script in the default location? If not, paste the script location."
        print(question1)
        answer1 = input(self.prompt)
        default_answer1 = ['y','yes','', 'ye', ' ']
        question2 = "What would you like this script to be called?"
        print(question2)
        answer2 = input(self.prompt)
        if answer1.lower() not in default_answer1:
            self.custom_path = answer1
        self.script_creator(answer2)
        Solution.list_files(self)
        print('Script creation successful in the following path:')
        print(self.path)
    def script_creator(self, script_name):
        try:
            name = script_name.lower()
            name_nospace = name.replace(' ','')     
            if self.custom_path != '':
                os.chdir(self.custom_path)
                open(name_nospace + 'design_doc.txt','w')
                open(name_nospace + 'READ_ME.txt','w')
                self.path = self.custom_path
            else:
                os.chdir(os.path.join(self.path, 'design_docs'))
                open(name_nospace + '_design_doc.txt','w')
                os.chdir(os.path.join(self.path, 'read_mes'))
                open(name_nospace + '_readme.txt','w')
                os.chdir(self.path)
            class_name = name.title()
            py_name = name + '.py'
            new_file = open(py_name, 'w')
            new_file.write('import os' + '\n\nclass ' + class_name.replace(' ','') + ':' + '\n\n' + r'if __name__ == "__main__":')
        except:
            print('The path does not exist.')
            return None

if __name__ == "__main__":
    default_path = r"C:\CustomOfficeTemplates\current_code\MyScripts"
    custom_path = ''
    prompt = '>'
    CreateScript(default_path,prompt, custom_path).starterquestions()