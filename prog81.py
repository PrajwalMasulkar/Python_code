# display year and name of weekday using built-in module

import datetime

x=datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))