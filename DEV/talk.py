import subprocess

phrase = str(raw_input("Type a phrase:"))

print(phrase)

#subprocess.call("./speak.sh", phrase)

subprocess.call(["./try.sh", '""' + phrase + '""'])

print("end")
