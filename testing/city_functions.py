def get_formatted_name(city,country,population=0):
    if population:
        formatted_name = city + ', ' + country + ' - population ' + str(population)
    else:
        formatted_name = city + ', ' + country
    return formatted_name.title()