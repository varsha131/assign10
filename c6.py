Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def up_low(string):
    uppers=0
    lowers=0
    for char in string:
        if char.islower():
            lowers+=1
        elif char.isupper():
            uppers+=1
        else:
            pass
    return(uppers,lowers)
print(up_low("hello mr.rogers,how are you this fine tuesday?"))
(0, 37)