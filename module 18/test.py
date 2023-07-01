from operator import le
from re import T
from traceback import print_tb
class Star_Cinema:
   hall_list = []
 
   def entry_hall(self, hall_obj):
       self.hall_list.append(hall_obj)
 
class Hall(Star_Cinema):
   def __init__(self, seats, show_list, rows, cols, hall_no):
       self.seats = seats
       self.show_list = show_list
       self.rows = rows
       self.cols = cols
       self.hall_no = hall_no
     
       self.entry_hall(Hall)
     
   def entry_show(self, id, movie_name, time):       
       show = (id, movie_name, time)
       self.show_list.append(show)
       self.seats[id] = [[i, j] for i in range(self.rows) for j in range(self.cols)]
     
   def book_seats(self, name, phone, id_of_show):
       m = '' 
       if id_of_show == '#34':
           m = self.show_list[0]
       elif id_of_show == '#45':
           m = self.show_list[1]
       else:
           print("-"*40)
           print("show id is wrong")
           print("-"*40)
           return
     
       t = []
       total_seat = int(input("ENTER NUMBER OF TICKET: "))
       for i in range(total_seat):
           seat = input("ENTER SEAT NO: ")
           if seat.upper() in self.seats[id_of_show]:
               print('ALREADY, THIS SEAT HAS BEEN  BOOKED')
           else:
               t.append(seat.upper())
     
       for i in t:
           if len(i) > 2 or  ord(i[0]) - 65 >= self.rows or  int(i[1]) >= self.cols:
               print('invalid seats...')
               return
     
       seats = []
       for i in t:
           a = ((ord(i[0]) - 65), int(i[1]))
           seats.append(a)
         
       for seat in seats:
           if list(seat) in self.seats[id_of_show]:
               print('booking successfully')
           else:
               print('-'*40)
               print('booked already')
               print('-'*40)
               return
     
       t1 = " ".join(t)
     
       for i in seats:
           for j, value in enumerate(self.seats[id_of_show]):
               if value == list(i):
                   self.seats[id_of_show][j] = ['X']
             
           
       print(f"\t{'#'*5} Ticket booked successfully {'#'*5}")
       print('-'*50)
     
       print(f'NAME: {name.upper()}')
       print(f'PHONE NUMBER: {phone}')
       print(f'MOVIE NAME: {m[1]} \t\t MOVIE TIME:{m[2]}')
       print(f"TICKETS: {t1}")
       print(f"HALL: {self.hall_no}")
     
       print()
               
   def view_show_list(self):
       print("-"*80)
       print()
     
       for i in self.show_list:
           print(f"MOVIE NAME: {i[1]} \t SHOW ID: {i[0]} \t TIME: {i[2]}")
         
       print()
       print("-"*80)
     
   def view_available_seats(self, show_id):
       movie_information = []
       for show in self.show_list:
           if show_id == show[0]:
               movie_information.append(show[1])
               movie_information.append(show[2])
             
       print()
     
       if len(movie_information) <= 0:
           print("-"*30)
           print('MOVEI ID INVALID')
           print("-"*30)
           return
     
     
       print(f"MOVIE NAME: {movie_information[0]}\t\t TIME: {movie_information[1]}")
       print("X for Already booked ")
     
       all_seats = self.seats[show_id]
       count = 0
     
       print("-"*50)
       print()
     
       for i in range(self.rows):
           for j in range(self.cols):
               if len(all_seats[count]) == 2:
                   print(f"{chr(65 + i)}{j} \t", end=" ")
                   count += 1
               else:
                   print(f"{all_seats[count][0]} \t", end=" ")
                   count += 1
           print()
         
       print()
       print("-"*50)
     
hall_1 = Hall(rows=5, cols=5, hall_no='A10', seats={}, show_list=[])
hall_1.entry_show('#34', 'Hawa', 'Oct 26 2022 9:00 AM')
hall_1.entry_show('#45', 'hazar bochor Dhore', 'Oct 27 2022 08:30 PM')
 
while True:
   print("1. VIES ALL SHOWS TODAY")
   print("2. VIEW AVAILABLE SEATS")
   print("3. BOOK TICKETS")   
 
   option = int(input("ENTER OPTION: "))
   if option == 1:
       hall_1.view_show_list()
     
   elif  option == 2:
       show_id = input('ENTER SHOW ID: ')
       hall_1.view_available_seats(show_id)
     
   elif option == 3:
       name = input('ENTER YOUR NAME: ')
       phone = input('ENTER YOUR PHONE: ')
       show_id = input('ENTER SHOW ID: ')
       hall_1.book_seats(name, phone, show_id)
 

"""
3
sabbir
57349857
#34
1
a0
"""
