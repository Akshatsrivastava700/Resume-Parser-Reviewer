import os
flag=int(0)
def corrections(string):
    temp=string.split(" ")
    temp=[x.replace("\n","") for x in temp]
    temp.remove('')
    i=int(0)
    while(i<len(temp)):
        if temp[i]=='':
            del(temp[i])
        i=i+1
    #print(temp)
    if (len(temp[1])>15 or len(temp[3])==1):
        return("")
    if temp[4]!="corrections:":
        return("")
    if temp[1]==temp[3]:
        return("")
    else:
        return(temp[1]+":"+temp[3])
        
    
def ext_spell(src_file):
    f=open(src_file+"_spell.txt",'r')
    string=f.read()
    #print string
    f.close()
    os.remove(src_file+"_spell.txt")
    string = string.replace('"', "")
    string = string.replace("{", "")
    string = string.replace("}", "")
    string = string.replace(",", "")
    temp=string.split("*br*")
    del(temp[-1])
    try:
        os.remove(src_file+"_spell_ext.txt")
        f=open(src_file+"_spell_ext.txt",'a')
    except:
        f=open(src_file+"_spell_ext.txt",'a')
    for x in temp:
        #print(x)
        crt_word=corrections(x)
        if len(crt_word)!=0:
                f.write(crt_word)
                f.write("\n")
    f.close()

