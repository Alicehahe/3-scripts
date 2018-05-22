import pprint
cats = [{'name':'zophie','desc':'chubby'},{'name':'pooka','desc':'fluffy'}]
print pprint.pformat(cats)
f = open('mycats.py','w')
z = f.write('cats = ' + pprint.pformat(cats) + '\n')
print len(pprint.pformat(cats))
print type(z)
f.close()
print z
