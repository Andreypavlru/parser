from get_web import get_result_table
from Classes import ResultRace
new_row = {
    "place": [],
    "car_name": [],
    "driver_name": [],
    "races": [],
    "total_rating": []
}
a = get_result_table()
def append():
    k = 0
    for value in a.find_all('td'):
        el = value['class']
        for col in value:
            x = col.text.strip()
            if 'place' in el:
                new_row['place'].append(x)
            if 'car-n' in el:
                new_row['car_name'].append(x)
            if 'name' in el:
                new_row['driver_name'].append(x)
            if 'last' in el:
                new_row['total_rating'].append(x)
            if 'standart' in el:
                if (x == 'X' or x == ''):
                    x = '0'
                if (k % 2 == 0):
                    qualify = x
                else:
                    result = x
                    new_row['races'].append(ResultRace(qualification=qualify, rating=result))
                k += 1
    return new_row