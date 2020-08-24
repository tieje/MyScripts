import os
import pyperclip
import shutil
import time
import sys
from datetime import datetime

class RunSqlScriptsLogChecker:
    def __init__(self, sql_name, abs_dir, keywords):
        self.sql_name = sql_name
        self.path = abs_dir
        self.keywords = keywords
    def checking_logs(self):
        sql_log_name = self.sql_name[:-4]+".log"
        log_folder = os.path.join(self.path,"logs")     
        try:
            shutil.move(self.sql_name, os.path.join(self.path,"scripts_ran",self.sql_name))
        except:
            print(self.sql_name+" has already been moved.")
        no_errors = self.log_checker()
        try:
            shutil.move(sql_log_name, os.path.join(self.path,"logs",sql_log_name))
        except:
            print(sql_log_name+" has already been moved.")
        if no_errors:
            try:
                shutil.move(os.path.join(log_folder, sql_log_name), os.path.join(self.path,"logs","no_error_logs"))
            except:
                print(sql_log_name + " is already in no_error_logs")
            print(self.sql_name + " ran without errors.")
        else:
            print("Errors found in " + self.sql_name)
            print("Please check errors in error_results.txt")
            print("Copy and paste the following into Windows Explorer:")
            print(os.path.join(self.path,'error_results.txt'))
            time.sleep(10)
            print("Are these errors OK? If these errors are OK, Enter 'yes'.")
            affirmative_resps = ('yes','y','ye','yse')
            response = input(prompt)
            while response not in affirmative_resps:
                print("Please press 'Ctrl + C' to end all scripts. Otherwise, Enter 'yes' to signal that these errors are acceptable.")
                response = input(prompt)
            try:
                os.mkdir('past_error_results')
            except:
                print("past_error_results is already a folder")
            try:
                shutil.move(os.path.join(self.path,"error_results.txt"),os.path.join(self.path,"past_error_results","error_results_"+datetime.now().strftime("%H_%M_%d_%m")+".txt"))
            except:
                print("Error_results.txt has already been moved.")
        print(sql_log_name+" was checked.")
        return False
    def log_checker(self):
        total_errors = 0
        errors = open('error_results.txt','w')
        os.chdir(self.path)
        dir_list = os.listdir(self.path)
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
            errors.close()
            return True
        return False
    def only_logs(self, raw_list):
        raw = []
        for i in raw_list:
            if i[-4:] == '.log':
                raw.append(i)
            else:
                pass
        return raw



if __name__ == "__main__":
    prompt = '>'
    keywords = [
        'COMPILE',
        'SP2-',
        'ORA-',
        'PLS-',
        'ERROR-',
        'WARNING'
        ]
    current_directory = os.getcwd()
    sql_file_name = sys.argv[1]
    RunSqlScriptsLogChecker(sql_file_name, current_directory, keywords).checking_logs()