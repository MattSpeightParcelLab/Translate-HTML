from HTMLParser import HTMLParser
import translate as trans
import re

words = list()
lang = raw_input("Lang: ")



voidList = ['\n','\n\n','\n\n\n', ' ','  ','   ']

# create a subclass and override the handler methods
class HTMLParser(HTMLParser):

    def handle_data(self, data):
        proceessedText =  checks(data)
        print(proceessedText)

        #translation = trans.translate(, lang)
        
        try:
            if proceessedText.find('\n') == -1:
                translation = trans.translate(proceessedText, lang)
                words.append((data,translation))

        except:
            return None

# instantiate the parser and fed it some HTML
parser = HTMLParser()

def changeWord(text):
    for word in words: 
        text = text.replace(word[0], word[1])
    return text


def parse(text):
    
    parser.feed(text)
    print(words)
    text = changeWord(text)
    return text

def processText(sep):

    for x in range(len(sep)):
                if re.match("\n*", sep[x], re.MULTILINE) or re.match("\b*", sep[x], re.MULTILINE):
                    sep[x] = ' '
                    print("hit")

    text = "  ".join(sep)

    return text

def checks(data):
    on = True

    for i in range(10):
        sep = data.split(' ')
        proceessedText =  processText(sep)

       
    return proceessedText