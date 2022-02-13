def Main_menu():
    oper = Show_request()
    if oper == '1':
        print('1')
    elif oper == '2':
        print('2')
    elif oper == '3':
        print('3')
    elif oper =='4':
        print('4')
    else:
        exit()
    return


def Show_request():
    message_1 = 'Для работы со справочником нажмите:\n1 - показать все данные из файла\n2 - найти запись в справочнике\n' + \
        '3 - редактировать запись из файла\n4 - записать все данные в файл\n5 - выход из программы' 
    print(message_1)
    answer = input()
    while answer not in ['1', '2', '3', '4', '5']:
        print(message_1)
        answer = input()
    return answer
