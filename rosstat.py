from xml.etree.ElementTree import indent
from bs4 import BeautifulSoup as BS
import requests
from datetime import datetime
import json

def main():
    res = requests.get('https://rosstat.gov.ru/')
    html = res.text
    soup = BS(html, features="html.parser")
    rows = soup.select('.indicators__main .indicators__cols')

    stat_data = []

    for row in rows:
        indicator = row.select_one('.indicators__link').get_text()
        data = row.select('.indicators__data')[1].get_text()
        unit = row.select('.indicators__data')[2].get_text()

        stat_data.append(
            {
                "indicator": indicator,
                "data": data,
                "unit": unit
            }
        )


    write_json(stat_data)
   

def get_current_date():
    now = datetime.now()
    return now.strftime('%d-%m-%y %H-%M')




def write_json(data):
    with open(f'rosstat/{get_current_date()}.json', 'w', encoding='utf-8') as f:
        json_data = json.dumps(data, indent=4, ensure_ascii=False)
        f.write(str(json_data))




if __name__ == '__main__':
    main()