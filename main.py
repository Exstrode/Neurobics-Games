import subprocess
from colorama import Fore, Style

# Define your options with the desired formatting
options = [
    f"{Fore.WHITE}[{Fore.BLUE}1{Fore.WHITE}]{Style.RESET_ALL} {Fore.RED}Guess the Number{Style.RESET_ALL}",
    f"{Fore.WHITE}[{Fore.BLUE}2{Fore.WHITE}]{Style.RESET_ALL} {Fore.RED}Math Game{Style.RESET_ALL}",
    f"{Fore.WHITE}[{Fore.BLUE}3{Fore.WHITE}]{Style.RESET_ALL} {Fore.RED}Say the Colour Not the Word{Style.RESET_ALL}",
    f"{Fore.WHITE}[{Fore.BLUE}4{Fore.WHITE}]{Style.RESET_ALL} {Fore.RED}Memory Game{Style.RESET_ALL}",
    f"{Fore.WHITE}[{Fore.BLUE}5{Fore.WHITE}]{Style.RESET_ALL} {Fore.RED}unknown{Style.RESET_ALL}\n\n"
]

# Create the menu by joining the options
menu = "\n".join(options)

while True:
    choice = input(menu)

    if choice == '1':
        # Execute guess.py
        subprocess.run(["python", "guess.py"])
    elif choice == '2':
        # Execute math.py
        subprocess.run(["python", "calc.py"])
    elif choice == '3':
        # Execute color.py
        subprocess.run(["python", "color.py"])
    elif choice == '4':
        # Execute letter.py
        subprocess.run(["python", "letter.py"])
    elif choice == 'q':
        break
    else:
        print("Invalid choice. Please enter '1' or '2' for the scripts or 'q' to quit.")
      
