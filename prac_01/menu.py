"""
function main()
    get name

    function display_menu()
        print("(H)ello")
        print("(G)oodbye")
        print("(Q)uit")

    display_menu()
    get choice

    while choice != 'Q'
        if choice == 'H'
            print(f"Hello {name}")
        elif choice == 'G'
            print(f"Goodbye {name}")
        else
            print("Invalid choice")

        display_menu()
        get choice
    print("Finished.")
main()
"""
def main():
    name = input("Enter name: ")

    def display_menu():
        print("(H)ello")
        print("(G)oodbye")
        print("(Q)uit")

    display_menu()
    choice = input(">>> ").upper()

    while choice != 'Q':
        if choice == 'H':
            print(f"Hello {name}")
        elif choice == 'G':
            print(f"Goodbye {name}")
        else:
            print("Invalid choice")

        display_menu()
        choice = input(">>> ").upper()
    print("Finished.")
main()
