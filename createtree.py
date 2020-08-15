import os
class Solution:
    def __init__(self, groot, prompt, base_root):
        self.groot = groot
        self.base_root = base_root
        self.prompt = prompt
        self.path = base_root
    def org_creator(self,directory,createfile):
        try:
            while directory != '' and directory != None and createfile != 'stop':
                self.list_files()
                self.file_creator(directory, createfile)
                self.list_files() 
                print(self.message_gen(directory,'d'))
                new_folder = input(self.prompt)
                self.down_the_rabbit_hole(directory,new_folder, createfile)
                break
        except:
            print('Files and folders created.')
            return None
        return None
    # helper functions
    def list_files(self):
        """
        I took this function from the following link:
        https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python
        """
        for root, dirs, files in os.walk(self.path):
            level = root.replace(self.path, '').count(os.sep)
            indent = ' ' * 4 * (level)
            print('{}{}/'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print('{}{}'.format(subindent, f))
    def down_the_rabbit_hole(self,old_hole, hole, order):
        while hole != '' and hole != None and order != 'stop':
            # A folder is created, so we jump into the next rabbit hole
            new_hole = os.path.join(old_hole, hole)
            os.mkdir(new_hole)
            os.chdir(new_hole)
            self.org_creator(new_hole,'y')
        self.up_the_rabbit_hole()
    def up_the_rabbit_hole(self):
        geyser = os.getcwd()
        if geyser != self.base_root:
            os.chdir('..')
            geyser = os.getcwd()
            self.org_creator(geyser, 'n')
        self.org_creator(geyser, 'stop')
    def file_creator(self, file_path, action):
        if action == 'y':
            os.chdir(file_path)
            self.list_files()
            print(self.message_gen(file_path,'f'))
            new_file = input(self.prompt)
            while new_file != '' and new_file != None:
                open(new_file,'w')
                self.list_files()
                print(new_file +' has been created.')
                print(self.message_gen(file_path,'f'))
                new_file = input(self.prompt)
        else:
            pass
    def message_gen(self,loot, org_type):
        try:
            short_root = loot.split('\\')[-1]
            if org_type == 'f':
                gen_message = 'In ' + short_root + '/, add file...'
            else:
                gen_message = 'In ' + short_root + '/, add folder...'
            return gen_message
        except:
            print(os.getcwd())


if __name__ == "__main__":
    groot = "Please copy and paste the directory in which you would like to create folders and files, then press Enter. If the command prompt is already on the correct root directory press Enter."
    prompt = ">"
    print(groot)
    base_root = input(prompt)
    if base_root =='':
        base_root = os.getcwd()
    print(base_root)
    Solution(groot, prompt, base_root).org_creator(base_root, 'y')
print('Organization Complete')