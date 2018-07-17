import csv
with open('C:\\Users\\Administrator\\Desktop\\pyprac\\module\\717file\\aqi.csv', 'r', encoding='utf-8-sig') as a:
    reader = csv.reader(a)
    init=int(50)
    for row in reader:
        if row[2] == 'AQI':
            pass
        else:
            if int(row[2])< int(init):
                init = row[2]
                place = row[1]
                location = row[0]
    print(place,location,init)        