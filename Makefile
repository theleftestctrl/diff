compilefile = diff.cpp
compiledoc = diff
picfile = pic.py
textfile = func.txt
logfile = log.txt
pythonvar = load_data_from_folder('.')('func.txt')[:,

all: compile run getpicture

compile:
	g++ -o $(compiledoc)  $(compilefile)
run:
	./$(compiledoc) 1> $(textfile) 2> $(logfile)
getpicture:
	python3 $(picfile) $(pythonvar)0] $(pythonvar)1] $(pythonvar)2] 

