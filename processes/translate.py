import requests as req
import json



count = 1

def translate(text,lang):
    return "Changed"#api1(text, lang)


def api1(text, lang):
    if len(text) < 100 or text != " " or text == '\n' or text == '':
        r = req.get("https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20200217T182614Z.4fee611f6112d7b9.801c7cbd6ca2193303bd4c8a363e6753da4c2583&text="+text+"&lang="+lang)
 
        if r.status_code == 200:
            translatedText = r.json()["text"][0]
            return translatedText
        else:
            print("ERROR - " + str(r.status_code))


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