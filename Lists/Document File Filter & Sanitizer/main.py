filenames = ["report_v1.test", "data_backup.csv", 'image_01.png', "notes.txt", "archieved_report.txt"]

# using endswith() inside list comprehension - Extract only .txt files
txt_files = [file for file in filenames if file.endswith(".txt")]
print("Text files: ", txt_files)
# using endswith() and replace() in for loop - Rename old '.txt' extension to '.bak'
updated_files = []
for file in filenames:
  if file.endswith(".txt"):
    new_name = file.replace(".txt", ".bak")
    updated_files.append(new_name)
  else:
    updated_files.append(file)

print(updated_files)

for index, file in enumerate(updated_files):
  print(f"[{index} {file}]")
# split() and join() - convert string to list and recombine with delimiters

file_path_str = "system/logs/errors/2026_report.txt"
path_components = file_path_str.split("/")
reconstructed_path = " -> ".join(path_components)

print("n")
