import requests
from bs4 import BeautifulSoup

def _get_html(url):

    res = requests.get(url)
    
    if res.status_code != 200:
        raise Exception("Error! got a %d" % res.status_code)
    
    page = res.text
    soup = BeautifulSoup(page, 'lxml')
    return soup

def get_us_states():

    url = "https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_income" #(one table)
    soup = _get_html(url)

    # grab the table
    state_links = soup.select('tbody:nth-of-type(2) > tr > td > a')

    # put em all in a list
    states = []
    for link in state_links:
        state = link.text
        states.append(state)
        
    return states

def get_canada_provinces():

    #(two tables)
    url = "https://en.wikipedia.org/wiki/Provinces_and_territories_of_Canada"
    soup = _get_html(url)
    
    # table 1 (provinces)
    prov_links = soup.select('tbody:nth-of-type(2) > tr > th:nth-of-type(1) > a')
    areas = []
    for link in prov_links:
        prov = link.text
        
        if 'postal' not in prov: # some random noise
            areas.append(prov)
    
    # table 2 (territories)
    links = soup.select('tbody:nth-of-type(3) > tr > th:nth-of-type(1) > a')

    for link in links:
        prov = link.text
        
        if 'postal' not in prov: # some random noise
            areas.append(prov)
            
    return areas
    
def get_uk_countries():

    url = "https://en.wikipedia.org/wiki/Countries_of_the_United_Kingdom"
    soup = _get_html(url)
    
    c_links = soup.select('tbody:nth-of-type(2) > tr > td:nth-of-type(1) > a')
    
    # put em all in a list
    countries = []
    for link in c_links:
        c = link.text
        countries.append(c)
    
    return countries
    
def get_mexico_states():

    url = "https://en.wikipedia.org/wiki/List_of_states_of_Mexico"
    soup = _get_html(url)

    # grab the table
    state_links = soup.select('tbody:nth-of-type(1) > tr > td:nth-of-type(1) > a')

    # put em all in a list
    states = []
    for link in state_links:
        state = link.text
        states.append(state)
    
    return states
    
def get_aus_states():

    url = "https://en.wikipedia.org/wiki/States_and_territories_of_Australia"
    soup = _get_html(url)
    
    # grab the table
    state_links = soup.select('tbody:nth-of-type(3) > tr > td > b > a')

    # put em all in a list
    states = []
    for link in state_links:
        state = link.text
        states.append(state)
        
    return states
    
def get_italy_states():

    url = "https://en.wikipedia.org/wiki/Regions_of_Italy"
    
    soup = _get_html(url)

    # grab the table
    state_links = soup.select('tbody:nth-of-type(2) > tr > td:nth-of-type(2) > b > a')

    # put em all in a list
    states = []
    for link in state_links:
        state = link.text
        states.append(state)
        
    return states
    
    
def main():

    # get all the places
    us = get_us_states()
    uk = get_uk_countries()
    can = get_canada_provinces()
    mex = get_mexico_states()
    aus = get_aus_states()
    it = get_italy_states()
    
    places = us + uk + can + mex + aus + it
    
    # save it all to a file
    with open('data/places.txt', 'w') as fo: 
    
        for place in places:
            fo.write(place)
            fo.write('\n')


if __name__ == "__main__":
    
    main()
    

    
    
    

    