from datetime import date


def checkio(from_date, to_date):
    number_of_days = (to_date - from_date).days + 1         # +1 to include start day
    start_day = from_date.weekday()
    remainder = number_of_days % 7

    complete_cycles_rest_days = number_of_days // 7 * 2     # each seven day cycle includes 2 rest days
    incomplete_cycle_rest_days = 0

    if start_day + remainder == 6:
        incomplete_cycle_rest_days = 1
    elif start_day + remainder > 6:
        incomplete_cycle_rest_days = 2
        if start_day == 6:
            incomplete_cycle_rest_days -= 1

    return complete_cycles_rest_days + incomplete_cycle_rest_days

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"
