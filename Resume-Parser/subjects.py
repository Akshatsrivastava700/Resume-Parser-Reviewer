import re
import os
import fitz
import clean_data as cl
def subject_of_interest(src_file,string):
    try:
        os.remove(src_file+"_sub"+".txt")
        f = open(src_file+"_sub"+".txt", "a")
    except:
        f = open(src_file+"_sub"+".txt", "a")
    sub=['data structure','dbms','networking','software engineering']
    string=cl.clean(string,0)
    string=string.lower()
    string = string.replace("\n","")
    #print(string)
    pos=int(0)
    for x in sub:
        if string.find(x)!=-1:
            f.write(x.upper())
            f.write("\n")
        pos+=1
    f.close()
