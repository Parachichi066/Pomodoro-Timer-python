import random

class Motivation:
    def get_motivation(self):
        try:
            with open("motivational_quotes.txt", "r", encoding="utf-8") as file:
                delimiter = ":"

                raw_quotes  = file.read()
                quotes_list = []

                for quote in raw_quotes.split(delimiter):
                    quotes_list.append(quote.strip())

                return random.choice(quotes_list)
        except FileNotFoundError:
            print("motivational_quotes.txt was not found!")