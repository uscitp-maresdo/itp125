Avengers = {'Clint Barton': 'Present', 'Natasha Romanov': 'Absent', 'Steve Rogers': 'Taken over by Hydra',
            'Carol Danvers': 'Present'}

print ("Avengers Assemble! Is everyone here?")

for stuff in Avengers:
    print ("Is " + stuff + " here?")

    if Avengers[stuff] == 'Present':
        print("Present")

    else:
        print("Eaten by the cookie monster")
        break