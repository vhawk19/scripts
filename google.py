import sys, os
usage = "To search on Google , enter the following Command python google.py [your search term] "
if len(sys.argv) <2:
     print(usage)
     sys.exit(0)
filename = sys.argv[1].split("\\")[-1]
filenames = filename.split('.')[0]
file = filenames.split()
total_name = ''
for word in file:
     if word == file[-1]:
          total_name+=word
     else:
          total_name+= word + '+'
link = "http://www.google.com/search?q="
os.system("start " + link + total_name)
