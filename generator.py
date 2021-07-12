with open('./text.txt') as file:
    paragraph=file.read();

    paraCount=int(input('paragraph count : '))# 3

    for count in range(paraCount):
        with open('./generator.txt','a') as write_file:
            write_file.write(paragraph+'\n\n')