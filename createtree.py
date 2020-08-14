import os

def org_creator(directory,createfile):
    try:
        while directory != '' and directory != None and createfile != 'stop':
            list_files(base_root)
            file_creator(directory, createfile)
            list_files(base_root) 
            print(message_gen(directory,'d'))
            new_folder = input(prompt)
            down_the_rabbit_hole(directory,new_folder, createfile)
            break
    except:
        print('Organization Complete')
# helper functions
def list_files(startpath):
    """
    I took this function from the following link:
    https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python
    """
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))
def down_the_rabbit_hole(old_hole, hole, order):
    while hole != '' and hole != None and order != 'stop':
        # A folder is created, so we jump into the next rabbit hole
        new_hole = os.path.join(old_hole, hole)
        os.mkdir(new_hole)
        os.chdir(new_hole)
        org_creator(new_hole,'y')
    up_the_rabbit_hole()
def up_the_rabbit_hole():
    geyser = os.getcwd()
    if geyser != base_root:
        os.chdir('..')
        geyser = os.getcwd()
        org_creator(geyser, 'n')
    org_creator(geyser, 'stop')
def file_creator(file_path, action):
    if action == 'y':
        list_files(file_path)
        print(message_gen(file_path,'f'))
        new_file = input(prompt)
        while new_file != '' and new_file != None:
            open(new_file,'w')
            list_files(file_path)
            print(new_file +' has been created.')
            print(message_gen(file_path,'f'))
            new_file = input(prompt)
    else:
        pass
def message_gen(loot, org_type):
    try:
        short_root = loot.split('\\')[-1]
        if org_type == 'f':
            gen_message = 'In ' + short_root + '/, add file...'
        else:
            gen_message = 'In ' + short_root + '/, add folder...'
        return gen_message
    except:
        print(os.getcwd())

groot = "Please copy and paste the directory in which you would like to create folders and files, then press Enter. If the command prompt is already on the correct root directory press Enter."
prompt = ">"
print(groot)
base_root = input(prompt)
if base_root =='':
    base_root = os.getcwd()

org_creator(base_root, 'y')

print('Organization Complete')