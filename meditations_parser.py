import re

def format_quote(quote):
    quote = quote.replace('\n', '')
    return f'{quote.strip()}|Marcus Aurelius|Meditations, Book {current_book}\n'

meditations = open('meditations.txt', 'r')
output = open('meditations_quotes.txt', 'w')
lines = meditations.readlines()

digit_regex = re.compile(r'[0-9]+\.')

first_quote_found = False
all_quotes = []
current_book = 0
current_quote = ''
for line in lines:
    # Check if new book
    words = line.split(' ')
    if len(words) > 0 and words[0] == 'Book':
        current_book = int(words[1])
        continue

    # Check if starts with digit.
    match = digit_regex.search(line)
    if match is not None:
        if first_quote_found == False:
            first_quote_found = True
        else:
            formatted_quote = format_quote(current_quote)
            all_quotes.append(formatted_quote)
            output.write(formatted_quote)
        current_quote = line
    else:
        current_quote += line

for i in range(0, 150):
    tokens = all_quotes[i].split('|')
    print(f'{tokens[0]}\n~ {tokens[1]} ({tokens[2]})\n\n\n')
