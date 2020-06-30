Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def test_range(n):
    if n in range(3,9):
        print("%s is in the range"%str(n))
    else:
        print("the number is outside the given range")
test_range(5)
5 is in the range