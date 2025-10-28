import requests
from bs4 import BeautifulSoup
import csv


url = 'URL'


response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

team_links = []
for link in soup.find_all('a'):
    href = link.get('href')
    if 'team' in href:
        team_links.append(href)

players_data = []

for team_link in team_links:
    team_url = url + team_link
    response = requests.get(team_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    team_name = soup.find('h1', {'class': 'team-name'}).text.strip()
    

    players_table = soup.find('table', {'class': 'players-table'})
    for row in players_table.find_all('tr')[1:]: 
        columns = row.find_all('td')
        player_name = columns[0].text.strip()
        player_number = columns[1].text.strip()
        player_position = columns[2].text.strip()
        
        players_data.append([player_name, team_name, player_number, player_position])


with open('players.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Player Name', 'Team', 'Number', 'Position'])
    writer.writerows(players_data)
