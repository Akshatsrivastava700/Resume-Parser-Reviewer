import unirest
import extract_sent as es
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import os
def ratio(src_file,string):
        l=string.split(".")
        l = [x.replace("\r","") for x in l]
        l = [x.replace("\n","") for x in l]
        l = [x.replace("\s","") for x in l]
        l = [x.replace("\u","") for x in l]
        try:
            os.remove(src_file+"_sentiment.txt")
            f = open(src_file+"_sentiment.txt", "a")
        except:
            f = open(src_file+"_sentiment.txt", "a")
        for i in l:
            if len(i)<=5:
                pass
            else:
                response = unirest.post("https://text-sentiment.p.rapidapi.com/analyze",
                headers={
                    "X-RapidAPI-Key": "3f9bb1c780msh4a63fc983a53845p122bd3jsn5f78421fed65",
                    "Content-Type": "application/x-www-form-urlencoded"
                  },
                  params={
                    "text": i
                  }
                )
                #print response.raw_body
                f.write(response.raw_body+"\n")
        f.close()
        es.extract(src_file)
        sentiment=['Positive','Negative','Neutral']
        sent_val=[]
        tree = ET.parse(src_file+'_sent_ext.xml')  
        root = tree.getroot()
        for elem in root:  
            for subelem in elem:
                sent_val.append(int(subelem.text))
        
        plt.bar(sentiment, sent_val)
        try:
                os.remove(src_file+'_sentiment.png')
                plt.savefig(src_file+'_sentiment.png')    
                plt.close()
        except:
                plt.savefig(src_file+'_sentiment.png')    
                plt.close()  
        #os.remove(src_file+'_sent_ext.xml')
