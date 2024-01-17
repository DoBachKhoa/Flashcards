import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def process_word(para, tagset):
    a, b = para.split('\t')
    a = a.strip()
    temp = b.split('|')
    meanings, tags = temp[:-1], temp[-1].split(',')
    tags = [t.strip() for t in tags]
    if len(tags) == 1 and tags[0] == '':
        tags = ['_untagged_']
    tags.append('_defaulttag_')
    for tag in tags:
        tagset.add(tag)
    meanings = [m.strip() for m in meanings]
    return [a, meanings, tags]

def process_file(filename):
    tagset = set()
    document = getText(filename)
    document.replace(u'\xa0', u' ')
    document = document.strip().strip('\n').strip()
    paras = document.split('\n')
    entries = []
    for para in paras:
        entries.append(process_word(para, tagset))
    return entries, tagset

def process(filename):
    entries, tagset = process_file(filename)
    print('Your processed dictionary looks like this: ')
    print('----------------------------------------')
    print('Tagset: ', tagset)
    print('----------------------------------------')
    print('Entries: ')
    for entry in entries: print(entry)
    print('----------------------------------------')
