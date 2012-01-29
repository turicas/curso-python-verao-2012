#-*- coding: utf-8 -*-
def r13(char):
   
    if (char >= 'a' and char <= 'z') or (
        char >= 'A' and char <= 'Z'):
       if char.isupper() == False:
           if ord(char) + 13 > ord('z'):
               return chr(ord(char) - 13)
           else:
               return chr(ord(char) + 13)
       else:
           if ord(char) + 13 > ord('Z'):
               return chr(ord(char) - 13)
           else:
               return chr(ord(char) + 13)  
    else:
        return char

def palavra(texto):
    novotexto = ""
    for char in texto:
        novotexto += r13(char)
    return novotexto
    
    
       
        
