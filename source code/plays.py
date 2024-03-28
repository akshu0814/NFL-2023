import mysql.connector
import csv

# connect to MySQL database
conn = mysql.connector.connect(user='axp2333', password='bUc@Nyix6t5h',host='academicmysql.mysql.database.azure.com', database='axp2333')
cursor = conn.cursor()

# mention the path to csv file
path = 'plays.csv'

# reading the csv file content
with open(path) as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # skip the header row

    # read the csv file and insert it into database
    for row in csv_reader:
        sql = "INSERT INTO plays (gameId, playId, playDescription, quarter, down, yardsToGo, possessionTeam, defensiveTeam, yardlineSide, yardlineNumber, gameClock, preSnapHomeScore, preSnapVisitorScore, passResult, penaltyYards, prePenaltyPlayResult, playResult, foulName1, foulNFLId1, foulName2, foulNFLId2, foulName3, foulNFLId3, absoluteYardlineNumber, offenseFormation, personnelO, defendersInBox, personnelD, dropBackType, pff_playAction, pff_passCoverage, pff_passCoverageType) VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s)"
        data = (int(row[0]), int(row[1]), row[2], (row[3]), (row[4]), (row[5]), (row[6]),(row[7]),(row[8]),(row[9]),(row[10]),(row[11]),(row[12]),(row[13]),(row[14]),(row[15]),(row[16]),(row[17]),(row[18]),(row[19]),(row[20]),(row[21]),(row[22]),(row[23]),(row[24]),(row[25]),(row[26]),(row[27]),(row[28]),(row[29]),(row[30]),(row[31]))
        cursor.execute(sql, data)

# commit the cursor and connection
conn.commit()
cursor.close()
conn.close()
