#Prompt User for the name of a file
type = input("Filename: ").strip().lower()

#Output file name
#.gif
if type.endswith(".gif"):
    print("image/gif")
#.jpg
elif type.endswith(".jpg"):
    print("image/jpeg")
#.jpeg
elif type.endswith(".jpeg"):
    print("image/jpeg")
#.png
elif type.endswith(".png"):
    print("image/png")
#.pdf
elif type.endswith(".pdf"):
    print("application/pdf")
#.txt
elif type.endswith(".txt"):
    print("text/plain")
#.zip
elif type.endswith(".zip"):
    print("application/zip")
#else
else:
    print("application/octet-stream")