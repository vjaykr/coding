import csv

def calculate_average(csv_file, column_name):
    total = 0
    count = 0
    
    with open(csv_file,'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            if column_name in row:
                try:
                    total += float(row[column_name])
                    count += 1
                except ValueError:
                    print(f"Invalid value '{row[column_name]}' in column '{column_name}'")
                    
    if count > 0:
        average = total / count
        return average
    else:
        return None
    
csv_file = "data.csv"
column_name = "value"

average = calculate_average(csv_file, column_name)
print(f"The average of column '{column_name}' is {average}")              
    