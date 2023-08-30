import json
import requests
import  os

ext='.json'
base_url='https://rosrid.ru/api/open-data?'

card_types=[
    ('Сведения о результатах научно-исследовательских работ','ikrbs'),
    ('Сведения о защищённых диссертациях на соискание учёных степеней','dissertation'),
    ('Сведения о результате интеллектуальной деятельности','rid'),
    ('Сведения об использовании РИД','iksi'),
    ('Состояния правовой охраны результатов интеллектуальной деятельности','ikspo'),
]

def get_data(tables=None,year_start=2016,year_stop=2022,by_year=False):
    print(f'Скачивание открытых данных из ЕГСУ НИОКТР')
    for card_type in tables:
        print(f'\t - {card_type[0]}:')
        folder_type = f'{card_type[1]}'
        if not os.path.isdir(folder_type):
            os.mkdir(folder_type)
        for year in range(year_start,year_stop+1):
            folder_year = os.path.join(folder_type,f'{year}')
            print(f'\t\t - {folder_year} год: ', end='')
            if not os.path.isdir(folder_year):
                os.mkdir(folder_year)
            if not by_year:
                for month in range(1,12+1):
                    m=f'{month:02}'
                    print(f'{m}',end=',')
                    url=f'{base_url}year={year}&month={m}&card_type={card_type[1]}'
                    r = requests.get(url)
                    data = r.json()
                    filename = os.path.join(folder_year,m+'.json')
                    with open(filename,'w', encoding='utf-8') as f:
                        json.dump(data,f,ensure_ascii=False)
            else:
                m = f'all_months'
                print(f'{m}', end=',')
                url = f'{base_url}year={year}&month={m}&card_type={card_type[1]}'
                r = requests.get(url)
                data = r.json()
                filename = os.path.join(folder_year, m + '.json')
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False)

            print()
    print('Скачивание завершено')

# За всё время
# get_data(tables=card_types)

# Только за 2022 год по месяцам
#get_data(tables=card_types,year_start=2022,year_stop=2022)

# Только за 2022 год за весь год
get_data(tables=card_types,year_start=2022,year_stop=2022,by_year=True)

# за период 2020-2022
# get_data(tables=card_types,year_start=2021,year_stop=2022)

