import requests

# https://pointerpointer.com/images/710.jpg
url="https://pointerpointer.com/images/"

nowLine=1
while True:


    try:
        gradeUrl=url+str(nowLine)+".jpg"
        r = requests.get(gradeUrl)

        fileName=str(nowLine)+".jpg"
        with open(fileName, 'wb') as outfile:
            outfile.write(r.content)
    except Exception as e: 
        print(e)
        print("some error: "+str(nowLine))

    print(str(nowLine))  # print log
    nowLine=nowLine+1
    if nowLine==711:
        break


