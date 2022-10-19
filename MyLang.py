var = {} # Список, в котором храняться переменные разного типа
l = 0 # Глобальная переменная, хранящая номер считываемой строки
x = 0 # Глобальная переменная, хранящая результат последней арифметической операции
a = 0 # Временные переменные
b = 0 # Временные переменные
c = 0 # Временные переменные

def main():
    file = input("Введите название файла с расширением: ")
    lixer(file)

# Объединяем в строку целый список
def join_strs(strs):
    result = ''
    for s in strs:
         result += ' ' + s
    return result[1:]

# ao - arithmetic operation
def ao(lisp, operation):
    global x, a, b, c
    if lisp[4] in var:
        if lisp[0] in var:
            a = var.get(lisp[0])
        else:
            a = lisp[0]
        if lisp[2] in var:
            b = var.get(lisp[2])
        else:
            b = lisp[2]
    else:
        print(f">>> Ошибка в строке {l} - переменная не создана")
        
    if operation == '+':
        x = float(a) + float(b)
    if operation == '-':
        x = float(a) - float(b)
    if operation == '*':
        x = float(a) * float(b)
    if operation == '/':
        x = float(a) / float(b)
        
    var.update({lisp[4] : x})

def lixer(file):
    global l;
    with open(file, 'r') as f:
        for line in f.readlines():
            l += 1
            lisp = line.split() # lisp - line + split
            if lisp == []:
                continue
            if lisp[0] == 'var':
                if len(lisp) >= 4:
                    list_join = join_strs(lisp)
                    if '"' in list_join:
                        v1 = list_join.find('"')
                        v1 += 1
                        v2 = list_join.rfind('"')
                        result = list_join[v1:v2]
                        var.update({lisp[1] : result})
                    else:
                        var.update({lisp[1] : lisp[3]})
                else:
                    var.update({lisp[1] : "None"})
            if lisp[1] == '=':
                if lisp[0] in var:
                    list_join = join_strs(lisp)
                    if '"' in list_join:
                        v1 = list_join.find('"')
                        v1 += 1
                        v2 = list_join.rfind('"')
                        result = list_join[v1:v2]
                        var.update({lisp[0] : result})
                    else:
                        var.update({lisp[0] : lisp[2]})
                else:
                    print(f">>> Ошибка в строке {l} - присваивание значения не существующей переменной")
            if lisp[0] == 'puts':
                if lisp[1] in var:
                    print(var.get(lisp[1]))
                else:
                    list_join = join_strs(lisp)
                    if '"' in list_join:
                        v1 = list_join.find('"')
                        v1 += 1
                        v2 = list_join.rfind('"')
                        result = list_join[v1:v2]
                        print(result)
                    else:
                        print(lisp[1])
            if lisp[0] == 'gets':
                if lisp[1] in var:
                    i = input()
                    var.update({lisp[1] : i})
                else:
                    print(f">>> Ошибка в строке {l} - присваивание значения не существующей переменной")
            if lisp[0] == '--':
                continue
            # Осуществление арифметических операций
            if (lisp[1] == 'plus' or lisp[1] == '+') and (lisp[3] == '->'):
                ao(lisp, '+')
            if (lisp[1] == 'minus' or lisp[1] == '-') and (lisp[3] == '->'):
                ao(lisp, '-')
            if (lisp[1] == 'mul' or lisp[1] == '*') and (lisp[3] == '->'):
                ao(lisp, '*')
            if (lisp[1] == 'div' or lisp[1] == '/') and (lisp[3] == '->'):
                ao(lisp, '/')

if __name__ == '__main__':
    main()



# Не выводить None через puts когда переменной не существует
# Добавить конкатенацию строк
# Научить переменные получать значения чужих переменных
    # Надо оборочивать строки в кавычки, а после считывать их, чтобы не путать с переменными
        # Добавить вывод текста в puts
    # Плюсом можно будет хранить не одно слово в переменной, а целые текста
# Возможность менять значение переменных присваивая им не значение, а операцию.
# Добавить комментарии
# Добавить знак просьбы о вводе значения. Способ i = input('> ') не работает
# Ну и всё остальное
# Добавить вывол типа переменной и его значения через специальную функцию
