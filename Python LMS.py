import datetime
import os
# os.getcwd()

class LMS:
    """ This class is used to keep record of books library.
    It has total four module: "Display Books", "Issue Books", "Return Books", "Add Books" """
    def __init__(self,list_of_books, library_name):
        self.list_of_books = "List_of_books.txt"
        self.library_name = library_name
        self.books_dict = {}
        Id = 101
        with open(self.list_of_books,"r") as bk:
           content = bk.readlines()
        for line in content[1:]:  # skip header row
            parts = line.strip().split()
            
        # Book name may have multiple words → join everything between index 1 and -4
        book_name = " ".join(parts[1:-4])  

        self.books_dict.update({
            str(Id): {
                "books_title": book_name,
                "lender_name": "",
                "Issue_data": "",
                "Status": "Available"
            }
        })
        Id += 1

    def display_books(self):
        print("---------------------------List of Books---------------------------")
        print("Books ID", "\t","Title")
        print("-------------------------------------------------------------------")
        for key, value in self.books_dict.items():
            print(key,"\t\t",value.get("books_title",), "- [",value.get("status"),"]")



    def Issue_books(self):
        books_id = input("Enter books ID: ")
        current_data = datatime.datatime.now().strtime("%Y-%m_%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]["Status"] == "Available":
                print(f"This books is already issued to {self.books_dict[books_id]["lender_name"]} \
                       on {self.books_dict[books_id]["Issue"]}")
                return self.Issue_books()
            elif self.books_dict[books_id]['Status'] == "Available":
               your_name = input("Enter your name: ")
               self.books_dict[books_id]['lender_name'] = your_name
               self.books_dict[books_id]['Issue_date'] = current_date
               self.books_dict[books_id]['Status'] = "Already Issued"
               print("Books Issued Successfully !!! \n")
        else:
            print("Books ID not found !!!")
            return self.Issue_books()
        
    def add_books(self):
        new_books = input("Enter books title: ") 
        if new_books == "":
            return self.add_books() 
        elif le(new_books) > 25:
            print("Books title length is too long!!! Title length should be 20 chars")
            return self.add_books()
        else:
            with open(self.list_of_books,"a") as bk:
                bk.writelines(f"{new_books}\n")
                self.books_dict.update({str(int(max(self.books_dict)) + 1): {"Books_title": new_books, "Lender_name": "", "Issue date": "", "Status": "Available"}})
                print(f"This books '{new_books}' has been added successfully !!!")
    def return_books(self):
        books_id = input("Enter books ID:")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["Status"] == "Available":
                print("This book is already available in library. Please check your book ID.")
                return return_books()
            elif not self.books_dict[books_id]["Status"] == "Available":
                self.books_dict[books_id]["lender_name"] = ""
                self.books_dict[books_id]["Issue_date"] = ""
                self.books_dict[books_id]["status"] = "Available"
                print("Successfully updated !!! \n")
            else:
                print("Book ID is not found")    




try:
    myLMS = LMS("list_of_books.txt","Python's")
    press_key_list = {"D": "Display Books","I":"Issue Books","A": "Add Books","R":"Return Books","Q":"Quit"}
    key_press = False
    while not (key_press == "q"): 
        print(f"\n---------------welcome To {myLMS.library_name} Library management system---------\n")
        for key, value in press_key_list.items():
            print("press", key, "To", value)
            key_press = input("press key: ").lower()
            if key_press =="i":
                print("\nCurrent Selection : Issue Books\n")
                myLMS.Issue_books()
            elif key_press == "a":
                print("\nCurrent Selection : Add books\n")
                myLMS.addd_books()
            elif key_Press == "d":
                print("\nCurrent Selection : Display books\n")
                myLMS.display_books()
            elif key_press == "r":
                print("\ncurrent Selection : Return Books\n")
                myLMS.return_books()
            elif key_press == "q":
                break
            else:
                continue


except Exception as e:
    print("something went wrong. please check your input !!!")                






l = LMS("List_of_books.txt","Python's Library")
print(l.display_books())