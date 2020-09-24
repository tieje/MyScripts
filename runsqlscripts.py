import os
import subprocess
import shutil
import re

class RunSqlScripts:
    # create the zz_drive.sql file based on existing examples
    def __init__(self, working_directory, db_name, pause_option):
        self.working_directory = working_directory
        self.db_name = db_name
        self.pause_option = pause_option
    def create_driver(self):
        driver_name = "custom_driver.sql"
        os.chdir(self.working_directory)
        sqlfiles = []
        for i in os.listdir():
            if i != driver_name:
                sqlfiles.append(i)
        unordered_numbers = self.only_x(sqlfiles, ".sql")
        final_sql_order = self.sort_files(unordered_numbers)
        ordered_spools = self.check_spool(unordered_numbers, final_sql_order)
        self.driver = open(driver_name,'w')
        final_string = self.write_string(ordered_spools)

        print("Driver has been created.")
        try:
            shutil.move(log_checker2, self.working_directory)
        except:
            print("Log checkers have already been moved.")
        try:
            os.mkdir('logs')
            os.mkdir('scripts_ran')
            os.mkdir(r"logs\no_error_logs")
        except:
            print("Folders have already been created.")
            pass
        self.driver.close()
        subprocess.run("sqlplus sc_base/superman@"+self.db_name+" @"+os.path.join(self.working_directory,driver_name), shell=True)
        return True
    # helper functions
    def write_string(self, sql_input):
        script_list = []
        log_checker_sqlplus_command = "host runsqlscriptslogchecker.py"
        ending2 = "host move "+os.path.join(self.working_directory, "runsqlscriptslogchecker.py")+" "+return_loc
        for i in sql_input:
            i_string = str(i[0])
            if i[2] == 'nospool':
                self.driver.write("\nspool " + '"'+i_string[:-4] + '.log"'+'\n@"' + os.path.join(self.working_directory, i_string) + '";\nspool off;')
            else:
                self.driver.write("\n@" +'"'+ i[0]+'"')
            self.driver.write("\n" + log_checker_sqlplus_command + " " + '"'+i_string+' //// '+ i[3] + '"' "\n")
            if self.pause_option == 'yes' or self.pause_option == 'y':
                self.driver.write("\nSET PAUSE ON\n" + "PAUSE Check results. Press Enter to begin running scripts again.\n\n")
        self.driver.write("\n"+"\n"+ending2)
        return self.driver

        # script list needs custom commands to run a short custom log checker

    def check_spool(self,spool_list, order_of_files):
        spool_exists = []
        log_name = []
        for i in spool_list:
            file = open(i,'r')
            first_lines = file.readlines()[:11]
            spool_presence = False
            for line in range(len(first_lines)):
                if 'spool' in first_lines[line].lower():
                    spool_presence = True
                    spool_line = line
                else:
                    pass

            if spool_presence:
                spool_exists.append('spool')
                log_name_in_file = re.search(' ' + '.+' + '(txt|log)$', first_lines[spool_line], re.I).group()
                log_name.append(log_name_in_file[1:])
            else:
                spool_exists.append('nospool')
                log_name.append(i[:-4] + '.log')
        spool_checked = zip(spool_list, order_of_files, spool_exists, log_name)
        final_order = sorted(spool_checked, key=lambda files1: int(files1[1]))
        return final_order

    def sort_files(self,file_list):
        ordered_files = []
        order_of_files = []
        for i in file_list:
            print("What is the order of " + i + " ? Please Enter the integer number of order.")
            order = input(prompt)
            ordered_files.append((i,order))
            order_of_files.append(order)
        # order sql files
        final_sql_order = sorted(ordered_files, key=lambda sqlfile: int(sqlfile[1]))
        for x in final_sql_order:
            print(x)
        self.response = 'response'
        affirmative_resps = ('yes','y','ye','yse')
        while self.response not in affirmative_resps:
            print("Is this the correct order? Type 'yes' if the order is correct.")
            self.response = input(prompt)
            if self.response in affirmative_resps:
                break
            else:
                self.sort_files(file_list)
        return order_of_files

    def only_x(self, raw_list, file_type):
        files = []
        for i in raw_list:
            if i[-4:].lower() == file_type:
                files.append(i)
            else:
                pass
        return files
def db_look_up(tnspath, dbname):
    os.chdir(tnspath)
    tns = open('tnsnames.ora', 'r')
    for i in tns.readlines():
        if dbname.lower() in i[:25].lower():
            return True
    return False
if __name__ == "__main__":
    log_checker2 = r"C:\CustomOfficeTemplates\current_code\MyScripts\runsqlscriptslogchecker.py"
    return_loc = r"C:\CustomOfficeTemplates\current_code\MyScripts"
    tnsnamesora_path = r"C:\oracle\product\12.1.0\client_1\network\admin"
    prompt = '>'
    message1 = "Enter the path of the sql scripts, OR press enter if the cmd prompt is on the correct working directory."
    message2 = "Enter the database name."
    message3 = "Please enter a valid database name or press Ctrl + C to exit."
    message4 = "Type 'yes' if you would you like the script to pause in between running individual sql scripts. Otherwise press Enter."
    print(message1)
    working_directory = input(prompt)
    if bool(working_directory) == False:
        working_directory = os.getcwd()
    print(message2)
    db_name = input(prompt)
    db_results = db_look_up(tnsnamesora_path, db_name)
    while db_results==False:
        print(message3)
        db_name = input(prompt)
        db_results = db_look_up(tnsnamesora_path, db_name)
    os.chdir(working_directory)
    print(message4)
    pause_option = input(prompt)
    RunSqlScripts(working_directory, db_name, pause_option).create_driver()