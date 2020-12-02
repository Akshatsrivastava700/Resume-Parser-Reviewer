import re
import os
def pro_lang(src_file,string):
    try:
        os.remove(src_file+"_pro_lang"+".txt")
        f = open(src_file+"_pro_lang"+".txt", "a")
    except:
        f = open(src_file+"_pro_lang"+".txt", "a")
    lang=['c','python','go','html','java']
    lstatus=[0,0,0,0,0,0,0,0,0]
    l=string.split(' ')
    temp=int(0)
    #print("Programming Languages")
    for i in l:
        temp=0
        for j in lang:
            if(re.match(j,i.lower())):
                lstatus[temp]=1
                break;
            temp+=1
    for i in range(0,9):
        if lstatus[i]==1:
            f.write(lang[i].upper())
            f.write("\n")
    f.close()
#exception=['GLA','G.L.A','C','Java','Python','Go','HTML']

