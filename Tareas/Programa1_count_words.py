import re
def count_words(lista):
    lista=''.join(lista)
    lista=re.sub(r'[^\w\s]',' ',lista)
    palabras=lista.split()
    dic = {palabras[i]:0 for i in range(len(palabras))}
    for p in palabras:
        dic[p]+=1
    return dic
txt = ['Hola, cómo estás!','gana dinero , gana desde casa.', 'Hola, puedes llamar ahora?', 'Hola, te puedo llamar mañana?']
print(count_words(txt))
    