class Books:
    def __init__(self,bName,aName):
        self.bn = bName
        self.an = aName
        self.isTaken = False
        self.takenBy = None
        self.returnBy = None

class Library:
    def __init__(self):
        self.books = []

    def add(self,bName,aName):
        book = Books(bName,aName)
        self.books.append(book)

    def Show(self):
        for b in self.books:
            print(b.bn,b.an)
    
    def isAvailable(self,bName):
        isAvailableBook = None
        for b in self.books:
            if bName == b.bn:
                isAvailableBook = b
        
        if isAvailableBook is None:
            print(f"The {bName} is Unavailable in Library")
            return False
        
        else:
            print(f"The Book is '{bName}' is Available")
            return True
        
    def Borrow(self,bName,name,returnDate = "2 Days"):
        if self.isAvailable(bName) is False:
            return
        
        isAvailableBook = None
        for b in self.books:
            if bName == b.bn:
                isAvailableBook = b

        isAvailableBook.isTaken = True
        isAvailableBook.takenBy = name
        isAvailableBook.returnBy = returnDate

        print(f"The Book Name {bName} is taken By {name} and will be Return Date by {returnDate}")
        return
    
    def RetrunBook(self,bName):
        isAvailableBook = None
        for b in self.books:
            if bName == b.bn:
                isAvailableBook = b

        isAvailableBook.isTaken = False
        isAvailableBook.takenBy = None
        isAvailableBook.returnBy = None

        print(f"The Book {bName} is Return ")

l = Library()
l.add("The 48 Law of Power ","Robert Grene")
l.Show()
l.isAvailable("The 48 Law of Power ")
l.Borrow("The 48 Law of Power","Arshad","3 Days")
l.RetrunBook("The 48 Law of Power ")
l.isAvailable("The 48 Law of Power ")