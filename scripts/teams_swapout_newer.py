import os
import json


season = 0
write = True


seasondir = f'season{season}'

def _make_path(filename):
    return os.path.join(seasondir, filename)

oldteamsfile = _make_path('old_teams.json')
newteamsfile = _make_path('new_teams.json')
teamsfile    = _make_path('teams.json')
schedulefile = _make_path('schedule.json')
bracketfile  = _make_path('bracket.json')
seasonfile   = _make_path('season.json')
postfile     = _make_path('postseason.json')
seedfile     = _make_path('seed.json')

with open(oldteamsfile, 'r') as f:
    oldteams = json.load(f)
    
with open(newteamsfile, 'r') as f:
    newteams = json.load(f)

if len(oldteams) != len(newteams):
    raise Exception(f"Error: mismatch in number of teams in {oldteamsfile} and {newteamsfile}")

team_name_map = {}
team_abbr_map = {}
for oldteam in oldteams:
    old_name = oldteam['teamName']
    old_abbr = oldteam['teamAbbr']
    for team in newteams:
        if oldteam['teamColor'] == team['teamColor']:
            team_name = team['teamName']
            team_abbr = team['teamAbbr']
            team_name_map[old_name] = team_name
            team_abbr_map[old_abbr] = team_abbr
            break

if len(team_name_map) != len(oldteams):
    print([j['teamName'] for j in oldteams])
    print(list(team_name_map.keys()))
    raise Exception(f"Error: size mismatch in number of teams {len(oldteams)} and size of old-new mapping {len(team_name_map)}")




for team in oldteams:
    team['teamName'] = team_name_map[team['teamName']]

teams = oldteams

if write:
    with open(teamsfile, 'w') as f:
        json.dump(teams, f, indent=4)



with open(schedulefile, 'r') as f:
    schedule = json.load(f)

for day in schedule:
    for game in day:
        game['team1Name'] = team_name_map[game['team1Name']]
        game['team2Name'] = team_name_map[game['team2Name']]
        game['team1Abbr'] = team_abbr_map[game['team1Abbr']]
        game['team2Abbr'] = team_abbr_map[game['team2Abbr']]

if write:
    with open(schedulefile, 'w') as f:
        json.dump(schedule, f, indent=4)



with open(seasonfile, 'r') as f:
    season = json.load(f)

for day in season:
    for game in day:
        game['team1Name'] = team_name_map[game['team1Name']]
        game['team2Name'] = team_name_map[game['team2Name']]
        game['team1Abbr'] = team_abbr_map[game['team1Abbr']]
        game['team2Abbr'] = team_abbr_map[game['team2Abbr']]

if write:
    with open(seasonfile, 'w') as f:
        json.dump(season, f, indent=4)



with open(bracketfile, 'r') as f:
    bracket = json.load(f)

for series in bracket:
    miniseason = bracket[series]
    for day in miniseason:
        for game in day:
            try:
                game['team1Name'] = team_name_map[game['team1Name']]
                game['team2Name'] = team_name_map[game['team2Name']]
                game['team1Abbr'] = team_abbr_map[game['team1Abbr']]
                game['team2Abbr'] = team_abbr_map[game['team2Abbr']]
            except KeyError:
                pass

if write:
    with open(bracketfile, 'w') as f:
        json.dump(bracket, f, indent=4)


with open(postfile, 'r') as f:
    postseason = json.load(f)

for series in postseason:
    miniseason = postseason[series]
    for day in miniseason:
        for game in day:
            try:
                game['team1Name'] = team_name_map[game['team1Name']]
                game['team2Name'] = team_name_map[game['team2Name']]
                game['team1Abbr'] = team_abbr_map[game['team1Abbr']]
                game['team2Abbr'] = team_abbr_map[game['team2Abbr']]
            except KeyError:
                pass

if write:
    with open(postfile, 'w') as f:
        json.dump(postseason, f, indent=4)


with open(seedfile, 'r') as f:
    seed = json.load(f)

for league in seed:
    seeds = seed[league]
    newseeds = []
    for iT, team_name in enumerate(seeds):
        newseeds.append(team_name_map[team_name])
    seed[league] = newseeds

if write:
    with open(seedfile, 'w') as f:
        json.dump(seed, f, indent=4)
