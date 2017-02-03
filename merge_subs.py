import sys # Used to read commmand line arguements
import os # Used to check file

# Check the file is good and return it in a list
def loadSrt(filename):
	if os.path.exists(filename):
		with open(filename, 'r') as f:
			try:
				# Load the srt file into a list
				return f.readlines()
				
			except:
				# Can't read the file
				print("Unable to read file" + filename)
				
	else:
		# Can't open the file
		print("Unable to open file " + filename + ".  Check the file and path.")
		exit()
		
if len(sys.argv) != 3:
	print("Usage: python3 merge_subs.py <language 1 srt file> <language 2 srt file>")
	print("Example: python3 merge_subs.py program_subs_EN.srt program_subs_CN.srt\n")
	print("(Different language srt files should be based unpon the same source to avoid synch issues)")
	exit()

# Load the subtitles of the first language
lang_1_list = loadSrt(sys.argv[1])
lang_2_list = loadSrt(sys.argv[2])

# Create empty list for the output
merged_list = []

# Loop through the lines in the file, adding just subtitles from lang_2
for index in range(len(lang_1_list)):
	
	merged_list.append(lang_1_list[index])
	line = lang_1_list[index].strip("\n")
	
	print(line)
	
	if line.isdigit():
		# This identifies the subtitle number
		# Already exists from lang_1
		pass
		
	elif line.count(":") == 4:
		# This identifies the duration, e.g. 00:01:20,000 --> 00:01:32,000
		# Already exists from lang_1
		pass
		
	elif len(line) == 0:
		# This identifies the empty lines
		# Already exists from lang_1
		pass
		
	else:
		# This must be the subtitle in lang_2 language
		print(lang_2_list[index].strip("\n"))
		merged_list.append(lang_2_list[index])

# Open the output file for writing
merged_srt = open("MERGED_" + sys.argv[1],"w")

# Write merged array and close the file
for srt in merged_list:
    merged_srt.write(srt)

merged_srt.close()