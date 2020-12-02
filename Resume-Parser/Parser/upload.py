#!C:/Python27/python.exe -u
# -*- coding: cp1252 -*-
import cgi, os
import subprocess
import cgitb; cgitb.enable()
try:
   form = cgi.FieldStorage()
   # Get filename here.
   fileitem = form['filename']
# Test if the file was uploaded
   if fileitem.filename:
      # strip leading path from file name to avoid 
      # directory traversal attacks
      fn = os.path.basename(fileitem.filename)
      open("E:/xampp/htdocs/Parser/Files/"+fn, 'wb').write(fileitem.file.read())
      while(1):
         try:
            f=open("task.txt",'w')
            f.write(fn[0:-4])
            f.close()
            break
         except:
            pass
      subprocess.call("python parser_controller.py 1", shell=True)
      message = 'The file "' + fn + '" was uploaded successfully'
   else:
      message = 'No file was uploaded'
except:
   message="Please Choose the file"
print """\
Content-Type: text/html\n
<html>
<body>
   <p>%s</p>
</body>
</html>
""" % (message)
