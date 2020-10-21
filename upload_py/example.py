from upload_py import *
import os

#anonfiles
print("Anonfiles:")
file = anonfiles()
file.upload(f"{os.getcwd()}/file.txt")
file.url_short()
file.url_full()
file.metadata()
print("")

#anonfiles
print("bayfiles:")
file = bayfiles()
file.upload(f"{os.getcwd()}/file.txt")
file.url_short()
file.url_full()
file.metadata()
print("")

#starfiles
print("starfiles:")
file2 = starfiles()
file2.upload(f"{os.getcwd()}/file.txt")
file2.url_file()
file2.url_file_direct()
file2.url_ipa_install()
file2.metadata()
print("")

#FilePipe
print("FilePipe:")
file3 = filepipe()
file3.upload(f"{os.getcwd()}/file.txt")
file3.url_file()
print("")

#FilePipe
print("File.io:")
file3 = fileio()
file3.upload(f"{os.getcwd()}/file.txt")
file3.url_file()
