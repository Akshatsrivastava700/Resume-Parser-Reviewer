def clean(string,status):
    try:
        if status==0:
            string = string.replace("'", "")
            string = string.replace('"', "")
            string = string.replace(",", "")
            string = string.replace(".", "")
            string = string.replace(":", "")
            string = string.replace("|", "")
            string = string.replace("/", "")
            string = string.replace("\ ","")
            string = string.replace("(", "")
            string = string.replace(")", "")
            string = string.replace("{", "")
            string = string.replace("}", "")
        elif status==1:
            string = string.replace("'", "")
            string = string.replace('"', "")
            #string = string.replace(",", "")
            string = string.replace(":", "")
            string = string.replace("|", "")
            string = string.replace("/", "")
            string = string.replace("\ ","")
            string = string.replace("(", "")
            string = string.replace(")", "")
            string = string.replace("{", "")
            string = string.replace("}", "")
        return(string)
        
    except:
        return("Error Generated")
        
