- python 3.7
- pip install xlwings
- change the "default" variable to be the path of the folder that contains the folders for company-specific bug reports
- will not work correctly if there are more than 26 columns

------------------------------------------------------

Steps for using this script

1. Update your company-specific default folder from SVN (subversion)

2. Export the issue report from excel with the correct three-letter company label and the following columns included:
	- Description
	- Environment
	- External Tracking #
	- Key
	- Labels
	- Priority
	- Release Source
	- Resolution
	- Status
	- Summary
    Use these as your default columns.


3. Save the export as an .xlsx file in your company-specific default folder:
	Ex.
	default is C:\WebTesting_Jira\Reports
	company-specific default is C:\WebTesting_Jira\Reports\KPC

4. Rename your reports in the following way:
    NEW_[COMPANY NAME]_BUG_REPORT_09_03_2020
    OLD_[same as above, just put the "OLD" as the first word]
    Putting the New and Old in front will be important.

5. Run the script: designbugreport.py

6. Commit changes to SVN.

------------------------------------------------------

Instructions for BRMs

1. Please checkout the company-specific folder from SVN.
    a. In this case they will be located in the following location in SVN:
    svn:https://mpsvn.medhokapps.com/cps/CPS/_Sandbox/ThomasF/WebTesting_Jira/Reports/KPC

2. If you want to make changes to the bug report, please do the following:
    a. First Update from SVN.
    b. You can make your changes to the Excel file labeled with "NEW".
    c. Keep in mind that only changes made to the "Status" column will be saved from one report to the next.
    c. Commit changes to SVN.

For more information, about the script please refer to the designbugreport.py file and the /read_mes/designbugreport_readme.txt file from the following link:

svn:https://mpsvn.medhokapps.com/cps/CPS/_Sandbox/ThomasF/MyScripts

