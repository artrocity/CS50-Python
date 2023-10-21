import sys
import os
import PIL
from PIL import Image, ImageOps

def main():
    check_arg(sys.argv)
    check_file_extension(sys.argv[1], sys.argv[2])
    input_img = sys.argv[1]
    output_img = sys.argv[2]
    put_shirt_on(input_img, output_img)

#Check sys.argv for CLI - Expect 2 CLI [1] to open, [2] to write
def check_arg(args):
    #If not 2 CLI, exit
    if len(args) < 3:
        sys.exit("Too few command-line arguments")
    elif len(args) > 3:
        sys.exit("Too many command-line arguments")

#Function to check file extensions
def check_file_extension(input_img, output_img):
    #Annotate the valid extensions
    valid_extensions = [".jpg", ".jpeg", ".png"]

    #Split the file name and store the extension in a variable
    input_extension = os.path.splitext(input_img)[-1]
    output_extension = os.path.splitext(output_img)[-1]

    #Ensure that extension must be img file(.jpg, .jpeg, .png)
    if input_extension.lower() not in valid_extensions or output_extension.lower() not in valid_extensions:
        sys.exit("Invalid File Extension")
    #Verify input and output extensions match
    if input_extension.lower() != output_extension.lower():
        sys.exit("Input and Output have different extensions")

def put_shirt_on(input_img, output_img):
    try:
        #Open input with Image.open
        with Image.open(input_img) as img:
            #Resize and crop with ImageOps.fit (600x600px)
            img = ImageOps.fit(img, size=(600,600))
            #Open Shirt with Image.Open
            shirt = Image.open("shirt.png")
            #Overlay the shirt with Image.paste
            img.paste(shirt, (0,0), shirt)
            #Save Image with image.save
            img.save(output_img)
    except FileNotFoundError:
        sys.exit("File not Found")

if __name__ == "__main__":
    main()