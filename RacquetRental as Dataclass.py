from dataclasses import dataclass, asdict
import csv


#import csv
#from dataclasses import dataclass, asdict

# 1. Define the data class using @dataclass
# 2. Create a list of dataclass instances
# 3. Write the dataclasses to a CSV file
# 4. asdict() turns each dataclass instance into a dictionary
# 5 . Create csv file
    #with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
# 6. Write the column headers   
# 8.Write the data rows
# 9. print(f"Successfully wrote data to {csv_filename}")

@dataclass
class raq_rent:
    r_head:float
    r_length:float
    r_manuf:str
    #user_input:str
    #user_dat:list
#cant figure below out,no idea why parsing failed...syntax error??
Rentals=
    [raq_rent1=raq_rent(98,27,'head'),
    raq_rent2=raq_rent(105,27.5,'wilson'),
    raq_rent3=raq_rent(100,26,'babolat')
    ]
csv_filename='Racquet Rental Log.csv'

fieldnames = list(asdict(Rentals[0]).keys())

with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    
# Write the column headers
    writer.writeheader()
        # Write the data rows
    for rent in Rentals:
        writer.writerow(asdict(rent))

print(f"Successfully wrote data to {csv_filename}")

#if __name__=="__main__":
#    def user_dat():
#        r_head=input('head size?  ')
#        r_length=input('length?  ')
#        r_manuf=input('manufacturer?  ')
#        return [r_head,r_length,r_manuf]
     
#q=raq_rent (98,102,'head',32,44)
#print(q)

#import csv
#from dataclasses import dataclass, asdict

# 1. Define the data class using @dataclass
#@dataclass
#class Employee:
#    name: str
#    department: str
#    salary: float

# 2. Create a list of dataclass instances
#employees = [
#    Employee("Alice Smith", "Engineering", 85000.00),
#    Employee("Bob Jones", "Marketing", 62000.50),
#    Employee("Charlie Brown", "Sales", 71000.00)
#]

# 3. Write the dataclasses to a CSV file
#csv_filename = "employees.csv"

# asdict() turns each dataclass instance into a dictionary
#fieldnames = list(asdict(employees[0]).keys())

#with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
#    writer = csv.DictWriter(file, fieldnames=fieldnames)
#    
#    # Write the column headers
#    writer.writeheader()
#    
#    # Write the data rows
#    for emp in employees:
#        writer.writerow(asdict(emp))

#print(f"Successfully wrote data to {csv_filename}")
