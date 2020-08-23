import os
import subprocess



class RunSqlScripts:
    # create the zz_drive.sql file based on existing examples
    def __init__(self, working_directory, db_name):
    	self.working_directory = working_directory
    	self.db_name = db_name
    def create_driver(self)
        sqlfiles_order = []
        os.chdir(self.working_directory)
        driver = open('custom_driver.sql','w')
        sqlfiles = self.only_x(os.listdir(), ".sql")
        final_sql_order = self.sort_files(sqlfiles)
        print("Driver is ")
    # helper functions
    def sort_files(file_list):
    	ordered_files = []
        for i in file_list:
        	print("What is the order of " + i + " ? Please Enter the integer number of order.")
        	order = input(prompt)
        	sqlfiles_order.append(tuple(i, order))
        # order sql files
        final_sql_order = sorted(sqlfiles_order, key=lambda sqlfile: sqlfile[1])
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
        return ordered_files

    def only_x(self, raw_list, file_type):
    	files = []
    	for i in raw_list:
    		if i[-4:] == file_type:
    			files.append()
    		else:
    			pass
    	return files
def db_look_up(tnspath, dbname):
	os.chdir(tnspath)
	tns = open('tnsnames.ora', 'r')
	for i in tns.readlines():
		if dbname in i[:25]:
			return True
	return False
if __name__ == "__main__":
	tnsnamesora_path = r"C:\oracle\product\12.1.0\client_1\network\admin"
	prompt = '>'
	message1 = "Enter the path the sql scripts, OR press enter if the cmd prompt is on the correct working directory."
	message2 = "Enter the database name."
	message3 = "Please enter a valid database name or press Ctrl + C to exit."
	print(message1)
	working_directory = input(prompt)
	if bool(working_directory):
		working_directory = os.getcwd()
	print(message2)
	db_name = input(prompt)
	db_results = db_look_up(tnsnamesora_path, db_name)
	while db_results==False:
		print(message3)
		db_name = input(prompt)
	    db_results = db_look_up(tnsnamesora_path, db_name)
	os.chdir(working_directory)
	RunSqlScripts(working_directory, db_name).create_driver()