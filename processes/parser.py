from HTMLParser import HTMLParser
import translate as trans
import re



words = list()

langCurrent = raw_input("Current Lang: ")
lang = raw_input("Translate to Lang: ")
words.append(("="+langCurrent,"="+lang))


voidList = ['\n','\n\n','\n\n\n', ' ','  ','   ']

class HTMLParser(HTMLParser):

    def handle_data(self, data):
        proceessedText =  checks(data)

        try:
                translation = trans.translate(proceessedText, lang).encode('utf-8').strip()
                words.append((data.strip(),translation))

        except:
            #print("ERROR")
            return None

parser = HTMLParser()

def changeWord(text):
    for word in words: 
        text = text.replace(word[0], word[1])
    return text


def parse(text):
    
    parser.feed(text)
    #print(words)
    text = changeWord(text)
    return text

def processText(sep):

    for x in range(len(sep)):
                if re.match("\n", sep[x], re.MULTILINE) or re.match("\b", sep[x], re.MULTILINE):
                    sep[x] = ''
                    #print("hit")

    text = "  ".join(sep)

    return text

def checks(data):
    on = True

    for i in range(10):
        sep = data.split(' ')
        proceessedText =  processText(sep)

       
    return proceessedText