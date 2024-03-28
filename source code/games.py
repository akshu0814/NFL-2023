import mysql.connector
import csv

#connection to Mysql database
conn = mysql.connector.connect(user='axp2333', password='bUc@Nyix6t5h',host='academicmysql.mysql.database.azure.com', database='axp2333')
cursor = conn.cursor()

# mention the path to csv file
path = 'games.csv'

# reading the csv file content
with open(path) as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    # read the csv file and insert it into database
    for row in csv_reader:
        sql = "INSERT INTO games (gameId, season, week, gameDate, gameTimeEastern, homeTeamAbbr, visitorTeamAbbr) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (int(row[0]), int(row[1]), int(row[2]), row[3], row[4], row[5], row[6])
        cursor.execute(sql, data)

# commit the cursor and connection
conn.commit()
cursor.close()
conn.close()
