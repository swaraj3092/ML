import csv

data = [
    ['Name', 'Age', 'City','Mobile Number','rollno'],
    ['Swaraj', 21, 'Puri', '1234567890','23053092'],
    ['Bob', 26, ' Bihar', '0987654321','23052611'],
    ['Prajakta', 20 , 'Tata', '1122334455','23052811']
]

with open('main.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

print("CSV file 'main.csv' created successfully.")