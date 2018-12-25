class_list = ['1,2', '1,2,3', '3,4', '5,6', '5,6,7', '7,8', '9,10,11']
week_list = ['一', '二', '三', '四', '五', '六', '日']
realfind = {}
for a in class_list:
    realfind[a] = {}
    for b in week_list:
        # print(a)
        # print(type(a))
        realfind[a][b] = {}
print(realfind)