import random


def function():
    f = open("data/occupations.csv","r") #opens file with name of "test.txt"
    string = f.read()
    f.close
    d={}
    quoteCount = 0
    character = 0
    while character<len(string):
        key = ""
        value = ""
        isValue = False
        while character<len(string) and (string[character]!="\n"):
            if (string[character]=='"'):
                quoteCount+=1
            if string[character]!='"' and string[character]!=",":
                if isValue:
                    value+=string[character]
                else:
                    key+=string[character]
                #print (string[character]+ " "+str(character)+str(isValue))
            elif string[character]==",":
                if quoteCount%2==0:
                    isValue=True
                else:
                    key+=string[character]
                #print (string[character]+str(character)+str(isValue))
            character+=1
        try:
            d[key]=float(value)   
        except ValueError:
            print ""         
        character+=1
    del d["Total"] 
    return d  

d=function()

def randomJob():
    x=random.randint(0,999)
    y=0
    for key in d:
        if x>=y and x<d[key]*10+y:
            return key
        else:
            y+=d[key]*10

if __name__=="__main__":
    print function()