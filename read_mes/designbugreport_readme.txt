- python 3.7
- pip install xlwings
- change the "default" variable to be the path of the folder that contains the folders for company-specific bug reports
- will not work correctly if there are more than 26 columns

Steps for using this script
1. Export the issue report from excel with the correct three-letter company label and the following columns included:
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

2. Save the export as an .xlsx file in your company-specific default folder:
	Ex.
	default is C:\WebTesting_Jira\Reports
	company-specific default is C:\WebTesting_Jira\Reports\KPC

3. Update your company-specific default folder from SVN (subversion)

4. Rename your reports in the following way:
    NEW_[COMPANY NAME]_BUG_REPORT_09_03_2020
    OLD_[same as above, just put the "OLD" as the first word]
    Putting the New and Old in front will be important.

5. Run the script: designbugreport.py

6. Commit changes to SVN.


Instructions for BRMs

1. Please checkout the company-specific folder from SVN.
	In this case they will be located in the following location in SVN:
	svn:https://mpsvn.medhokapps.com/cps/CPS/_Sandbox/ThomasF/WebTesting_Jira/Reports/KPC

2. If the BRM wants to make changes do the following:
	a. Update from SVN.
	b. Make changes to the "Status" column only.
	c. Commit changes to SVN.