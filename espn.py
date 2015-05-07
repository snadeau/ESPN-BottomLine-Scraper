import urllib2
import urllib
import re

espn_urls = {'nfl': 'http://sports.espn.go.com/nfl/bottomline/scores',
             'nba': 'http://sports.espn.go.com/nba/bottomline/scores',
             'mlb': 'http://sports.espn.go.com/mlb/bottomline/scores',
             'nhl': 'http://sports.espn.go.com/nhl/bottomline/scores',
             'ncf': 'http://sports.espn.go.com/ncf/bottomline/scores',
             'ncb': 'http://sports.espn.go.com/ncb/bottomline/scores'}

remove_rankings = ['(1)','(2)','(3)','(4)','(5)','(6)','(7)','(8)','(9)',
                   '(10)','(11)','(12)','(13)','(14)','(15)','(16)','(17)',
                   '(18)','(19)','(20)','(21)','(22)','(23)','(24)','(25)']
                   

def get_content(url):
    response = urllib2.urlopen(url)
    content = response.read()
    return content

content = get_content(espn_urls['mlb'])
strings = content.split('&')
scores = []
for string in strings:
    if 'left' in string:
        if string.endswith('(FINAL)'):
            newstring = string[string.find('=')+1:string.find('(FINAL)')]
            newstring = newstring.replace('^', '')
            newstring = urllib.unquote(newstring)
            for n in remove_rankings:
                newstring = newstring.replace(n, '')
            scores.append(newstring.strip())

list_teams = []
list_scores = []

for score in scores:
    results = re.findall(r'\d+', score)
    teams = re.findall(r'\D+', score)
    new_teams = [team.strip() for team in teams]
    list_teams.append(new_teams)
    list_scores.append(results)

compiled_results = zip(list_teams, list_scores)
print compiled_results

    
        
    


    
    
            
