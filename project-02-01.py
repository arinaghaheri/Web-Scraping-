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

teams_data = []

for team_link in team_links:
    team_url = url + team_link
    response = requests.get(team_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
  
    team_name = soup.find('h1', {'class': 'team-name'}).text.strip()
    team_rank = soup.find('div', {'class': 'team-rank'}).text.strip()
    team_points = soup.find('div', {'class': 'team-points'}).text.strip()
    
    teams_data.append([team_name, team_rank, team_points])


with open('teams.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Team Name', 'Rank', 'Points'])
    writer.writerows(teams_data)
