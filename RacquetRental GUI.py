#from datetime import date
#import os.path
import csv
import PySimpleGUI as sg


def save_contact(Rental_Date,User_Name,Racquet_Mfg,Racquet_Model,Head_Size,Return_Date,Staff_Initials):
    #file_exists=os.path.isfile('RacquetRentals.csv')
    with open('RacquetRentals.csv', mode='a', newline='') as csvfile:
        fieldnames = ['Rental_Date','User_Name','Racquet_Mfg','Racquet_Model','Head_Size','Return_Date','Staff_Initials']
        writer = csv.writer(csvfile)
        # writer = csv.writer(csvfile, fieldnames=fieldnames)
        # if not file_exists:
        #     writer.writeheader()
        writer.writerow([Rental_Date,User_Name,Racquet_Mfg,Racquet_Model,Head_Size,Return_Date,Staff_Initials])
      
def get_contacts():
    '''review contacts'''
    contacts = []
    with open('RacquetRentals.csv', mode='r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            contacts.append(row)
    return contacts

               
def main():
    
    sg.theme('SystemDefault')
    layout =[[sg.Text('Please enter rental information')],
    [sg.Text('Rental_Date', size =(15, 1)), sg.InputText(key='Rental_Date')],
    [sg.Text('User_Name', size =(15, 1)), sg.InputText(key='User_Name')],
    [sg.Text('Racquet_Mfg', size =(20, 1)), sg.InputText(key='Racquet_Mfg')],
    [sg.Text('Racquet_Model', size =(20, 1)), sg.InputText(key='Racquet_Model')],
    [sg.Text('Head_Size', size =(20, 1)), sg.InputText(key='Head_Size')],
    [sg.Text('Return_Date', size =(15, 1)), sg.InputText(key='Return_Date')],
    [sg.Text('Staff initials', size =(15, 1)), sg.InputText(key='Staff_Initials')],
    [sg.Save(), sg.Exit()]]
    
    window = sg.Window('eGuest with PySimple GUI', layout)
    #event, values = window.read()
    # window.close()

    while True:
        event, values = window.read()
        if event == 'Save':
            save_contact(values['Rental_Date'],values['User_Name'],values['Racquet_Mfg'],values['Racquet_Model'],
                          values['Head_Size'],values['Return_Date'],values['Staff_Initials'])
            sg.Popup('Contact saved!')
        elif event == 'Exit':
            break
    window.close()

if __name__ == '__main__':
    main()
