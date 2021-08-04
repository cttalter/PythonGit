string0 = input('enter string:')
outstr = ''
for eachstr in string0:
    if not eachstr.isdigit():
        outstr += eachstr
print(outstr)
