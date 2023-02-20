# films = []
# f_one_n = str(input('Film 1 name\n'))
# f_one_l = str(input('film 1 length\n'))
# f_one_y = int(input('Film 1 year\n'))
# f_one_r = float(input('Film 1 rate\n'))
#
# f_two_n = str(input('Film 2 name\n'))
# f_two_l = str(input('film 2 length\n'))
# f_two_y = int(input('Film 2 year\n'))
# f_two_r = float(input('Film 2 rate\n'))
#
# film_one = {'name': f_one_n, 'len': f_one_l, 'year': f_one_y, 'rate': f_one_r}
# film_two = {'name': f_two_n, 'len': f_two_l, 'year': f_two_y, 'rate': f_two_r}

# films.append(film_one)
# films.append(film_two)
# print('Your film list\n', films)

films = []
film_one = {}
film_two = {}
film_one["name"] = str(input('Film 1 name\n'))
film_one["len"] = str(input('film 1 length\n'))
film_one["year"] = int(input('Film 1 year\n'))
film_one["rate"] = float(input('Film 1 rate\n'))

film_two["name"] = str(input('Film 2 name\n'))
film_two["len"] = str(input('film 2 length\n'))
film_two["year"] = int(input('Film 2 year\n'))
film_two["rate"] = float(input('Film 2 rate\n'))

films.append(film_one)
films.append(film_two)

print('Your film list:\n', films)