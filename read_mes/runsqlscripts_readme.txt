This script runs sql scripts in sqlplus.


No special python packages.

- Add the folder that this script is in to PATH on Windows Env
- Read and follow instructions.
- python 3.7
- generates a sql script and creates folders
- run this script in a folder that only contains the sql scripts you intend to run
- If the script is not working as intended, it's either because the sql scripts are missing a semi-colon or because it's spooling to a .txt file instead of a .log file
	- If the sql script spools to a .txt file, you'll need to run the mhklogchecker.py script manually on the location.

- Do NOT run this script on OneDrive folders. The runsqlscriptlogchecker.py file is moved to the Onedrive file location, but it cannot be moved back to it's original place from the command line due to lack of permissions.

- variables logchecker2, return_loc, and tnsnamesora_path must be updated to the location of runsqlscriptslogchecker.py and the folder of it, respectively
	# Ex.
    log_checker2 = r"C:\CustomOfficeTemplates\current_code\MyScripts\runsqlscriptslogchecker.py"
    return_loc = r"C:\CustomOfficeTemplates\current_code\MyScripts"
    tnsnamesora_path = r"C:\oracle\product\12.1.0\client_1\network\admin"