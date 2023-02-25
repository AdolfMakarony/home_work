from films import film_list

counts_list=[]
title_list_sw = []
title_list_the = []
year_list = []
my_film_list_year = []
my_film_list_rate = []
for film in film_list:
    if film['rating'] > 8.9:
        my_film_list_rate.append(film['title'])

    films_years = list(range(2003, 2005 + 1))
    if film['year'] in films_years:
        my_film_list_year.append(film['title'])

    year_list.append(film['year'])

    if 'the' in film['title']:
        title_list_the.append(film['title'])

    if 'Star Wars' in film['title']:
        result=[film['top 250 rank'], film['title']]
        title_list_sw.append(result)

my_film_list_rate_num = list(enumerate(my_film_list_rate, start=1))
print('\nSearch result, rate more 8.9:\n')
for film in my_film_list_rate_num:
    print(film[0], '. ', film[1])

my_film_list_year_num = list(enumerate(my_film_list_year, start=1))
print('\nSearch result, year 2003 - 2005:\n')
for film in my_film_list_year_num:
    print(film[0], '. ', film[1])

year_list = sorted(year_list)
year_list_set = set(year_list)
for year in year_list_set:
    counts = year_list.count(year)
    result = [year, counts]
    counts_list.append(result)
def custom_key(some):
    return some[1]
counts_list.sort(key=custom_key, reverse=True)
print('\n Most rated year is ', counts_list[0])

print(*title_list_the, sep='\n')

print(*title_list_sw, sep='\n')