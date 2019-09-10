import datetime
import math
from hashlib import  md5
def  getHoney():
    e = math.floor(datetime.datetime.now().timestamp())
    i = hex(e).upper()[2:]
    t = md5(str(e).encode('utf-8')).hexdigest().upper()
    if len(i) != 8:
        _as = "479BB4B7254C150"
        _cp = "7E0AC8874BB0985"
        return _as, _cp
    a = ''
    r = ''
    o = t[:5]
    n = t[-5:]
    for s in range(5):
        a += o[s] + i[s]
        r += i[s + 3] + n[s]
    _as = 'A1'+ a + i[-3:]
    _cp = i[:3] + r + 'E1'
    return _as, _cp


