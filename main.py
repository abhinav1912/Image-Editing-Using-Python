# import required classes
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import argparse
from os.path import exists

# define command line flags
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image")
parser.add_argument("-o", "--output")
args = parser.parse_args()

# assign defaults to input and output directory
input_file = None
output_directory = None

# defining the image template path
while True:
    if not args.image:
        input_file = input("Enter the input file path: ")
    else:
        input_file = args.image
    if not exists(input_file):
        print("Input File doesn't exist.")
        args.image = None
        input_file = input("Enter input file path: ")
    else:
        break
print(f"Selected file {input_file} as input.")

# defining the output directory path
while True:
    if not args.output:
        output_directory = input("Enter output directory: ")
    else:
        output_directory = args.output
    if not exists(output_directory):
        print("Invalid output directory.")
        args.output = None
        output_directory = input("Enter output directory: ")
    else:
        break
print(f"Selected {output_directory} as output directory.")


# define the required font
font = ImageFont.truetype('AvenirLTProRoman.otf', size=70)

# define the image width and height
W, H = 1600, 1250

# define the Excel file to load details
df = pd.read_excel(io='Enter your file path')

for i in df["attribute"]:   # define the attribute to be filled in the image
    try:
        image = Image.open(input_file)
        name = "something.png"  # define a name for this particular file, including the extension
        draw = ImageDraw.Draw(image)
        msg = i.upper().strip()
        draw = ImageDraw.Draw(image)
        w, h = draw.textsize(msg, font=font)
        draw.text(((W-w)/2 , 540), msg, font=font, fill="black")
        image.save(output_directory+name)
    except Exception as error:
        print(f"Row: {i} Error: {str(error)}")