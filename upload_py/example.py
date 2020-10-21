from upload_py import *
import os

#anonfiles
print("Anonfiles:")
file = anonfiles()
file.upload(f"{os.getcwd()}/file.txt")
print(file.url_short())
print(file.url_full())
print(file.metadata())
print("")

#anonfiles
print("bayfiles:")
file = bayfiles()
file.upload(f"{os.getcwd()}/file.txt")
print(file.url_short())
print(file.url_full())
print(file.metadata())
print("")

#starfiles
print("starfiles:")
file2 = starfiles()
file2.upload(f"{os.getcwd()}/file.txt")
print(file2.url_file())
print(file2.url_file_direct())
print(file2.url_ipa_install())
print(file2.metadata())
print("")

#FilePipe
print("FilePipe:")
file3 = filepipe()
file3.upload(f"{os.getcwd()}/file.txt")
print(file3.dl_url())
print("")

#FilePipe
print("File.io:")
file3 = fileio()
file3.upload(f"{os.getcwd()}/file.txt")
print(file3.dl_url())
