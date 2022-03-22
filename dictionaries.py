monthConversion = {"Jan": "January",
                   "Feb": "February",
                   "Mar": "March",
                   "Apr": "April",
                   "May": "May",
                   "Jun": "June",
                   "Jul": "July",
                   "Aug": "August",
                   "Sep": "September",
                   "Oct": "October",
                   "Nov": "November",
                   "Dec": "December",}
# Declaration
print(monthConversion.get("Odt", "Not a valid month"))
# Here we are defining a default value "Not a valid month, so if the key is incorrect it will print default key instead of None
