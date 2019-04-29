import requests
import html
from bs4 import BeautifulSoup
result = requests.get("http://www.hikinginglacier.com/glacier-national-park-day-hikes.htm")
src = result.content
hike_info = BeautifulSoup(src, 'html.parser')

def hike_list():
    table_body = hike_info.find('tbody')
    rows = table_body.find_all('tr')
    cleaned_data = []
    for row in rows:
        row=row.find_all('td')
        hike_list=[x.text.replace('\n', ' ').replace('\xa0', ' ').lower()for x in row]
        cleaned_data.append(hike_list)
    return(cleaned_data)
hike_list()

header=hike_list()[0]
def hike_dict():
    hike_dict =[]
    for i in range(1, len(hike_list())):
        rows = hike_list().pop(i)
        hike_dict.append(dict(zip(header, rows)))
    return(hike_dict)
hike_dict()

def search_name():
    name_input = input("What is the name of the hike you would like to look up? ").lower()
    for i in hike_dict():
        if i['trail name']==name_input:
            return(i)
    if name_input != hike_dict():
        print("Try again")
    return search_name()


def search_loc():
    loc_input = input("What section of the park would you like to hike in? ").lower()
    for i in hike_dict():
        if i['location'] == loc_input:
            loc_list = [d for d in hike_dict() if d['location'] in loc_input]
            return loc_list
    if loc_input != hike_dict():
        print("Try again")
    return search_loc


def search_feats():
    feats_input = input("What would you like to see on your hike? Choose one: Alpine Lake, Alpine Meadow, Forest Hike, Glaciers, Historic, Lake, Lake Views, Meadows, Outstanding Views, Scenic Views, Subalpine Lake, Waterfalls, and Wildflowers. ").lower()
    for i in hike_dict():
        if i['trail features'] == feats_input:
            feats_list = [d for d in hike_dict() if d['trail features'] in feats_input]
            return feats_list
    if feats_input != hike_dict():
        print("Choose a different option")
    return search_feats


print("Welcome to the Glacier National Park Trail Database!")
def repl():
    while True:
        user_input = input("There are several ways to search for a trail to hike: \n By Name \n By Location \n By Trail Features \nChoose one or type 'exit'> ").lower()
        if user_input == 'exit':
            return
        elif user_input == 'name':
            print(search_name())
            return repl()
        elif user_input == 'location':
            print(search_loc())
            return repl()
        elif user_input == 'trail features' or 'features' or 'feature':
            print(search_feats())
            return repl()
        else:
            print("Please try again ")
            return repl()
repl()
