
import os
# the set path for where the images are located 
dirPath =''
# where the new yml file will be created
outputPath =''
# the correct spacing for different levels of indentation in yaml file
lvlOneIndent = "   "
lvlTwoIndent = "      "
lvlThreeIndent = "        "

# album name (folder name)
albumTitle = " - title: "
# the folder that has images for a spicfic album
imgAlbum = "album: "
# this will have the dir for the image
imgLink = "- image: "
# image description
imgDesc = "description: "

preRoot = ""
# opens output file
f = open(outputPath,"a") 

files = os.listdir(dirPath)
#loops over all folders in dirPath
for root, dirs, files in os.walk(dirPath, topdown=False):
        # loops over each file in folder
        for file in files:
                # checks if root is the same as preRoot 
                if root != preRoot:
                        # writes information to file
                        f.write("\n" + lvlOneIndent + albumTitle)
                        f.write("\n" + lvlTwoIndent + imgAlbum)
                preRoot = root
                  # writes information to file
                f.write("\n" + lvlTwoIndent + imgLink + os.path.join(name))
                f.write("\n" + lvlThreeIndent + imgDesc)
# closes open file
f.close()
    
