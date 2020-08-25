No special python packages.

- Add the folder that this script is in to PATH on Windows Env
- Read and follow instructions.
- python 3.7
- generates a sql script and creates folders
- run this script in a folder that only contains the sql scripts you intend to run

- Do NOT run this script on OneDrive folders. The runsqlscriptlogchecker.py file is moved to the Onedrive file location, but it cannot be moved back to it's original place from the command line due to lack of permissions.

- variables logchecker2 and return_loc must be updated to the location of runsqlscriptslogchecker.py and the folder of it, respectively
	# Ex.
    log_checker2 = r"C:\CustomOfficeTemplates\current_code\MyScripts\runsqlscriptslogchecker.py"
    return_loc = r"C:\CustomOfficeTemplates\current_code\MyScripts"