# Esercizio n°3 del Capitolo 2:

# Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
# If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm).
# Write a Python program to solve the general version of the above problem.
# Ask the user for the time now (in hours), and then ask for the number of hours to wait for the alarm.
# Your program should output what the time will be on the clock when the alarm goes off.

# Svolgimento:

time = input("Che ore sono? ")
time = float(time)
alarm = input("Tra quante ore suona la sveglia? ")
alarm = float(alarm)
# "float" per permettere anche le frazioni di ora.
clock_alarm = alarm % 24
new_time = time + clock_alarm
new_time = new_time % 24
print("La sveglia suonerà alle", new_time)


# --------------------------------------------------#
# --------------------------------------------------#


# Esercizio n°4 del Capitolo 2:

# It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is Saturday.
# If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return home
# after 10 nights you would return home on a Saturday (day 6).
# Write a general version of the program which asks for the starting day number, and the
# length of your stay, and it will tell you the number of day of the week you will return on.

# Commentata c'è una soluzione che fa uso delle liste, in maniera tale da restituire un giorno
# della settimana e non un numero.
# Svolgimento:

# week_day = ["Domenica", "Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato"]
print("Quale giorno della settimana è prevista la partenza?")
starting_day = input("Seleziona un numero da 0 (Domenica) a 6 (Sabato). ")
starting_day = int(starting_day)
number_of_nights = input("Quante notti trascorrerai in viaggio? ")
number_of_nights = int(number_of_nights)
returning_day = (number_of_nights + starting_day) % 7
# print("Tornerai ", week_day[returning_day])
print("Tornerai il gionro", returning_day)


# --------------------------------------------------#
# --------------------------------------------------#


# Esercizio n°7 del Capitolo 2:

# Write a Python program that assigns the principal amount of 10000 to variable P,
# assign to n the value 12, and assign to r the interest rate of 8% (0.08).
# Then have the program prompt the user for the number of years, t, that the money will be compounded for.
# Calculate and print the final amount after t years.

# Svolgimento:

P = 10000
n = 12
r = 0.08
t = input("Inserisci il numero di anni: ")
t = float(t)
A = P*(1 + r/n)**(n*t)
print("Il risultato finale è:", A)
