import parse
import trie

if __name__ == '__main__':
#==============================================
# This is for construct
#==============================================

    with open('./eminem.html', 'r') as f:
        content = f.read()
    #print(content)
    parser = parse.parse()
    parser.feed(content)
    raw_data = parser.data
    data = []
    # construct raw_data
    for item in raw_data:
        if '\n' not in item:
            data.append(item)
    #print(data)

    # construct words set and then build trie
    words_set = set()
    for item in data:
        elements = item.split(' ')
        #print(elements)
        for e in elements:
            if e not in words_set:
                words_set.add(e)
    #print(words_set)
    words_list = list(words_set)
    print(words_list)

    # construct occurence list
    occ_list = []
    for word in words_set:
        l = []
        for i in range(0, len(data)):
            if word in data[i]:
                l.append(i)
        occ_list.append(l)
    print(occ_list)

    # build trie
    t = trie.Trie()
    root = t.build_trie(words_list, occ_list)

#=================================================
# This part is for search
#=================================================
    while True:
        keywords = input().split(" ")
        if len(keywords) == 1 and keywords[0] == 'IHateEminem':
            print('See ya.')
            break

        #put all together and get duplicate
        l = []
        for word in keywords:
            if t.is_member(word):
                print(t.get(word))
                for element in t.get(word):
                    l.append(element)
            else:
                print('Oops, no results.')
        print(l)

        result = set([x for x in l if l.count(x) > 1])
        result = list(result)
        for i in range(0, len(result)):
            print(i+1, ', ',data[result[i]])
