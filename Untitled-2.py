'''Refactoring of racquet rental script as dataclass'''
from dataclasses import dataclass, asdict
import csv
import os.path
import string


@dataclass
class raq_rent:
    '''Racquet specifications'''
    r_head:float
    r_length:float
    r_manuf:str

usr_manuf=input(str('what is racquet manufacturer?'))
usr_length= input(str('what is racquet length'))      #incorporate try/fail user input sanitation
user_headsize=input(str( 'what is racquet head size'))
Rentals=[raq_rent(98,27,'head'), raq_rent(105,27.5,'wilson'),
    raq_rent(100,26,'babolatGOOFY')]

csv_filename='Racquet Rental Log.csv'
fieldnames = list(asdict(Rentals[0]).keys())
file_exists=os.path.isfile('Racquet Rental Log.csv')

with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

# Write the column headers
    writer.writeheader()
        # Write the data rows
    for rent in Rentals:
        writer.writerow(asdict(rent))

print(f"Successful! wrote data to {csv_filename}")

#problems to solve.
#Right now, only overwrites csv data. need to append to next row
#How to populate Rentals on the fly with user input
#How to sanitize user input data
#add rentAL date, rentER name
#appify when done???

# work in this solution from eGuest project.
#  def member_name():
#         """generates merged member first and last names"""
#         member_first=(str.capitalize(input('member first name?  ')))
#         member_last=(str.capitalize(input('member last name?  ')))
#         member_name_merge=(' '.join([member_first,member_last]))
#         return member_name_merge



# with open('eGuestREDO1225222.csv', 'a', newline='') as csvfile:
#         fieldnames = ['Visit_Date','Guest_Fname','Guest_Lname',
#                      'Guest_Address','Guest_City','Guest_State','Member_Name']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         if not file_exists:
#             writer.writeheader()

#         for a in range (0,total_guests):
#                 writer.writerow({'Visit_Date':visit_date(),'Guest_Fname':guest_fname(),\
#                 'Guest_Lname':guest_lname(),'Guest_Address':guest_address(),\
#                 'Guest_City':guest_city(),'Guest_State':guest_state(),'Member_Name':member_name()\
#                 })
# #there is 1 and only 1 set of function calls at the end of scrit when writing
# #csv to disk...otherwise will call a second #time at the end and overwrite
# #original data input by userfile_exists=os.path.isfile('eGuestREDO1225222.csv')
