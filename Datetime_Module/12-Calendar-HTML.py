# Insert calendar in HTML page
import calendar
c = calendar.HTMLCalendar()
print(c.formatmonth(2023, 3))

# create a HTML file --> month format
f = open("d:\\cal1.html", "w")
print(f.write(c.formatmonth(2023, 3)))
print(f.close())

# year format
f = open("d:\\cal2.html", "w")
print(f.write(c.formatyear(2023)))
print(f.close())