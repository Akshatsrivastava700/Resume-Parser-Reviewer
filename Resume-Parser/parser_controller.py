import fetch_prog_lang as prol
import sentiment_ratio as sr
import spell_check as sc
import clean_data as cl
import fitz
import subjects as sub
import Grade as gd
import Result as rl
import os
def controller(src_file):
    doc=fitz.open("E:/xampp/htdocs/Parser/Files/"+src_file+".pdf")
    page = doc[0]
    string=page.getText("text")
    cl_string=cl.clean(string,0)
    if cl_string=="Error Generated":
        exit(0)  
    #print(string)
    doc.close()
    sc.spell(src_file,cl_string)
    #print("Spell check completed")
    sr.ratio(src_file,string)
    #print("Sentiment Completed")
    sub.subject_of_interest(src_file,string)
    #print("Subject of Intrest Found")
    prol.pro_lang(src_file,string)
    #print("Programming languages found")
    gd.grade(src_file)
    #print("Grade Given")
    rl.result(src_file)
    #print("Result Found")

