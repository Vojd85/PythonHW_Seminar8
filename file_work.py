import json
def load():
            # загрузить из json
            # fname='BD.json' #открываем файл
            with open('BD.json', 'r', encoding='utf-8') as file:  # открываем файл на чтение
                BD_local = json.load(file)  # загружаем из файла данные в словарь data
            return BD_local
def save(inp):
            # сохранить в json
            with open('BD.json', 'w', encoding='utf-8') as file:  # открываем файл на запись
                file.write(json.dumps(inp,
                                    ensure_ascii=False))  # преобразовываем словарь data в unicode-строку и записываем в файл
            

