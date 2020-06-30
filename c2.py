Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> color=['red','green','white','black','pink','yellow']
color=[x for (i,x) in enumerate(color) if  i not in (0,4,5)]
print(color)