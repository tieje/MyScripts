import os

class Solution:
    groot = "Please copy and paste the directory in which you would like to create folders and files, then press Enter. If the command prompt is already on the correct root directory press Enter."
    prompt = ">"
    def introduction():
        print(groot)
        roots = input(prompt)
        if roots =='':
            roots = os.getcwd()
        org_creator(roots)
    def org_creator(directory,createfile):
        list_files(directory)
        file_creator(directory, createfile)        
        print(message_gen(directory,'d'))
        new_folder = input(prompt)
        down_the_rabbit_hole(directory,new_folder)
        Print('Organization Completed.')
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
    def down_the_rabbit_hole(old_hole, hole):
        while hole != '':
            # A folder is created, so we jump into the next rabbit hole
            new_hole = os.path.join(old_hole, hole)
            os.chdir(new_hole)
            org_creator(new_hole,'y')
        up_the_rabbit_hole(old_hole)

    def up_the_rabbit_hole(geyser):
        while geyser != roots
            new_geyser = os.chdir('..')
            org_creator(new_geyser, 'n')
        pass

    def file_creator(file_path, action):
        if action == 'y':
            create_files = []
            print(gen_message(file_path,'f'))
            new_file = input(prompt)
            while new_file != '':
                create_files.append(new_file)
            for file in create_files:
                open(file,'w')
        else:
            pass

    def message_gen(loot, org_type):
        short_root = loot.split('\\')[-1]
        if org_type == 'f'
            gen_message = 'In ' + short_root + ', add file...'
        else:
            gen_message = 'In ' + short_root + ', add folder...'
        return gen_message

Solution().introduction()