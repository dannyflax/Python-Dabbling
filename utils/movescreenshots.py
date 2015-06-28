from os import listdir
from os.path import isfile, join
from shutil import move

def main():
	mypath = '/Users/dannyflax/Desktop'
	newpath = '/Users/dannyflax/Documents/Important Media/Simulator Screenshots'

	onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
	for file in onlyfiles:
		if file.startswith('iOS Simulator'):
			move(mypath+'/'+file,newpath+'/'+file)
    

if __name__ == "__main__":
    main()