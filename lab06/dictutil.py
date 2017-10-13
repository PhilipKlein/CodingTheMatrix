def dict2list(dct, keylist): return [dct[i] for i in keylist]

def list2dict(L, keylist): return dict(zip(keylist, L))

def listrange2dict(L): return dict([i, L[i]] for i in range(len(L)))
#def listrange2dict(L): return dict(zip(range(len(L)), L))
#def listrange2dict(L): return list2dict(L, range(len(L)))


def makeInverseIndex(strlist):
    # read all files
    inverse_index = {}
    doc_number = 0
    for document in strlist:
        with open(document) as IF:
            for line in IF:
                for word in line.split():
                    if word in inverse_index:
                        inverse_index[word].add(doc_number)
                    else:
                        inverse_index[word] = set()
                        inverse_index[word].add(doc_number)
                doc_number += 1
    return inverse_index

def orSearch(inverse_index, query):
    document_set = {}
    for word in query:
        document_set[word] = set();
        if word in inverse_index:
            document_set[word].update(inverse_index[word])
    return document_set

def andSearch(inverse_index, query):
    set_dct = orSearch(inverse_index, query)
    add_set = set_dct[query[0]]
    for val in set_dct.values():
        add_set &= val
    return add_set


orList = ['ball', 'b', 'Video']
andList = ['ball', 'the']
print("orSearch with words", orList)
print(orSearch(makeInverseIndex(('stories_big.txt',)), orList))
print("andSearch with words", andList)
print(andSearch(makeInverseIndex(('stories_big.txt',)), andList))
