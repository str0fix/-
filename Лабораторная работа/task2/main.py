def get_count_char(str_):
    dict_={}
    for x in str_:
        if (x.isalpha()):
            dict_[x]=0
    for x in str_:
        for y in dict_:
            if ( ( x == y ) and x.isalpha() ):
                dict_[y]+=1
    return dict_

def get_percent(dict_):
    count=len(dict_)
    for x in dict_:
        dict_[x]= round(dict_[x]/count, 3)
    return dict_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
main_str = main_str.lower()
main_str = "".join(main_str.split())
new_str=get_count_char(main_str)
print(new_str)
print("Далее результат второй функции с округлением до тысячных долей")
print(get_percent(new_str))