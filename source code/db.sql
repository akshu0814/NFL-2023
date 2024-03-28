CREATE TABLE games (
  gameId INT PRIMARY KEY,
  season INT,
  week INT,
  gameDate VARCHAR(10),
  gameTimeEastern TIME,
  homeTeamAbbr CHAR(3),
  visitorTeamAbbr CHAR(3)
);

CREATE TABLE players (
  nflId INT PRIMARY KEY,
  height VARCHAR(10),
  weight INT,
  birthDate VARCHAR(10),
  collegeName VARCHAR(255),
  officialPosition VARCHAR(10),
  displayName VARCHAR(255)
);

CREATE TABLE plays (
  gameId INT NOT NULL,
  playId INT NOT NULL,
  playDescription TEXT,
  quarter INT,
  down INT,
  yardsToGo INT,
  possessionTeam VARCHAR(3),
  defensiveTeam VARCHAR(3),
  yardlineSide VARCHAR(3),
  yardlineNumber INT,
  gameClock VARCHAR(10),
  preSnapHomeScore INT,
  preSnapVisitorScore INT,
  passResult VARCHAR(2),
  penaltyYards VARCHAR(10),
  prePenaltyPlayResult INT,
  playResult VARCHAR(10),
  foulName1 VARCHAR(255),
  foulNFLId1 VARCHAR(10),
  foulName2 VARCHAR(255),
  foulNFLId2 VARCHAR(10),
  foulName3 VARCHAR(255),
  foulNFLId3 VARCHAR(10),
  absoluteYardlineNumber VARCHAR(10),
  offenseFormation VARCHAR(255),
  personnelO VARCHAR(255),
  defendersInBox VARCHAR(10),
  personnelD VARCHAR(255),
  dropBackType VARCHAR(255),
  pff_playAction BINARY,
  pff_passCoverage VARCHAR(255),
  pff_passCoverageType VARCHAR(255),
  PRIMARY KEY(gameId, playId),
  FOREIGN KEY(gameId) REFERENCES games(gameId)
);



CREATE TABLE scouting (
    gameId INT NOT NULL,
    playId INT NOT NULL,
    nflId INT NOT NULL,
    pff_role VARCHAR(50),
    pff_positionLinedUp VARCHAR(50),
    pff_hit VARCHAR(50),
    pff_hurry VARCHAR(50),
    pff_sack VARCHAR(50),
    pff_beatenByDefender VARCHAR(50),
    pff_hitAllowed VARCHAR(50),
    pff_hurryAllowed VARCHAR(50),
    pff_sackAllowed VARCHAR(50),
    pff_nflIdBlockedPlayer VARCHAR(50),
    pff_blockType VARCHAR(50),
    pff_backFieldBlock VARCHAR(50),
    PRIMARY KEY (gameId, playId, nflId),
    FOREIGN KEY (gameId, playId) REFERENCES plays(gameId, playId),
    FOREIGN KEY (nflId) REFERENCES players(nflId)
);


CREATE TABLE tracking (
  gameId INT,
  playId INT,
  nflId VARCHAR(5),
  frameId INT,
  time TIMESTAMP,
  jerseyNumber VARCHAR(10),
  team VARCHAR(10),
  playDirection VARCHAR(10),
  x DECIMAL(5,2),
  y DECIMAL(5,2),
  s DECIMAL(5,2),
  a DECIMAL(5,2),
  dis DECIMAL(5,2),
  o VARCHAR(10),
  dir VARCHAR(10),
  event TEXT
 );

