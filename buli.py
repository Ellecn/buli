import argparse
import urllib.request
import json

parser = argparse.ArgumentParser(description="Buli - Football table command line tool", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-l", "--league", default="bl1", help="League: 'bl1', 'bl2', 'bl3'")
parser.add_argument("-s", "--season", default="2024", help="Season: '2022', '2021', ...")
config = vars(parser.parse_args())

class Team:
    def __init__(self, name, points, position):
        self.name = name
        self.points = points
        self.position = position
    def __str__(self):
        return "{} ({}.)".format(self.name, self.position)

def getTeamsWithPoints(points):
    return list(filter(lambda t: t.points == points, table))

table = []

url = "https://www.openligadb.de/api/getbltable/{}/{}".format(config['league'], config['season'])
with urllib.request.urlopen(url) as response:
    json_obj = json.load(response)
    position = 1
    for team in json_obj:
        table.append(Team(team['teamName'], team['points'], position))
        position += 1

for i in range(table[0].points, table[len(table)-1].points-1, -1):
    teamsString = " | ".join([str(elem) for elem in getTeamsWithPoints(i)])
    print("{:02d} Pkt: {}".format(i, teamsString))
