from xeger import Xeger
_x = Xeger()
for i in range(20):
    testStr = _x.xeger(r'/[a-z,_]+\((?R)?\)/')
    print(repr(testStr))
