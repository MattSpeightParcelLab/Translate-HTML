import processes.parser as parser

def loadFile(filename):
    file = open(filename, "r")
    return file.read()

def wrtieTransHTML(text, filename):
    file = open("output/"+filename+".html", "w+")
    file.write(text)
    file.close() 

filename = str("bose")#raw_input("Filename: "))


filetext = parser.parse(loadFile("input/"+filename+".html"))
#print(filetext)
wrtieTransHTML(filetext, raw_input("Document Name: "))
#print(trans.translate("Car","fr"))
