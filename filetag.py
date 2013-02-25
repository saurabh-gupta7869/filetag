import glob, os

def rename(dir, pattern, titlePattern):
    for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        #title=title[:-8]  #for removing previous tag appended to end of title and is of length 8  i.e  %s[kukasa]  --> %s
        #title=title[8:]   #for removing previous tag appended to front of title and is of length 8  i.e  [kukasa]%s --> %s
        print titlePattern % title
        os.rename(pathAndFilename, 
                  os.path.join(dir, titlePattern % title + ext))

rename(r'dir',r'*.extension',r'[tag1]%s[tag2]') #when want to delete tag then remove [tag1] and [tag2]



# EXAMPLE:-
# rename(r'C:\Users\saurabh gupta\Desktop\...\videosongs', r'*.wmv', r'[kukasa]%s')
# so runaway.wmv becomes [kukasa]runaway.wmv 
