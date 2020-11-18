meditations = open('meditations_quotes.txt', 'r').read().splitlines()

import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def format_quote(quote):
    [message, author, source] = quote.split('|')
    return f'{bcolors.OKCYAN}{message}{bcolors.ENDC}\n\t\t\t~ {bcolors.BOLD}{bcolors.WARNING}  {author}{bcolors.ENDC} {bcolors.OKBLUE}({source}){bcolors.ENDC}'

print(format_quote(random.choice(meditations)))