'''A simple logbook for racquet rental saved to RACQUETRENTAL.csv'''

import csv
import os
from datetime import date
#from time import time--use to time difference between appending and tuple unpacking functions below
#[date,staff init,member,make,model,head size, returned(y/n)]

rentals=int(input('how many racquets out? '))
def dateout():
    '''Generate date of rental.'''
    out=date.today()
    return out

def staffname():
    '''Input staff initials.'''
    try:
        staff=input(str('staff initials  '))
    except ValueError:
        print ('staff initials cannot contain numbers')
    return str.upper(staff)

def mbrname():
    '''Input name of person renting racquet.'''
    try:
        memname=input('Enter member full name in format of: First Last.  ')
    except ValueError:
        print( 'member name cannot contain numbers')
    return str.title(memname)

#def raqspecs():
#    '''Record racqet specifications.'''
#    racquet=[]
#    rqspecs=input(str('Enter racquet specs in format of: Make/Model/Headsize '))
#    racquet.append(rqspecs)
#    return racquet

def raqspecs():
    '''Record racqet specifications.'refactored from list appending to tuple unpacking...simpler, probably faster '''
    raqmake,raqmodel,raqsize=input('raquet make?  '),input('raquet model?  '),input('raqheadsize?  ')
    return str.capitalize(raqmake),str.capitalize(raqmodel),int(raqsize)

def raq_make():
	raq_manuf=input ('who is the racquet manufacturer?')
	return raq_manuf
		
def raq_model():
	raq_mod=input ('what is the racquet make?')
	return raq_mod
				
def raq_head():
	head_size=input ('what is raquet head size?  ')
	return head_size


file_exists=os.path.isfile('RACQUETRENTAL.csv')

with open ('RACQUETRENTAL.csv','a', newline='') as csvfile:
#function open ('filename.CSV),r-read,w-write-a-append (add to) as filetype csvfile:
    fieldnames = ['RENTAL DATE','STAFF INIT','MEMBER NAME','RACQUET MAKE','RACQUET MODEL','RACQUET HEAD']
#fieldnames defines ROW 1 in spreadsheet, column headers in single quotes in form of a list
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#dictwriter is a dictionary utility function for python csv files...transcribes a dictionary to csv file
    writer.writeheader()
#if this line not included, will take first line of data as ROW...is optional
    for i in range (0,rentals):
        writer.writerow(({'RENTAL DATE':dateout(),'STAFF INIT':staffname(),'MEMBER NAME':mbrname(),'RACQUET MAKE':raq_make(),'RACQUET MODEL':raq_model(),'RACQUET HEAD':raq_head()}))
        