class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    def __str__(self):
        return f"Title:{self.title},Author:{self.author},ISBN:{self.isbn}"
class User:
    def __init__(self,name,user_id):
        self.name = name
        self.user_id= user_id
class Library:
    
    def __init__(self,book,user):
        self.book = book
        self.user= user
        self.borrowed = []
    def add_book(self,book):
        self.book.append(book)
        print("Book has been added")
    def display_books(self):
        for i in self.book:
            print(i)
            
    def borrow_book(self,user,isbn):
        self.userids = [u.user_id for u in self.user]
        if user.user_id in self.userids:
            for book in self.book:
                if(book.isbn == isbn):
                    self.borrowed.append(book)
                    print("Thank you for being a member of our library club")
                    print(f"Book with isbn:{book.isbn} has been borowed by {user.name}")
                    self.book.remove(book)
                    break
            else:
                print("The book with the ISBN id is not available")
        else:
            print("Welcome to the club sir")
            for book in self.book:
                if(book.isbn == isbn):
                    self.borrowed.append(book)
                    print("Thank you for being a member of our library club")
                    print(f"Book with isbn:{book.isbn} has been borowed by {user.name}")
                    self.book.remove(book)
                    break
                    
            else:
                print("The book with the ISBN id is not available")
    def return_book(self,user,isbn):
        for book in self.borrowed:
            if isbn == book.isbn:
                self.book.append(book)
                print("The book has been returned")
                break
            else:
                if isbn in [book.isbn for book in self.book]:
                    print("The book with the ISBN id is already available")
                    break
                else:
                    print("The book with the isbn is not available")
b1 = Book("Harrypotter","JK.Rowling",3050)
b2 = Book("Bahubali","Sivaraman",3550)
u1 = User("ravi",111)
u2 = User("raju",112)
lib1 = Library([b1,b2],[u1,u2])
while(True):
    opt = input("What do you want to do?\nAddbook-(a/A)\nDisplaybooks-(d/D)\nBorrowbook-(b/B)\nReturnbook-(r/R)").lower()
    if opt  not in ['a','b','d','r']:
        while(True):
            opt = input("Choose a valid option(a,b,d,r)").lower()
            if opt in ['a','b','d','r']:
                break
    if opt == 'a':
        title,author,isbn = input("Enter the title,author,isbn of the book you want to add").split(',')
        isbn = int(isbn)
        b = Book(title,author,isbn)
        lib1.add_book(b)
    if opt == 'b':
        user,userid = input("Enter your name and your id").split(',')
        userid = int(userid)
        u  = User(user,userid)
        ibn = int(input("Enter the isbn of the book"))
        lib1.borrow_book(u,ibn)
    if opt == 'd':
        lib1.display_books()
    if opt == 'r':
        user,userid = input("Enter your name and your id").split(',')
        userid = int(userid)
        u  = User(user,userid)
        ibn = int(input("Enter the isbn of the book"))
        lib1.return_book(u,ibn) 
    opt2= input("Do you want to continue(Press enter) or exit(n\\N):")
    if opt2 in ['N','n']:
        print("Okay bye.Thanks for the visit")
        break
    
    
    
    
    
    
    
    
            
        
    
        
