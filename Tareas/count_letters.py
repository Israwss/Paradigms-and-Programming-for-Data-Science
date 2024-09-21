def count_letters(word):
    word.lower()
    word=word.replace(' ','')
    word=list(word)
    dic={word[i]:0 for i in range(len(word))}
    for w in word:
        dic[w]+=1
    dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
    return dic

print(count_letters('últimamente hemos tenidos varios días muy lluviosos'))
    