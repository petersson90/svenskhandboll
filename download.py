import requests
import os

def download_url(url):
  x = requests.get(url)
  if not x.status_code == 200:
    print(url, "failed with status code", x.status_code)
  else:
    print(url)
#  downloaded_obj = requests.get(url)
#  file_name = url[-16:]
#  season_id = "20" + file_name[:2]
#  division_id = file_name[:7]
#  # print(season_id, division_id, file_name)
#  directory = "tmp/" + season_id + "/" + division_id + "/"

#  if not os.path.exists(directory):
#    os.mkdir(directory)

#  with open(directory + "/" + file_name, "wb") as file:
#    file.write(downloaded_obj.content)

#  print(file_name, "saved in", directory)

if __name__ == "__main__":
  for division_id in [2113104]:
    base_url = "http://protokoll.svenskhandboll.se/"
    season_id = "20" + str(division_id)[:2]
    for match_no in range(32, 40):
      match_id = division_id * 1000 + match_no
      url = base_url + season_id + "/" + str(match_id) + "_m.pdf"
      download_url(url)
    
# download_url("http://protokoll.svenskhandboll.se/2021/2113104032_m.pdf")