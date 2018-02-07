import csv

with open('examples.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    # print(readCSV)
    
    Series = []
    EpisodeS1 = []
    EpisodeS2 = []

    for row in readCSV:
        # print(row)
        # print('============')
        # print(row[0],row[1])
        serie = row[0]
        season_1 = row[1]
        season_2 = row[2]

        Series.append(serie)
        EpisodeS1.append(season_1)
        EpisodeS2.append(season_2)

    print(Series)
    print(EpisodeS1)
    print(EpisodeS2)

    whatSeries = input('what series do you wish to know the last episode of first season?')
    Serdex = Series.index(whatSeries)
    print(whatSeries.lower())
    print('The last episode of', whatSeries, 'Season 1 is:', EpisodeS1[Serdex])
    

