import os

class CreateTree:
    def createtree():
    	groot = "Please copy and paste the directory in which you would like to create folders and files, then press Enter. If the command prompt is already on the correct root directory press Enter."
    	prompt = ">"
    	print(groot)
    	long_root = raw_input(prompt)
    	if long_root =='':
    		long_root = os.getcwd()
    	def iterativeTreeHelper(root_d):
    		def endRoot(loot):
        		short_root = loot.split('\\')[-1]
            	add_file_message = 'In ' + short_root + ', add file...'
            	return add_file_message
        	def file_creator(file_name):
    			create_files = []
            	while file_name != '':
            		create_files.append(file_name)
            		print(add_file_message)
            		new_file = input(prompt)
            	for file in create_files:
            		open(file,'w')
            def folder_creator(folder_name):
            	create_folders = []
            	while folder_name != '':
            		create_folders.append(folder_name)
            		print(add_folder_message)
            		new_folder = input(prompt)
            os.chdir(root_d)
        	print(endRoot(root_d))
        	new_file = input(prompt)
        	while new_file != '':
            	file_creator(new_file)

    	"""def recursiveTreehelper(root_d):
    		while != '':
    	createtreehelper(long_root)"""
    	iterativeTreeHelper(long_root)

# the iterations do have some kind of end eventually, but I'll need to figure that out later