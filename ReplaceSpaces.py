
import os

# for exp in range(1,26):

filenames = os.listdir('0_Images/FireExperiments/Two_Story/')

print (filenames)

path = '0_Images/FireExperiments/Two_Story/'

for filename in filenames:
	 os.rename(os.path.join(path, filename), os.path.join(path, filename.replace(' ', '_')))
