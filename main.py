from interactive import *

def main():
    while True:
        showMenu()
        userChoice = int(input('Enter your choice: '))
        if userChoice == 0:
            break
        elif userChoice == 1:
            returnByGenre()


if __name__ == "__main__":
    main()
