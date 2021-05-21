class Recrut:

    def __init__(self, name = '', city = '', status = ''):
        self.name = name
        self.city = city
        self.status = status

    def init_from_dict(self, recrut_dict):
        self.name = recrut_dict.get('name')
        self.city = recrut_dict.get('city')
        self.status = recrut_dict.get('status')


count = 0 # считает записи (типа для удобства пользователя)
unsw = 'д' # признак продолжения внесения рекрутов
recruts =[]

while unsw == str.lower('д'):
    recrut = {}
    count += 1
    print(f'    {count}-я запись')

    recrut['name'] = input('Введите имя и фамилию: ')
    recrut['city'] = input('Введите город проживания: ')
    recrut['status'] = input('Введите статус: ')
    recruts.append(recrut)

    unsw = input('Для продолжения нажмите "д", для завершения - "н": ')

for recrut in recruts:
    rct = Recrut()
    rct.init_from_dict(recrut)
    print(f'{rct.name} г. {rct.city} статус: {rct.status}')