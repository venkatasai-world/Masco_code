#Morse code conversion
import csv

user_input=input("Enter a Word:").upper()
out=""
dicto={}



try:
    with open('morse_code_symbols.csv','r', encoding="cp1252") as file:
        reader = csv.DictReader(file)
        for row in reader:
            dicto[row['Character']]=row['Morse_Code']
    
    for ch in user_input:
        if ch==" ":
            out += " /  " 
        elif ch in dicto:
            out+=dicto[ch]+" "
        else:
            out+="? "


                

finally:
    file.close()


print("Morse Code is:",out)
