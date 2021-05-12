
import os


pathOfFolder=input("Enter the path of the folder - ")
os.chdir(pathOfFolder)#add your folder path
cfolder_path = os.getcwd()
print(os.listdir())
with open('htmlelemets.html','a') as f:
    f.write('''<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    </head>
    <body>''')

    for ele in os.listdir():
        print(ele[-3:])
        if os.path.isdir(cfolder_path+"/{}".format(ele)):
            folder = """./{}""".format(ele)
            print(folder)
            os.chdir(cfolder_path+"/{}".format(ele))
            os.listdir()
            for deepervideos in os.listdir():
                if deepervideos[-3:] == "mp4":
                    file  = folder+'/'+deepervideos
                    print("yes")
                    f.write("""<br><h2 style = "display : inline;">{} </h2><i>in ({})</i> <br> \n""".format(deepervideos[:-4],file))
                    f.write("""======<video preload="metadata" controls width="1080" src="{}"></video><br> \n""".format(file))
            os.chdir(cfolder_path)
        if ele[-3:] == "mp4":
            print("yes")
            f.write("<h3>{}</h3> \n".format(ele[:-4]))
            f.write("""===<video preload="metadata" controls width="1080" src="{}"></video> \n""".format(ele))
    f.write('''</body>
</html> ''')
