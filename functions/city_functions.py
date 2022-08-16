# module de l'exercice 13.1
def get_city_country(city, country, population=''):
    the_city = city.lower().title()
    the_country = country.lower().title()
    if population:
        return f"{the_city}, {the_country} - population: {population}"
    else:
        return f"{the_city}, {the_country}"
        