from bs4 import BeautifulSoup
import requests

def get_soup(searchVal):
    #URL format equivalent to going to dictionary.com and searching the argument
    URL= f"https://www.dictionary.com/browse/{searchVal}"
    #getting html source code
    source = requests.get(URL).text
    #parsing it using BeautifulSoup and lxml as the parser
    soup = BeautifulSoup(source,'lxml')

    #the html class of the section we want from dictionary.com : css-pnw38j e1hk9ate4
    section = 'css-pnw38j e1hk9ate4'
    
    #returns list of all <section> tags that have class attribute set to css-pnw38j e1hk9ate4
    return soup.find_all('section',class_=section)
    #Add stuff to do when no results come aka this won't exist

#rename me
def func(section):
    heading = section.h3.span.text
    
    #meanings exist in div elements
    #find_all useful as some words have multiple meaning within the same heading
    meanings = section.div.find_all('div')
    for meaning in meanings:
        print(meaning.prettify())

    
func(get_soup('fuck')[1])
