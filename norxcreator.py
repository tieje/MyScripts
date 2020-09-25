# This file is based off of PCUG page 118 v. 14
import os
import pyperclip as pc
class NoRxCreator:
	def __init__(self, dest_dir):
		self.dest_dir = dest_dir
	def createnorxfile(self):
		os.chdir(self.dest_dir)
		file_name = 'NoRxExampleFile.txt'
		new_file = open( file_name,'w')
		self.filespecs()
		new_file.write(
		# Header
		self.file_id_name +
		self.sending_entity +
		self.file_creation_date +
		self.file_control_number +
		self.header_filler +
		"\n" +
		# Detail
		self.record_type +
		self.rec_type_orig_det +
		self.HICN_or_RRB_number +
		self.SSN +
		self.MBI +
		self.detail_filler_1 +
		self.contract_number +
		self.pbp_number +
		self.detail_filler_2 +
		self.file_creation_date +
		self.detail_filler_3 +
		"\n" +
		self.file_id_name_trailer +
		self.sending_entity +
		self.file_creation_date +
		self.trailer_filler_1 +
		self.file_record_count +
		self.trailer_filler_2
		)
		print("'No Rx File' creation successful!\nThe file path has been copied to your clipboard.")
		pc.copy(self.dest_dir)
		return None
	def filespecs(self):
		# Header
		self.file_id_name = "CMSNRX0H"
		self.sending_entity = "MBD" + 5 * " "
		self.file_creation_date = "20200617"
		self.file_control_number = 9 * " "
		self.header_filler = 717 * " "
		# Detail Record
		self.record_type = "NRX"
		self.rec_type_orig_det = 5 * " "
		self.HICN_or_RRB_number = "000237     "
		self.SSN = "362291448"
		self.MBI = "00023742959"
		self.detail_filler_1 = 49 * " "
		self.contract_number = "H5262"
		self.pbp_number = "001"
		self.detail_filler_2 = 71 * " "
		self.detail_filler_3 = 574 * " "
		# Trailer Record
		self.file_id_name_trailer = "CMSNRX0T"
		self.trailer_filler_1 = 9 * " "
		self.file_record_count = "0000001"
		self.trailer_filler_2 = 710 * " "

if __name__ == "__main__":
	message1 = "Paste and Enter the file destination OR press Enter to use the current working directory."
	prompt = '>'
	print(message1)
	dest_dir = input(prompt)
	if bool(dest_dir) == False:
		dest_dir = os.getcwd()
	NoRxCreator(dest_dir).createnorxfile()