import unirest
import fitz
import os
import extract_spell as es
def spell(src_file,string):
    l=string.split(' ')
    l = [x.replace("\r","") for x in l]
    l = [x.replace("\n"," ") for x in l]
    l = [x.replace("\s","") for x in l]
    l = [x.replace("\u","") for x in l]
    #print(l)
    try:
        os.remove(src_file+"_spell"+".txt")
        f = open(src_file+"_spell"+".txt", "a")
    except:
        f = open(src_file+"_spell"+".txt", "a")
    for i in l:
        if i.find(" ")!=-1:
            temp=i.split(" ")
            for x in i:
                if len(x)<=1:
                    pass
                else:
                    try:
                        response = unirest.get("https://montanaflynn-spellcheck.p.rapidapi.com/check/?text="+str(x.lower()),
                          headers={
                            "X-RapidAPI-Key": "3f9bb1c780msh4a63fc983a53845p122bd3jsn5f78421fed65"
                          }
                        )
                    except:
                        pass
                    #print response.raw_body
                    f.write(response.raw_body+"*br*")
        else:
            if len(i)<=1:
                pass
            else:
                try:
                    response = unirest.get("https://montanaflynn-spellcheck.p.rapidapi.com/check/?text="+str(i.lower()),
                      headers={
                        "X-RapidAPI-Key": "3f9bb1c780msh4a63fc983a53845p122bd3jsn5f78421fed65"
                      }
                    )
                except:
                    pass
                #print response.raw_body
                f.write(response.raw_body+"*br*")
    f.close()
    es.ext_spell(src_file)

