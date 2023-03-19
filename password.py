import random
import string
from colorama import init, Fore, Style
init()

import pyfiglet
from colorama import init, Fore, Style
init()

# Generate ASCII art of "Strong password generator" with large letters
ascii_text = pyfiglet.figlet_format("Strong password generator by m_dev")

# Set the color of the ASCII art to green
colored_ascii_text = Fore.GREEN + ascii_text + Style.RESET_ALL

# Print the colored ASCII art
print(colored_ascii_text)

def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.sample(characters, length))

    return password
n=int(input('Enter the length of password:  '))
password = generate_password(n)
print(Fore.GREEN + "Generated password: " + Style.RESET_ALL,end='')
print(password)
