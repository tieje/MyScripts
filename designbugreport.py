import os
import xlwings as xw

class DesignBugReport:
	def __init__(self, default):
		self.default = default
		self.prompt = '>'
	def controlla(self):
		folder_finder()
		excel_finder()
	def folder_finder(self):
		for i in os.listdir():
			print(i)
		print("In which folder would you like to design the bug report?")
		self.working_dir = input(self.prompt)
		os.chdir(os.path.join(self.default,self.working_dir))
	def excel_finder(self):
		xw.sheets
	def design_excel(self):
		# Delete the first three rows
		sht.range('1:3').api.Delete(DeleteShiftDirection.xlShiftToLeft)
		# going down first
		# counterA find the row that contains MPCORE-167
		counterA = 1
		# counterB finds number of filled rows
		counterB = 1
		cut_off = 'MPCORE-167'
		trigger = True
		cell_value = sht.range('A2').value
		while bool(cell_value) != False:
			if trigger:
				if cell_value == cut_off:
					trigger = False
				status_checker(counterA)
				counterA += 1
			counterB += 1
			cell_value = sht.range('A'+counterB).value
		# Delete the rows under MPCORE-167
		sht.range(counter':'self.rows).api.Delete(DeleteShiftDirection.xlShiftToLeft)
		# Change column names
		cell_value = sht.range('A1').value
		counter = 1
# TODO: Build the status_checker that will highlight the entire row to be the color corresponding to status.
	def status_checker(self):


if __name__ == "__main__":
	default = r"C:\WebTesting_Jira\Reports"
	#TODO: I'll need to confirm with the user to determine which is the new bug report and which is the old bug report
	#TODO: Ask the user if the current default location correct, print out the default. If not then it will ask the user to change the default path variable
	DesignBugReport(default)

"""
testing below
"""
import xlwings as xw
from xlwings.constants import DeleteShiftDirection

app = xw.App()
wb = app.books.open('name.xlsx')
sht = wb.sheets['Sheet1']

# Delete row 2
sht.range('2:2').api.Delete(DeleteShiftDirection.xlShiftUp) 

# Delete row 2, 3 and 4 
sht.range('2:4').api.Delete(DeleteShiftDirection.xlShiftUp) 

# Delete Column A
sht.range('A:A').api.Delete(DeleteShiftDirection.xlShiftToLeft)

# Delete Column A, B and C
sht.range('A:C').api.Delete(DeleteShiftDirection.xlShiftToLeft)

wb.save()
app.kill()