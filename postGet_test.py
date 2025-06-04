#!usr/bin/env/python3

from pprint import pprint
import requests


new_save = {
    "name": "Test Session Grudy Meshin",
    "full_dur": 200,
    "num_breaks": 4,
    "break_dur": 7,
    "long_break_dur": 20,
    "study_dur": 25,
    "study_link": "https://youtu.be/rBpApqtG7Us?si=kwFthg-jaZMDUKuO",
    "break_link": "https://youtu.be/rBpApqtG7Us?si=kwFthg-jaZMDUKuO" 
    }

requests.post("http://localhost:3000/studysessions", json=new_save, timeout= 10)

save_data = requests.get("http://localhost:3000/studysessions", timeout= 10)
save_json = save_data.json()
pprint(save_json)
