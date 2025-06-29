from calendar import isleap # Importing "isleap" to check for leap years.
from datetime import datetime # Importing "datetime" to get the current date.

# Function to get the user's D.O.B without any errors.
def dob():
    while True:
        user_input = input("Enter your D.O.B like dd/mm/yyyy: ") # Asking user for their dob.
        data = user_input.split("/") # Spliting the data

        # Checking if the given format is correct or not.
        if len(data) != 3:
            print("Invalid format. Use dd/mm/yyyy.")
            continue

        try:
            day = int(data[0])
            month = int(data[1])
            year = int(data[2])

            if not (1000 <= year <= 9999):
                print("Year must be 4 digits.")
                continue

            # Validate and return as datetime object
            return datetime(year, month, day)

        except ValueError:
            print("Invalid date. Please try again.")

# Get user DOB
dob_date = dob()
today = datetime.now()

# Days lived
days_lived = (today - dob_date).days

# Approximate years
years_lived = days_lived // 365

# Months lived (approximate)
months_lived = (today.year - dob_date.year) * 12 + (today.month - dob_date.month)

# If the current day is less than birth day, subtract a month (still incomplete month)
if today.day < dob_date.day:
    months_lived -= 1

# List leap years
leap_years = [year for year in range(dob_date.year, today.year + 1) if isleap(year)]

# Output results
print(f"\nYou have lived for:")
print(f"  -> {days_lived} days")
print(f"  -> ~{months_lived} months")
print(f"  -> ~{years_lived} years")
print(f"Leap years in your lifetime: {leap_years}")
print(f"Total leap years: {len(leap_years)}")