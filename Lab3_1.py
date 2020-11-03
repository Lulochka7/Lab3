import csv
with open("zarplata.csv", encoding='utf-8') as r_file:    
    file_reader = csv.reader(r_file, delimiter = ";")    
    count = 0    
    for row in file_reader:
        if count == 0:            
            print(f'Файл содержит столбцы: {";".join(row)}')
        else:            
            print(f'    {row[0]}  {row[1]} получит зарплату в размере {row[2]}')
        count += 1
    print(f'Всего в файле {count} строк.')