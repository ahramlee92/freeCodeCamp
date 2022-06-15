def add_time(start, duration, startingDay=""):
    # Split time
    # Hours equals time[0], minutes equals time[1]
    start = start.split()
    amPm = start[1]
    time = start[0].split(":")

    # Split duration
    # Hours equals durTime[0], minutes equals durTime[1]
    durTime = duration.split(":")

    # Check time is am or pm
    if amPm == "PM":
        time[0] = int(time[0]) + 12

    addHours = int(time[0]) + int(durTime[0])
    addMins = int(time[1]) + int(durTime[1])

    # Check minutes
    if addMins >= 60:
        minsToHours = addMins // 60
        addHours = addHours + minsToHours

        addMins -= 60

    # Check time is over one day
    daysAdd = 0
    if addHours > 24:
        daysAdd = addHours // 24
        addHours -= daysAdd * 24

    # set AM/PM
    if 0 < addHours < 12:
        amPm = "AM"
    elif addHours == 12:
        amPm = "PM"
    elif addHours > 12:
        amPm = "PM"
        addHours -= 12
    else:
        amPm = "AM"
        addHours += 12

    daysLater = ""
    if daysAdd > 0:
        if daysAdd == 1:
            daysLater = " (next day)"
        else:
            daysLater = " (" + str(daysAdd) + " days later)"

    dayOfWeek = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    if startingDay:
        weeks = daysAdd // 7
        num = dayOfWeek.index(startingDay.lower().capitalize()) + (daysAdd - 7 * weeks)
        if num > 6:
            num -= 7
        day = ", " + dayOfWeek[num]
    else:
        day = ""

    new_time = str(addHours) + ":" + \
               (str(addMins) if addMins > 9 else ("0" + str(addMins))) + \
               " " + amPm + day + daysLater


    return new_time