file0 = open('MANIFESTO OF THE COMMUNIST PARTY.txt')
article = file0.read()
paragraphs = article.split('\n')
words = []
for EachParagraph in paragraphs:
    words += EachParagraph.split(' ')
dict0 = {}
for word in words:
    try:
        dict0[word] += 1
    except KeyError:
        dict0[word] = 1
print(dict0)
