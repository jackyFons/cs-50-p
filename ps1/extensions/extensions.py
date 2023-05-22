# Gets case-insensitive input w/o spaces
file = input("File name: ").lower().strip()

# finds index of .
index = file.rfind(".")

# File extension exists
if index != -1:
    ext = file[index+1:]
    if ext == "jpeg" or ext == "jpg":
        print("image/jpeg")
    elif ext == "gif":
        print("image/gif")
    elif ext == "png":
         print("image/png")
    elif ext == "pdf":
        print("application/pdf")
    elif ext == "txt":
        print("text/plain")
    elif ext == "zip":
        print("application/zip")
    else:
        print("application/octet-stream")
# File extension DNE
else:
    print("application/octet-stream")