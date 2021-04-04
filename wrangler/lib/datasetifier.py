import csv
from shutil import copyfile

def write_csv(filename, fields, rows):
    with open('data/' + filename, 'a+') as f:
        write = csv.writer(f)
        write.writerows(rows)