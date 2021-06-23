import requests
from bs4 import BeautifulSoup

def main():
    # grab them animal names and make some HTML soup
    url = 'https://animals.net'
    res = requests.get(url)

    if res.status_code != 200:
        print ("Error! got a %d" % res.status_code)
        return

    page = res.text
    soup = BeautifulSoup(page, 'lxml')

    # find the table and grab a list of all the elements IN it
    animal_links = soup.select('.tagindex > div > ul > li')

    animals = []
    # loop through and grab out all the actual animal names  from the lis
    for link in animal_links:
        animal = link.text
        animals.append(animal)

    # save it all to a file
    with open('data/animals.txt', 'w') as fo: 
    
        for animal in animals:
            fo.write(animal)
            fo.write('\n')

if __name__ == '__main__':
    main()