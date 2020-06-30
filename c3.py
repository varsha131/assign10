Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def cloning(li1):
    li_copy=li1[:]
    return li_copy
li1=[4,8,2,10,15,18]
li2=cloning(li1)
print("original list:",li1)
print("after cloning:",li2)