# Import packages
import os

# Define path of files to be renamed
path = "data/"

# List and rename files
filenames = os.listdir(path)
for dir, subdir, listfilename in os.walk(path):
    for filename in listfilename:
        if str(dir) != "data/":
            # Create new filename
            daynum = str(dir).split("/input")[1]
            new_filename = "day" + daynum + filename.replace("input", "")

            # Copy files
            src = os.path.join(dir, filename)  # NOTE CHANGE HERE
            dst = os.path.join(path, new_filename)  # AND HERE
            os.rename(src, dst)
