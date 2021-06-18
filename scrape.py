from bs4 import BeautifulSoup
import requests

def get_soup(searchVal): 
    URL= f"https://www.dictionary.com/browse/{searchVal}"
    source = requests.get(URL).text
    soup = BeautifulSoup(source,'lxml')

    section = 'css-pnw38j e1hk9ate4'
    
    #returns list of all <section> tags that have class attribute set to css-pnw38j e1hk9ate4
    return soup.find_all('section',class_=section)
    #Add stuff to do when no results come aka this won't exist
