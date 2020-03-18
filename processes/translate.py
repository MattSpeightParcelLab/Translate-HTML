import requests as req
import json
import re



count = 1

def translate(text,lang):
    return api1(text, lang)


def api1(text, lang):
    if len(text) < 100 or text != " " or text != '\n' or text == '':
        r = req.get("https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20200217T182614Z.4fee611f6112d7b9.801c7cbd6ca2193303bd4c8a363e6753da4c2583&text="+text+"&lang="+lang)
 
        if r.status_code == 200:
            translatedText = r.json()["text"][0]
            
            return translatedText
        else:
            #print("ERROR - " + str(r.status_code))
            return None


def api2(text):
    if len(text) < 100 or text != " " or text == '\n' or text == '':
        url = "https://translator.p.rapidapi.com/api/translate"

        payload = "input="+text+"&target="+lang
        headers = {
            'x-rapidapi-host': "translator.p.rapidapi.com",
            'x-rapidapi-key': "0a5aeb3651msh57de14699d83346p11380bjsn7db0b8421ad4",
            'content-type': "application/x-www-form-urlencoded"
    }

        r = req.request("POST", url, data=payload, headers=headers)
        
        if r.status_code == 200:
            translatedText = r.json()["output"]
            return translatedText
        else:
            print("ERROR - " + str(r.status_code))

def deeplScrapper(text, startlang, endlang):
    r = req.get("https://www.deepl.com/translator#"+startlang+"/"+endlang+"/"+text)
    text = find(search(r.text.splitlines(), 'dictLink'), [">", "<"])
    print(text)







###############################################
############### DEEPL FUNCTIONS ###############
###############################################


# Search
def search(txt, searchvar):
    for line in txt:
        if re.search(searchvar, line, re.I):
            return line

# Find a value between two chars - first result
def find(txt, var):
    text = ""

    arr = list(txt)

    count = 0

    for a in arr:
        if a == var[0]:
            arr = arr[count + 1:len(arr) - 1]
            break
        count += 1

    count = 0

    for a in arr:
        if a == var[1]:
            arr = arr[0:count]
            break
        count += 1

    text = ''.join(arr)

    print(text)
    return text