from datetime import date
import os.path
import csv
import PySimpleGUI as sg


def save_contact(rental_date,user_name,racquet_mfg,racquet_model,
                 head_size,return_date,staff_initials):
    '''write data to csv file'''

    with open('RacquetRentals.csv', mode='a', newline='',encoding='UTF-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([rental_date,user_name,racquet_mfg,racquet_model,
                         head_size,return_date,staff_initials])

def get_contacts():
    '''review contacts'''
    contacts = []
    with open ('RacquetRentals.csv', mode='r',encoding='UTF-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            contacts.append(row)
    return contacts

def main():
    '''gui layout and logic'''
    sg.theme('SystemDefault')
    layout =[[sg.Text('Please enter rental information')],
    [sg.Text('Rental date', size =(15, 1)), sg.InputText(key='rental_date')],
    [sg.Text('User name', size =(15, 1)), sg.InputText(key='user_name')],
    [sg.Text('Racquet mfg', size =(20, 1)), sg.InputText(key='racquet_mfg')],
    [sg.Text('Racquet model', size =(20, 1)), sg.InputText(key='racquet_model')],
    [sg.Text('Head size', size =(20, 1)), sg.InputText(key='head_size')],
    [sg.Text('Return date', size =(15, 1)), sg.InputText(key='return_date')],
    [sg.Text('Staff initials', size =(15, 1)), sg.InputText(key='staff_initials')],
    [sg.Save(), sg.Exit()]]

    window = sg.Window('Racquet Rental Tracker', layout)

    while True:
        event, values = window.read()
        if event == 'Save':
            save_contact(values['rental_date'],values['user_name'],values['racquet_mfg'],
                         values['racquet_model'],values['head_size'],values['return_date'],
                         values['staff_initials'])
            sg.Popup('Contact saved!')
        elif event == 'Exit':
            break
    window.close()

if __name__ == '__main__':
    main()
