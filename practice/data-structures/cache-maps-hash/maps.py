# Code

locations = {
  'North America': {
    'USA': ['Mountain View', 'Atlanta']
  },
  'Asia': {
    'India': ['Bangalore'],
    'China': ['Shanghai']
  },
  'Africa': {
    'Egypt': ['Cairo']
  }
}
# TODO: Print a list of all cities in the USA in alphabetic order.
for city in locations['North America']['USA']:
    print(city)

# TODO: Print all cities in Asia, in alphabetic order, next to the name of the country
cities = []
for country in locations['Asia']:
    for city in locations['Asia'][country]:
        cities.append(f"{city} - {country}")
        
for city in sorted(cities):
    print(city)
