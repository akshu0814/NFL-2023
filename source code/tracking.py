import mysql.connector
import csv

# connect to MySQL database
conn = mysql.connector.connect(user='axp2333', password='bUc@Nyix6t5h',host='academicmysql.mysql.database.azure.com', database='axp2333')
cursor = conn.cursor()

# mention the path to csv file
path = 'tracking1.csv'

# reading the csv file content
with open(path) as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # skip the header row

    # read the csv file and insert it into database
    for row in csv_reader:
        sql = "INSERT INTO tracking (gameId, playId, nflId, frameId, time, jerseyNumber, team, playDirection, x, y, s, a, dis, o, dir, event) VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = ((row[0]), (row[1]), (row[2]), (row[3]), row[4], (row[5]), row[6], row[7], row[8], (row[9]), (row[10]), (row[11]), (row[12]), (row[13]), (row[14]), row[15])
        cursor.execute(sql, data)

# commit the cursor and connection
conn.commit()
cursor.close()
conn.close()
