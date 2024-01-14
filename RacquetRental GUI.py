 from datetime import date
import os.path
import csv
import PySimpleGUI as sg


def save_contact(Visit_Date,Guest_Fname,Guest_Lname,Guest_Address,Guest_City,Guest_State,Guest_Zip,Member_Name,Staff_Initials):
    file_exists=os.path.isfile('eGuestData8877.csv')
    with open('eGuestData8877.csv', mode='a', newline='') as csvfile:
        fieldnames = ['Visit_Date','Guest_Fname','Guest_Lname','Guest_Address','Guest_City','Guest_State','Guest_Zip','Member_Name','Staff_Initials']
        writer = csv.writer(csvfile)
        # writer = csv.writer(csvfile, fieldnames=fieldnames)
        # if not file_exists:
        #     writer.writeheader()
        writer.writerow([Visit_Date,Guest_Fname,Guest_Lname,Guest_Address,Guest_City,Guest_State,Guest_Zip,Member_Name,Staff_Initials])
      
def get_contacts():
    contacts = []
    with open('eGuestData8877.csv', mode='r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            contacts.append(row)
    return contacts

               
def main():
    
    sg.theme('DarkAmber')
    layout =[[sg.Text('Please enter guest information')],
    [sg.Text('Visit_Date mm/dd/yyyy', size =(15, 1)), sg.InputText(key='Visit_Date')],       
    [sg.Text('Guest first name', size =(15, 1)), sg.InputText(key='Guest_Fname')],
    [sg.Text('Guest last name', size =(15, 1)), sg.InputText(key='Guest_Lname')],
    [sg.Text('Guest address', size =(20, 1)), sg.InputText(key='Guest_Address')],
    [sg.Text('Guest city', size =(20, 1)), sg.InputText(key='Guest_City')],
    [sg.Text('Guest state', size =(20, 1)), sg.InputText(key='Guest_State')],
    [sg.Text('Guest zip', size =(20, 1)), sg.InputText(key='Guest_Zip')],
    [sg.Text('Member name', size =(15, 1)), sg.InputText(key='Member_Name')],
    [sg.Text('Staff initials', size =(15, 1)), sg.InputText(key='Staff_Initials')],
    [sg.Save(), sg.Exit()]]
    
    window = sg.Window('eGuest with PySimple GUI', layout)
    #event, values = window.read()
    # window.close()

    while True:
        event, values = window.read()
        if event == 'Save':
            save_contact(values['Visit_Date'],values['Guest_Fname'],values['Guest_Lname'],values['Guest_Address'],
                          values['Guest_City'],values['Guest_State'],values['Guest_Zip'],values['Member_Name'],values['Staff_Initials'])
            sg.Popup('Contact saved!')
        elif event == 'Exit':
            break
    window.close()

if __name__ == '__main__':
    main()
