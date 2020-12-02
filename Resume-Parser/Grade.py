import os
import xml.etree.ElementTree as ET
def open_file(src_file):
    f=open(src_file)
    string=f.read()
    f.close()
    return(string)
def grade(src_file):
    grade=int(100)
    temp=open_file(src_file+"_spell_ext.txt")
    l=temp.split("\n")
    del(l[-1])
    grade=grade-len(l)
    temp=open_file(src_file+"_sub.txt")
    temp=temp.lower()
    sub=['data structure','dbms','networking','software engineering']
    for x in sub:
        if temp.find(x)==-1:
            grade-=2
    sent_val=[]
    tree = ET.parse(src_file+'_sent_ext.xml')  
    root = tree.getroot()
    for elem in root:  
        for subelem in elem:
            sent_val.append(int(subelem.text))
    if int(sent_val[0])-int(sent_val[1])<=0:
        grade-=5
    if int(int(sent_val[0])-int(sent_val[2])<=0):
        grade-=2
    del(sent_val)
    lang=['c','python','go','html','java']
    lang_marks=['5','4','3','2','5']
    temp=open_file(src_file+"_pro_lang.txt")
    temp=temp.lower()
    i=int(0)
    for x in lang:
        if temp.find(x)==-1:
            grade-=lang_marks[i]
        i+=1
    sub=['data structure','dbms','networking','software engineering']
    for x in sub:
        if temp.find(x)==-1:
            grade-=6
    del(sub)
    try:
        os.remove(src_file+"_grade.txt")
        f=open(src_file+"_grade.txt",'a')
    except:
        f=open(src_file+"_grade.txt",'a')
    if grade>90 and grade<=100:
        f.write("A+")
    elif grade>80 and grade<=90:
        f.write("A")
    elif grade>70 and grade<=80:
        f.write("B+")
    elif grade>60 and grade<=70:
        f.write("B")
    elif grade>50 and grade<=60:
        f.write("C")
    else:
        f.write("D")
    f.close()

