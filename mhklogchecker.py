import os
import pyperclip
from datetime import datetime

class MhkLogChecker:
    def __init__(self, path,keywords):
        self.path = path
        self.keywords = keywords
    def check_logs(self):
        total_errors = 0
        errors = open('error_results.txt','w')
        os.chdir(self.path)
        dir_list = os.listdir()
        logs_list = self.only_logs(dir_list)
        errors.write(datetime.now().strftime("%d/%m/%Y %H:%M"+'\n'))
        for log_file in logs_list:
            line_count = 0
            file = open(log_file,'r')
            errors.write('\n\n'+log_file+'\n\n')
            all_lines = file.readlines()
            for line in all_lines:
                line_count += 1
                for kword in self.keywords:
                    if kword in line:
                        total_errors += 1
                        errors.write("Line "+str(line_count)+' '+'"'+kword+'"' + ': ' + line)
                    else:
                        pass
        print(str(total_errors) + ' errors present.')
        if total_errors == 0:
            print("No errors, you're all set!")
        print("Paste and Enter to check error results.")
        pyperclip.copy(os.path.join(self.path,'error_results.txt'))
        return None

    # helper functions
    def only_logs(self, raw_list):
        logs = []
        for i in raw_list:
            if i[-4:] == '.log':
                logs.append(i)
            else:
                pass
        return logs
if __name__ == "__main__":
    message = "Paste a path or press Enter to use the current path."
    prompt = ">"
    keywords = [
        'COMPILE',
        'SP2-',
        'ORA-',
        'PLS-',
        'ERROR-',
        'WARNING'
    ]
    print(message)
    path = input(prompt)
    if bool(path) == False:
        path = os.getcwd()
    MhkLogChecker(path,keywords).check_logs()