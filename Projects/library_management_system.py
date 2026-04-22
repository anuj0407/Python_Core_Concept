# Making a Library Management System using OOPs
from abc import ABC, abstractmethod
from datetime import datetime, timedelta

#abstract class 
class Media(ABC):
    def __init__(self, title,id_number):
        self.id_number = id_number
        self.title = title
        self._is_available = True
        self._return_date = None

    @property
    def check_availability(self): # property decorator to check the availability of media
        return self._is_available
    
    @abstractmethod
    def borrowing_duration(self): # abstract method to define the loan period for different media types
        pass

    def __str__(self):
        if(self.check_availability):
            return f"{self.title} (ID: {self.id_number})"
        else:
            return f"{self.title} (ID: {self.id_number}) - Due: {self._return_date.strftime('%d-%m-%y')}"
        
class Book(Media):
    def borrowing_duration(self):
        return 14
    
class DVD(Media):
    def borrowing_duration(self):
        return 7
    
class Magazine(Media):
    def borrowing_duration(self):
        return 2
    
class Library:
    def __init__(self):
        self.media_list = []
        self.borrow_media_list = []
        print("-------Welcome to the Library Management System!-------")

    def __len__(self):
        return len(self.media_list) 
    
    def add_media(self,media):
        self.media_list.append(media)

    def borrow_media(self, id_number):
        for media in self.media_list:
            if media.id_number == id_number:
                if media.check_availability:
                    self.media_list.remove(media)
                    self.borrow_media_list.append(media)
                    media._is_available = False
                    media._return_date = datetime.now() + timedelta(days = media.borrowing_duration())
                    print(f"you borrowed title: {media.title} | return date:{media._return_date}.")
                    return
        for media in self.borrow_media_list:
            if media.id_number == id_number:
                print(f"Sorry, '{media.title}' is currently not available. It is due on {media._return_date}.")
                return
        print(f"Sorry, media with ID {id_number} not found.")
    
    def return_media(self, id_number):
        for media in self.borrow_media_list:
            if media.id_number == id_number:
                self.borrow_media_list.remove(media)
                self.media_list.append(media)
                media._is_available = True
                print(f"You have returned title: {media.title} | Thank you!")
                return
        print(f"Sorry, media with ID {id_number} not borrowed .")


# System use

library = Library()

library.add_media(Book("The Great Gatsby", "B1452"))
library.add_media(DVD("Inception", "D1453"))
library.add_media(Magazine("National Geographic", "M1454"))
library.add_media(Book("Python Programming", "B1455"))
print()
print(f"Total media in library: {len(library)}") # total meidia before borrowing
library.borrow_media("B1455")
print(f"Total media in library: {len(library)}") # total media after borrowing
print()
for media in library.media_list + library.borrow_media_list:
    print(media)
print()
library.borrow_media("B1455")
library.return_media("B1455")
print(f"Total media in library: {len(library)}") # total media after returning



