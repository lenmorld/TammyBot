import subprocess

phrase = str(input("Type a phrase:"))

#subprocess.call("./speak.sh", phrase)

subprocess.call(["./try.sh", phrase])

print("end")
