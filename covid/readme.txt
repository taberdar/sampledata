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

countries.db
Sqlite database containing country data (original in docker-databases git repo) (use sqlitebrowser to view the database)

covid.db
Sqlite database containing covid data (original in docker-databases git repo) (use sqlitebrowser to view the database)
