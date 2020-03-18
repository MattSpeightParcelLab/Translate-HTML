**HOW TO GUIDE**

################ PARCELLAB USAGE ################

1.  "CURRENT LANG" -> (ISO 3166-1 alpha-2 code) THIS IS USED TO CHANGE THE LANG IN THE TRACKING LINK (CAN BE LEFT EMPTY)
     `lang=de`
2.  "TRANSLATE TO LANG" -> (NEEDED) (ISO 3166-1 alpha-2 code) -> THIS WILL BE THE FINAL TRANSLATED LANGUAGE
3.  "FILENAME" -> (NEEDED) -> THIS IS THE FILENAME OF ANY FILE IN THE "/INPUTS" FOLDER (NOTE: NO NEED FOR THE .HTML)

################ NONE PARCELLAB ##################

1.  "CURRENT LANG" -> (CAN BE LEFT EMPTY) (ISO 3166-1 alpha-2 code) -> API WILL AUTO DETECT THE LANG
2.  "TRANSLATE TO LANG" -> (NEEDED) (ISO 3166-1 alpha-2 code) -> THIS WILL BE THE FINAL TRANSLATED LANGUAGE
3.  "FILENAME" -> (NEEDED) -> THIS IS THE FILENAME OF ANY FILE IN THE "/INPUTS" FOLDER (NOTE: NO NEED FOR THE .HTML


| Language| Code           
| --------|:-----:
| English | en
| French  | fr      
| Spanish | es      


################ NORMAL USAGE ################
```
> ./translate.sh

---------------------------------------------
---------- ♨️ Translate HTML FILE ♨️ ----------
---------------------------------------------
Current Lang: en
Translate to Lang: fr
Filename: index
--------- Translation Compleate ✅ ----------
```
THE CODE WILL THEN LOAD IN VSCODE. (OUTPUT WILL BE DISPLAYED AND SAVED IN "/OUTPUT" FOLDER AS "OUT.HTML".)
