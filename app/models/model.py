# weeks = (years * 52) + (months * 4)

def weeksLeft(gYear, gMonth, cYear, cMonth):
    years = int(gYear) - int(cYear)
    months = int(gMonth) - int(cMonth)
    weeks = (years * 52) + (months * 4)
    print(weeks)
    return weeks
    
# weeksLeft()

def equation(weeksAmount, tuition):
    weekly = int(tuition) / int(weeksAmount)
    weekly = round(weekly, 2)
    print(weekly)
    return weekly
# print("You need to save " + str(round(weekly, 2)) + " every week.")




