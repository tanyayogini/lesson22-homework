# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list():
    data = _read(csv)
    data = _sort(data)
    return _filter(data)


def _read(csv):
    data = []
    for line in csv.split('\n'):
        data.append(line.split(';'))
    return data


def _sort(data):
    data.sort(key=lambda x: int(x[1]))
    return data


def _filter(data):
    result = []
    for i in data:
        if int(i[1]) >= 10:
            result.append(i)

    return result


if __name__ == '__main__':
    print(get_users_list())
