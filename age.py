from datetime import datetime


def age():
    current_date = datetime.today()
    given_input = input('Please input a date in the form DD/MM/YYYY: ')
    given_date = datetime.strptime(given_input, '%d/%m/%Y')
    difference = current_date - given_date
    difference_years = int(difference.days // 365.2425)
    return difference_years


if __name__ == "__main__":
    print(age())
