import os

#Read the lines of the widderShins generated file
with open (r"C:/Users/rminana/Desktop/OdecAutoAPIDoc/widdershins/widdershins.md",'r') as file:
        lines = file.readlines()
#Create the file where are written the lines before the pattern matches
keepContent= True
with open(r"C:/Users/rminana/Desktop/OdecAutoAPIDoc/widdershins/headder.md",'w') as file:
   for line in lines:
        if (keepContent==True):
            if("-->" in line ):
                keepContent=False
            else:
              file.write(line) 
#Create the file where are written the lines after the pattern matches
onCopy = False
with open (r"C:/Users/rminana/Desktop/OdecAutoAPIDoc/widdershins/body.md",'w') as file:
    for line in lines:
        if (onCopy == True):
            file.write(line)
        if ("-->" in line):
            onCopy=True
#For last, we create antoher file to concatenate all the files generated in the propper
with open (r"C:/Users/rminana/Desktop/OdecAutoAPIDoc/widdershins/index.html.md",'w') as index:
    with open (r"C:/Users/rminana/Desktop/OdecAutoAPIDoc/widdershins/headder.md",'r') as headder:
        headderLines = headder.readlines()
        for line in headderLines:
            index.write(line)
    with open (r"C:/Users/rminana/Desktop/OdecAutoAPIDoc/textSources/literatura.md",'r') as lit:
        litLines = lit.readlines()
        for line in litLines:
            index.write(line)
    with open (r"C:/Users/rminana/Desktop/OdecAutoAPIDoc/widdershins/body.md",'r') as body:
        bodyLines = body.readlines()
        for line in bodyLines:
            index.write(line)
#Remove the two other files (NOT WORKING) 

try:
    os.system('cmd /k "del headder.md"')
except:
    print ('not executed')
