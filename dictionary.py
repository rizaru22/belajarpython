orang={1:{"nama":"Safrizal","umur":"34"},2:{"nama":"Arti","umur":"17"}}
# print(orang)

# for key in orang:
#     # print(orang[key])
#     for key2 in orang[key]:
#         print(orang[key][key2])

# print (orang.items())

for key,value in orang.items():
    # print(key)
    for key2 in value:
        print(key2+"-"+value[key2])

