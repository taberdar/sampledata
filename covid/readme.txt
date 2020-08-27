countrycodes.csv
Country code data
Country -> full name of the country
GeoId -> 2 letter geoid
Code -> 3 letter code

covid.csv
Snapshot of covid data on the 3rd July 2020

Index(['Date', 'Cases', 'Deaths', 'Population', 'GeoId', 'DeathsPerMillion',
       'CumulativeDeaths', 'CumulativeCases', 'CumulativeDeathsPerMillion',
       'CumulativeCasesPerMillion', 'Country', 'Code', 'DeathsRolling7Days',
       'DeathsPerMillionRolling7Days'],
      dtype='object')

covid_data.db
Sqlite database containing covid and countries data(original in docker-databases git repo) (use sqlitebrowser to view the database)
