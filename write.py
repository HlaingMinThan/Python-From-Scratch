# with open('./about.txt','w') as file:
#     file.write()
    

# #other work

# with open('./about.txt','a') as file:
#     file.write()

lists=['I am hlaing min than','\nI am 20 years old']

with open('./about.txt','a') as file:
    file.writelines(lists)