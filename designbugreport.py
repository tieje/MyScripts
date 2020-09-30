import os
import xlwings as xw
from xlwings.constants import DeleteShiftDirection

class DesignBugReport:
    def __init__(self, default):
        self.default = default
        self.copy_counter = 0
        self.normal_statuses = ['Backlog',
            'Requirements',
            'Selected for Development',
            'In Progress',
            'Code Review',
            'Ready for Test',
            'Testing',
            'Demo',
            'Done']
    def controlla(self):
        self.excel_finder()
        self.design_excel()
        print('Completed')
        return None
    def excel_finder(self):
        os.chdir(default)
        for i in os.listdir():
            print(i)
        print("In which folder would you like to design the bug report?")
        self.working_dir = os.path.join(self.default,input(prompt))
        os.chdir(self.working_dir)
        dir_list = os.listdir()
        for x in dir_list:
            if 'old' in x.lower():
                self.copy_book = xw.Book(x)
            elif 'new' in x.lower():
                self.work_book = xw.Book(x)
        self.sht = self.work_book.sheets[0]
        self.copy_sht = self.copy_book = self.copy_book.sheets[0]
        return None
    def design_excel(self):
        # Delete the first three rows
        if self.sht.range('A1').value != 'Key':
            self.sht.range('1:3').api.Delete(DeleteShiftDirection.xlShiftToLeft)
        # go across first to establish labels for columns
        i = 65
        cell_value = self.sht.range(chr(i)+'1').value
        while bool(cell_value):
            if cell_value.lower() == 'status':
                self.status_col = chr(i)
            if cell_value == 'External Tracking #':
                self.sht.range(chr(i)+'1').value = 'External Tracking # (for client use)'
            if cell_value.lower() == 'resolution':
                self.resolution_col = chr(i)
            i += 1
            cell_value = self.sht.range(chr(i)+'1').value
        self.right_limit=chr(i)
        # checking for status column of old excel sheet
        d = 65
        cell_value = self.copy_sht.range(chr(d)+'1').value
        while bool(cell_value):
            if cell_value.lower() == 'status':
                self.old_status_col = chr(d)
            d += 1
            cell_value = self.copy_sht.range(chr(d)+'1').value
        self.old_right_limit=chr(d)
        # going down second
        # counterA find the row that contains MPCORE-167
        counterA = 1
        # counterB finds number of filled rows
        counterB = 1
        # custom cut off from old bugs. Copy and paste
        if any(['kpc' in i.lower() for i in os.listdir()]):
            self.cut_off = 'MPCORE-167'
        elif any(['aet' in i.lower() for i in os.listdir()]):
            self.cut_off = 'MPCORE-166'
        trigger = True
        cell_value = self.sht.range('A2').value
        while bool(cell_value) != False:
            if trigger:
                if cell_value == self.cut_off:
                    trigger = False
                self.status_checker(str(counterA))
                counterA += 1
            counterB += 1
            cell_value = self.sht.range('A'+str(counterB)).value
        # Delete the rows under MPCORE-167
        self.sht.range(str(counterA)+':'+str(counterB)).api.Delete(DeleteShiftDirection.xlShiftToLeft)
        # copy status from old excel
        cell_value = self.sht.range('A2').value
        counterA = 1
        self.contingent_error_counter = 1
        while bool(cell_value):
            self.contingent_error_counter += 1
            self.copy_excel(counterA)
            counterA += 1
            cell_value = self.sht.range('A'+str(counterA)).value
        return None
    def status_checker(self, row_n):
        cell_val = self.sht.range(self.status_col+row_n).value
        if cell_val == 'Requirements':
            # Blue color is RGB of 55,70,150 respectively
            self.sht.range('A'+row_n+':'+self.right_limit+row_n).color = (135,206,235)
        elif cell_val.lower() == 'in progress':
            # yellow color is RGB of 255,220,50
            self.sht.range('A'+row_n+':'+self.right_limit+row_n).color = (255,220,50)
        elif cell_val.lower() == 'done':
            if self.sht.range(self.resolution_col+row_n).value.lower() == 'cannot reproduce':
                # change it to yellow and ask for client attention
                self.sht.range('A'+row_n+':'+self.right_limit+row_n).color = (255,220,50)
                self.sht.range(self.resolution_col+row_n).value = 'Cannot reproduce, needs client attention.'
            else:
                self.sht.range('A'+row_n+':'+self.right_limit+row_n).color = (124,252,0)
        return None
    def copy_excel(self, row_n):
        while self.copy_sht.range('A'+str(row_n)).value != self.sht.range('A'+str(row_n+self.copy_counter)).value and bool(self.copy_sht.range('A'+str(row_n)).value):
            self.copy_counter += 1
            if self.copy_counter >= 200:
                print('Press Ctrl + C to stop this script. There is a mismatching bug around row ' + str(self.contingent_error_counter) + '. Compare with the old report and look at Label column to see if you exported the correct report.')
        if self.copy_sht.range(self.old_status_col+str(row_n)).value not in self.normal_statuses:
            self.sht.range(self.status_col+str(row_n+self.copy_counter)).value = self.copy_sht.range(self.old_status_col+str(row_n)).value
        return None

if __name__ == "__main__":
    default = r"C:\Jira_Reports"
    prompt = '>'
    print("Is the following the correct default path? If yes, then press enter. If not, then press Ctrl + C to cancel the script and go change the default.")
    print(default)
    response = input(prompt)
    if bool(response) == False:
        pass
    DesignBugReport(default).controlla()