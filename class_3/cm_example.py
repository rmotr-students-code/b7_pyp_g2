f = open('names.txt', 'r')
try:
    big_name = ''
    for name in f.readlines():
        big_name += name
except Exception:
    pass
finally:
    f.close()
