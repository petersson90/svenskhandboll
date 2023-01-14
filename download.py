import requests
import os

def download_url(url):
  x = requests.get(url)
  if not x.status_code == 200:
    return f'{url} failed with status code {x.status_code}'

  file_name = url[-16:]
  season_id = "20" + file_name[:2]
  division_id = file_name[:7]
  # print(season_id, division_id, file_name)
  directory = os.path.join("tmp", season_id, division_id)
  modified = x.headers['Last-Modified']

  if not os.path.exists(directory):
    os.makedirs(directory)

  with open(os.path.join(directory, file_name), "wb") as file:
    file.write(x.content)

  return f'{file_name} saved in {directory} (last modified: {modified})'

if __name__ == "__main__":
  # with open('log_file.txt', 'w') as log_file:
    

  for division_id in [1513102, 1613102, 1713103, 1813104, 1913104, 2013104, 2113104]:
    base_url = "http://protokoll.svenskhandboll.se/"
    season_id = "20" + str(division_id)[:2]
    for match_no in range(1, 5):
      match_id = division_id * 1000 + match_no
      for file_ending in ['_m.pdf', '_a.pdf']:
        url = base_url + season_id + "/" + str(match_id) + file_ending
        print(download_url(url))
    
# download_url("http://protokoll.svenskhandboll.se/2021/2113104032_m.pdf")
