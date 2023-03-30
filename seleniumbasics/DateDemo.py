from datetime import date

today = date.today().strftime("%d-%b-%Y")
select_date = "14-Feb-2023"

if select_date >= today:
    print("valid Date")
else:
    print("Invalid Date")