from urllib.request import urlretrieve

link=input('image download link : ')

fileName=input('File Name : ')

urlretrieve(link,'image/'+fileName+'.jpg')