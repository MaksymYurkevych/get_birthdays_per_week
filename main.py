from datetime import datetime, timedelta


def get_birthdays_per_week(birthday_list):
    """Gets list of dicts with name and birthday as keys and returns day of the week to congratulate a person"""
    today = datetime.now()
    end = today + timedelta(days=7)
    to_greet = {}
    for person in birthday_list:
        a_date = datetime.strptime(person['birthday'], "%d/%m/%Y")  # datetime object
        b_date = datetime(day=a_date.day, month=a_date.month, year=datetime.now().year)
        if today.strftime("%d/%m") <= b_date.strftime("%d/%m") <= end.strftime("%d/%m"):
            weekday_name = b_date.strftime("%A")  # name of the weekday
            number_of_weekday = b_date.isoweekday()  # number of day in the week

            if number_of_weekday > 5:
                weekday_name = 'Monday'

            to_greet[person['name']] = weekday_name

    present_week_days = [day for day in to_greet.values()]
    unique_week_days = set(present_week_days)

    full_dict = {}
    for day in unique_week_days:
        gr_list = []
        for name, weekday in to_greet.items():
            if weekday == day:
                gr_list.append(name)
                full_dict[day] = gr_list

    to_output = ""
    for day, name in full_dict.items():
        person_name = ""
        for n in name:
            if name[-1] == n:
                person_name += n
            else:
                person_name += n + ", "
        to_output += "".join((day + ": " + person_name)) + "\n"

    return print(to_output)


if __name__ == '__main__':
    birth_list = [{"name": "Yulia", "birthday": '06/12/1996'},
                  {"name": "Sarpl", "birthday": '07/12/1997'},
                  {"name": "Sunny", "birthday": '26/12/2000'},
                  {"name": "Luk", "birthday": '10/12/1995'},
                  {"name": 'Sim', "birthday": '12/12/1991'},
                  {"name": 'Nok', "birthday": '14/12/1994'},
                  {"name": 'Kred', "birthday": '13/12/1994'},
                  {"name": 'Tim', "birthday": '18/12/1997'},
                  {"name": 'Kooc', "birthday": '09/12/1997'}]
    get_birthdays_per_week(birth_list)
