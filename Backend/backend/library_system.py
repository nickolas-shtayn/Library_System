from cli import print_menu, add_book, remove_book, view_books, borrow_book, return_book


def main():
    while True:
        choice = print_menu()

        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            view_books()
        elif choice == '4':
            borrow_book()
        elif choice == '5':
            return_book()
        elif choice == '6':
            print("Exiting Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
