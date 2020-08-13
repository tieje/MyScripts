"""
8/12/2020

I want to script primarily in python rather than powershell because I'm better at python.
I do understand that I'll need to use powershell sometimes because some things can be done more simply in powershell.

I want to learn how to script because I like automating work given to me. The faster I can automate tasks, the more time I'll have to devote to other projects.


https://docs.microsoft.com/en-us/windows/python/scripting



Create new folders in powershell
mkdir
mkdir folder1\new_directory, folder1\folder2\new_directory

Create new files in powershell
new-item
new-item folder1\item1.txt, folder1\folder2\item2.txt



https://towardsdatascience.com/10-python-file-system-methods-you-should-know-799f90ef13c2

Must import os and shutil
import os
import shutil

Get Info

os.getcwd() — get the current working directory path as a string — pwd
returns
'C:\\CustomOfficeTemplates\\py\\custom_code\\practice\\windows_scripting\\tutorial_08_12_2020'

os.listdir() — get the contents of the current working directory as a list of strings — ls
returns
['food', 'src']

os.walk("starting_directory_path")— returns a generator with name and path info for directories and files in the the current directory and all subdirectories— no exact short CLI equivalent, but ls -R provides subdirectory names and the names of files within subdirectories
Returns
<generator object walk at 0x00000262FE777318>
# Used for iterating over directories


Change Things

os.chdir("/absolute/or/relative/path") — change the current working directory — cd



os.path.join()—create a path for later use — no short CLI equivalent

os.makedirs("dir1/dir2") — make directory —mkdir -p

shutil.copy2("source_file_path", "destination_directory_path") — copy a file or directory — cp

shutil.move("source_file_path", "destination_directory_path") — move a file or directory — mv

os.remove("my_file_path") — remove a file — rm

shutil.rmtree("my_directory_path")— remove a directory and all files and directories in it —rm -rf






https://realpython.com/python-pathlib/



https://pbpython.com/pathlib-intro.html



https://docs.python.org/3.7/library/filesys.html

Projects

Template
-----------------------------------------------------
Began

Title:
Summary:
Status:

Ended
-----------------------------------------------------

-----------------------------------------------------
Began 8/12/2020

Title: createcase
Small Project: Create a script that creates case folders for clients
Status: On hold until createtree is completed

Ended
-----------------------------------------------------

-----------------------------------------------------
Began 8/12/2020

Title: createtree
Small Project: Create a script that creates a tree of folder and items
Status: Currently working on

Ended
-----------------------------------------------------

-----------------------------------------------------
Began

Title: logchecker
Summary: Create a script that checks log files for errors for sql scripts ran in sqlplus
Status: Have not started

Ended
-----------------------------------------------------


"""
