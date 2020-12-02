import os
import xml.etree.ElementTree as ET
def find_pos(string):
    temp = string.split(",")
    for x in temp:
        if x=="pos:1":
            return(100)
    return(0)
def find_neg(string):
    temp = string.split(",")
    for x in temp:
        if x=="neg:1": 
            return(100)
    return(0)
def find_nlt(string):
    temp = string.split(",")
    for x in temp:
        if x=="mid:1": 
            return(100)
    return(0)
def calc_value(pos_val,neg_val,ntl_val,l,src_file):
    positive=pos_val/l
    negative=neg_val/l
    ntl=ntl_val/l
    try:
        os.remove(src_file+"_sent_ext.xml")
        data = ET.Element('DATA')  
        items = ET.SubElement(data, 'Values')    
        item1 = ET.SubElement(items, 'POSITIVE')
        item2 = ET.SubElement(items, 'NEGATIVE')
        item3 = ET.SubElement(items, 'NEUTRAL')
        item1.text = str(positive) 
        item2.text = str(negative)
        item3.text = str(ntl)
        # create a new XML file with the results
        mydata = ET.tostring(data)  
        myfile = open(src_file+"_sent_ext.xml", "w")  
        myfile.write(mydata)
        myfile.close()
    except:
        data = ET.Element('DATA')  
        items = ET.SubElement(data, 'Values')    
        item1 = ET.SubElement(items, 'POSITIVE')
        item2 = ET.SubElement(items, 'NEGATIVE')
        item3 = ET.SubElement(items, 'NEUTRAL')
        item1.text = str(positive) 
        item2.text = str(negative)
        item3.text = str(ntl)
        # create a new XML file with the results
        mydata = ET.tostring(data)  
        myfile = open(src_file+"_sent_ext.xml", "w")  
        myfile.write(mydata)
        myfile.close()
def extract(src_file):
    pos_val=int(0)
    neg_val=int(0)
    ntl_val=int(0)
    temp=int(0)
    f = open(src_file+"_sentiment"+".txt", "r")
    string=f.read()
    f.close()
    os.remove(src_file+"_sentiment.txt")
    string = string.replace("{", "")
    string = string.replace('"', "")
    l=string.split("\n")
    for x in l:
        temp=find_pos(x)
        if temp!=0:
            pos_val+=temp
            temp=int(0)
            pass
        temp=find_neg(x)
        if temp!=0:
            neg_val+=temp
            temp=int(0)
            pass
        temp=find_nlt(x)
        if temp!=0:
            ntl_val+=temp
            temp=int(0)
    calc_value(pos_val,neg_val,ntl_val,len(l),src_file)

