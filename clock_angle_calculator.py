def angle_calculation(hour, minute):
    try:
        hour = int(hour)
        if hour in range(0, 24):
            if hour in range(0, 12):
                pass
            else:
                hour -= 12
        else:
            print "Wrong format of hour"
            exit(1)
    except TypeError:
        print "Wrong format of hour"
        exit(1)

    try:
        minute = int(minute)
        if minute in range(0, 60):
            pass
        else:
            print "Wrong format of minute"
            exit(1)
    except TypeError:
        print "Wrong format of minute"
        exit(1)

    hour_degrees = 30
    hour_coefficient = 0.5
    minute_coefficient = 6

    hour_angle = hour * hour_degrees + minute * hour_coefficient
    minute_angle = minute * minute_coefficient
    return abs(hour_angle - minute_angle)


def main():
    try:
        hour, minute = raw_input("Please enter time (eq. 15:15): ").split(":")
        print "Angle between hour and minute hand is " + str(angle_calculation(hour, minute)) + " degrees."
    except ValueError:
        print "Wrong time format"

if __name__ == "__main__":
    main()
