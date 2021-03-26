
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def first_letter(word):
    if word[0] == 'R':
        return word

resulting_names = list(filter(first_letter, all_names))
print(resulting_names)




