Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def unique_list(l):
    x=[]
    for a in l:
        if a not in x:
            x.append(a)
        return x
print(unique_list([1,2,3,3,3,3,4,5]))
[1]