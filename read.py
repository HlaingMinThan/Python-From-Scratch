# file=open('./text.txt')

# # for line in file:
# #     print(line)

# # file.seek(0);

# # lineLists=file.readlines()
# # print(lineLists);

# file.seek(50)

# paragraph=file.read(100)
# print(paragraph);

# file.close()

with open('./text.txt') as file:
    for line in file:
        print(line);


print('other work')