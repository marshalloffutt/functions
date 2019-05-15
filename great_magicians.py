# 8-10

def make_great(magicians):
    # Make each magician great, and add to great_magicians
    while magicians:
        magician = magicians.pop()
        great_magician = magician.title() + ' the Great'
        great_magicians.append(great_magician)
    
    # Modify original list
    for great_magician in great_magicians:
        magicians.append(great_magician)

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

magicians = ['larry', 'gary', 'barry']
great_magicians = []

make_great(magicians)
show_magicians(magicians)