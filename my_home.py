s = b"r\xc3\xa9sum\xc3\xa9"
print(type(s))
b = s.decode("utf-8")
print(b)
c = b.encode()
print(c)
d = c.decode('Latin1')
print(d)