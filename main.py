#Make a dictionary called "cities". 
#Use the names of three cities as keys in your dictionary.
#Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city.
#The keys for each city's dictionary should be something like "country, population, and fact".
#Print the name of each city and all of the information you have stored about it.Make sure the final output is nicely formatted and neat.

cities={
    'Bergamo': {
        'country':'Italy',
        'population':'918,675',
        'fact':'it has an ancient elevated part of the city',
    },

    'Bari':{
        'country':'Italy',
        'population':'623,000',
        'fact':'Bari is a bustling commercial center and port.',
    },

    'Roma':{
        'country':'Italy',
        'population':'4,331,970',
        'fact':'Rome has the famous Colosseum',
    },

    }
for city,information in cities.items():
    print('')
    print('city and some information about it: ')
    print(city)
    for type,info in information.items():
        print(f'{type}: {info}')
        
