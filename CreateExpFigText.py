import fnmatch
import os
import re

file = open("ExperimentFigures.tex","w")

firstline = '\\begin{figure}[H]\n'
lastline = '\\end{figure}\n'

numbers = re.compile(r'(\d+)')

def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

for exp in range(1,26):

	if exp < 5: 

		x = 0
		figs = 0

		filenames = os.listdir('0_Images/Experiment_Screenshots/Experiment_' + str(exp))

		#file.write('\\Begin{center}\n' + '\\large\n' + '\extbf{Experiment ' + str(exp)+' Data}\n' + '\\end{center}\n\n')
		# file.write('\\clearpage')
		# file.write('\\large\n' + '\extbf{Experiment ' + str(exp)+' Data}\n' + '\n')

		files = sorted(filenames, key=numericalSort)

		file.write(firstline)
		file.write('\setcounter{subfigure}{0} \n')
		file.write('\\centering \n')
		for name in files:	
			if name.replace(' ',' ')[len(name)-4:] == '.jpg':
				figurename = '\\subfloat[]{\includegraphics[height=2in]{0_Images/Experiment_Screenshots/Experiment_' + str(exp) + '/' + name + '}} \\ \n'
				file.write(figurename)
				x = x + 1
				figs = figs + 1
				if x >= 3:
					if figs != len(files) - 1:
						x = 0
						figurecaption = '\caption{Experiment '+ str(exp) +' Images}'
						file.write(figurecaption +'\n')
						file.write('\label{fig:Experiment' +str(exp) + 'ImagesCont' + str(figs/3) + '} \n')
						file.write(lastline + '\n \n')
						file.write(firstline)
						file.write('\ContinuedFloat \n')
						file.write('\centering \n')

		if x > 0:
			figurecaption = '\caption{Experiment '+ str(exp) +' Images}'
			file.write(figurecaption +'\n')
			file.write('\label{fig:Experiment' +str(exp) + 'ImagesCont' + str(figs/3 + 1) + '} \n')
			file.write(lastline)
			file.write('\n')

	if exp > 9: 

		x = 0
		figs = 0

		filenames = os.listdir('0_Images/Experiment_Screenshots/Experiment_' + str(exp))

		#file.write('\\Begin{center}\n' + '\\large\n' + '\extbf{Experiment ' + str(exp)+' Data}\n' + '\\end{center}\n\n')
		# file.write('\\clearpage')
		# file.write('\\large\n' + '\extbf{Experiment ' + str(exp)+' Data}\n' + '\n')

		files = sorted(filenames, key=numericalSort)

		file.write(firstline)
		file.write('\setcounter{subfigure}{0} \n')
		file.write('\\centering \n')
		for name in files:	
			if name.replace(' ',' ')[len(name)-4:] == '.jpg':
				figurename = '\\subfloat[]{\includegraphics[height=2in]{0_Images/Experiment_Screenshots/Experiment_' + str(exp) + '/' + name + '}} \\ \n'
				file.write(figurename)
				x = x + 1
				figs = figs + 1
				if x >= 3:
					if figs != len(files) - 1:
						x = 0
						figurecaption = '\caption{Experiment '+ str(exp) +' Images}'
						file.write(figurecaption +'\n')
						file.write('\label{fig:Experiment' +str(exp) + 'ImagesCont' + str(figs/3) + '} \n')
						file.write(lastline + '\n \n')
						file.write(firstline)
						file.write('\ContinuedFloat \n')
						file.write('\centering \n')

		if x > 0:
			figurecaption = '\caption{Experiment '+ str(exp) +' Images}'
			file.write(figurecaption +'\n')
			file.write('\label{fig:Experiment' +str(exp) + 'ImagesCont' + str(figs/3 + 1) + '} \n')
			file.write(lastline)
			file.write('\n')